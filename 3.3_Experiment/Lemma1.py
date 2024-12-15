# Quantum
import pennylane as qml

# Numericlal
import numpy as np

# Torch
import torch

# Plot
import matplotlib.pyplot as plt

class Lemma1:
    '''
        Lemma 1(보고서의 Lemma 3.2.1)을 구현하기 위한 class
    '''
    def __init__(self, w, x, b, output_num):
        '''
            w(matrix, tensor) : tensor for weights [row0 : w0, row1 : w1, ...], (output_num x input_num)
            x(tensor) : tensor for x(input, list)
            b(tensor) : tensor for bias_list
            output_num(int) : number of output perceptrons (same as len(b))
        '''
        # list(tensor) Initiallize
        self.w = w
        self.x = x
        self.b = b
        self.output_num = output_num

        # lengths Calculate
        self.N_in = len(x)
        self.N = int(2 ** (np.ceil(np.log2(self.N_in + 3))))
        self.n = int(np.log2(self.N))
        self.s = int(np.ceil(np.log2(self.output_num)))

        # About x
        self.A_x  = torch.sqrt(torch.tensor(self.N_in) - (self.x @ self.x))
        self.v_x  = torch.cat(( self.A_x.unsqueeze(0)  ,self.x , torch.tensor([1.0]) ,torch.tensor([0.0] * (self.N - self.N_in - 2))))

        # About w, b
        self.A_wb = torch.zeros(self.output_num)
        self.v_wb = torch.zeros(self.output_num, self.N)
        for i in range(len(self.w)):
            self.A_wb[i] = torch.sqrt(torch.tensor(self.N_in) + 1 - (self.w[i] @ self.w[i] + self.b[i] * self.b[i]))
            self.v_wb[i] = torch.cat((torch.tensor([0.0]), self.w[i], self.b[i].unsqueeze(0), torch.tensor([0.0] * (self.N - self.N_in - 3)), self.A_wb[i].unsqueeze(0)))

        self.start_indexes = {
            's' : 0,
            'q' : self.s
        }

        # device initiallize
        # n : num_qubit
        self.dev = qml.device("default.qubit", wires=self.s+self.n)

    def qubit_index(self, name):
        register_name = name[0]
        register_index = int(name[1:])
        return self.start_indexex[register_name] + register_index

    def norm(self, vec):
        return np.linalg.norm(vec)

    def u(self, vec):
        '''
            small u(v_x)
        '''
        qml.AmplitudeEmbedding(vec, wires=range(self.s, self.s + self.n), normalize=True)

    def k_to_control_wire_list(self, k):
        return [int(i) for i in ('0' * (self.s - len(bin(k)[2:]))) + bin(k)[2:]]

    def U_wb(self, index):
        # U_wb, i.e. small_u(v_wb)^†, Pauli-X for each qubit
        qml.adjoint(self.u)(self.v_wb[index])

    def U_z(self):
        # U_x, i.e. small_u(v_x)
        self.u(self.v_x)

        # qml.Barrier()

        for i in range(self.output_num):
            qml.ctrl(self.U_wb, control=range(self.s), control_values=self.k_to_control_wire_list(i))(i)
            # qml.Barrier()

        # Pauli-X for q register
        q0 = self.s
        for i in range(self.n):
            qml.PauliX(wires=q0+i)

    def hadamard_s(self):
        # Hadamard for all qubit of l register
        for i in range(self.s):
            qml.Hadamard(wires=i)

    def outer_lemma1(self):
        self.hadamard_s()
        self.U_z()


    def lemma1(self, chk=False):
        @qml.qnode(device=self.dev ,interface="torch")
        def inner_lemma1():
            self.outer_lemma1()
            return qml.state()
        if chk:
            print(qml.draw_mpl(inner_lemma1)())
        return inner_lemma1()

    def get_z(self, k, chk=False):
        '''
            k번째 wegiht에 대한 z를 구해준다.
        '''
        bit_string = '0' * (self.s - len(bin(k)[2:])) + bin(k)[2:]
        index = int(bit_string + '1' * self.n, 2)
        result = self.lemma1(chk=chk)
        return result[index] * (2 ** (self.s / 2))

    def get_z_list(self):
        return torch.tensor([float(self.get_z(i)) for i in range(self.output_num)])