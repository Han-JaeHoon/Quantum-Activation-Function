# Quantum
import pennylane as qml

# Numericlal
import numpy as np

# Torch
import torch

# Plot
import matplotlib.pyplot as plt

# Self-Defined class
from Lemma1 import Lemma1

class Theorem1(Lemma1):
    '''
        QAF 논문 Theorem 1을 구현하기 위한 class
    '''
    def __init__(self, w, x, b, d, l = 0):
        '''
            w(matrix, tensor) : tensor for weights [row0 : w0, row1 : w1, ...], (output_num x input_num)
            x(tensor) : tensor for x(input, list)
            b(tensor) : tensor for bias_list
            d(int)      : degree for Taylor (polynomial) Expansion
        '''
        super().__init__(w, x, b, output_num=len(b))
        self.d = d
        self.l = l

        # device initiallize
        # n : num_qubit
        self.dev = qml.device("default.qubit", wires=(self.s + self.n + self.d + self.l))

    def V(self, m):
        a_m = self.s + self.n + m

        # Controlled-Hadamard for (control, target) : (q register, a_m)
        qml.ctrl(qml.Hadamard, control=range(self.s, self.s + self.n))(wires=a_m)

        # CNOT for (control, target) : (a_m, q register)
        for i in range(self.n):
            q_i = self.s + i
            qml.CNOT(wires=[a_m, q_i])

        # Controlled-U(x, w, b) for : (a_m, q register)
        qml.ctrl(self.U_z, control=a_m)()

    def outer_theorem1(self):
        '''
            Pauli-X 후 S_V(V_0, V_1, ... , V_{d-1})
        '''
        # Pauli-X for each qubit of q register
        for i in range(self.n):
            q_i = self.s + i
            qml.PauliX(wires=q_i)

        self.hadamard_s()
        qml.Barrier()
        # V_m for each m in (0, ... , d - 1)
        for m in range(self.d):
            self.V(m)
            qml.Barrier()

    def theorem1(self, chk=False):
        '''
            Theorem 1의 state |psi_z^d> 를 생성해서, state vector를 return
        '''
        @qml.qnode(device=self.dev)
        def inner_theorem1():
            self.outer_theorem1()
            return qml.state()
        if chk:
            print(qml.draw_mpl(inner_theorem1)())
        return inner_theorem1()

    def corollary1(self, k, w_index):
        '''
            k를 input으로 받아, |w_index>(s) |N-1>(q)|2^k - 1>(a) state에 대한 amplitude를 return
        '''
        result = self.theorem1()
        w_bitstring = '0' * (self.s - len(bin(w_index)[2:])) + bin(w_index)[2:]
        bitstring = w_bitstring + ('1' * self.n) + ('0' * (self.d - k)) + ('1' * k)
        index = int(bitstring, 2)
        return (result[index] * (2 ** ((self.s / 2) + (self.d / 2)))) ** (1 / k)

    def get_z_list(self):
        '''
            k=d 고정, 모든 weight에 대한 z값 리스트 리턴
        '''
        return torch.tensor([float(self.corollary1(k=self.d, w_index=i)) for i in range(self.output_num)])