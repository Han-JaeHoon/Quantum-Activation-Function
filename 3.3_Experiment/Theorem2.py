# Quantum
import pennylane as qml

# Numericlal
import math
import numpy as np
import sympy as sp

# Torch
import torch

# Self-Defined class
from Theorem1 import Theorem1

class Theorem2(Theorem1):
    '''
        Theorem 2(보고서의 Theorem 3.1.1)을 구현하기 위한 class
    '''
    def __init__(self, w, x, b, d, f, l = 0):
        '''
            w, x, b, d : same as Thm1
            f(str) : name of function which will be sympified
        '''

        super().__init__(w, x, b, d, l=l)
        self.f = sp.sympify(f)  # target f
        self.k = -1             # target f의 taylor expansion 중 계수가 0이 아닌 최저 차수
        self.C_d = 1            # f_d(z)와 실제 f(z)의 factoring constant
        self.theta_list = self.make_theta_list()


    def taylor_series_coefficients(self):
        # 심볼 정의
        z = sp.symbols('z')
        point = 0.0

        # 테일러 전개 계산
        taylor_expansion = sp.series(self.f, z, point, self.d + 1).removeO()

        # 계수 추출
        coeffs = [taylor_expansion.coeff(z, i) for i in range(self.d + 1)]
        return coeffs

    def make_theta_list(self):
        # Get Coeffs of Taylor (polynomial) Expansion of target f
        coefficients = self.taylor_series_coefficients()

        # Update k (target f의 taylor expansion 중 계수가 0이 아닌 최저 차수)
        for i in range(0, self.d + 1):
            if coefficients[i] != 0:
                self.k = i
                break

        theta_list = [0 for _ in range(self.d)]
        # target f = 0
        if self.k < 0:
            return theta_list

        # a_i = 0 for all i < k
        for i in range(self.k):
            theta_list[i] = -1 * math.pi / 2

        # a_k Initiallization
        theta_list[self.k] = math.atan(-1 * coefficients[self.k + 1] / coefficients[self.k])

        A = 1
        for i in range(self.k + 1, len(coefficients) - 1):
            A *= math.cos(theta_list[i - 1])
            theta_list[i] = math.atan(-1 * coefficients[i + 1] / coefficients[self.k] * A)

        # C_d update
        C_d = coefficients[self.k] # a_k
        for i in range(self.k, self.d):
            C_d /= math.cos(theta_list[i]) # 1/cos(theta)
        self.C_d = torch.tensor([float(C_d)])

        return theta_list

    def U(self, d):
        '''
            U_d Unitary for S_U iteration
        '''
        theta_list = self.theta_list # make_theta_list()
        for k in range(1, d):
            a_0 = self.s + self.n
            a_k = a_0 + k
            qml.ctrl(qml.RY, control=a_k, control_values=0)(2 * theta_list[k - 1], wires=a_0)
            qml.CNOT(wires=[a_0, a_k])

    def outer_theorem2(self):
        '''
            S_U := d register에는 U_d, q register에는 Pauli-X for each qubit
        '''
        # Pauli-X for each qubit of q register
        # and S_V
        self.outer_theorem1()

        qml.Barrier()

        # U_d
        self.U(self.d)

        qml.Barrier()

        # Pauli-X for each qubit of q register
        for i in range(self.n):
            q_i = self.s + i
            qml.PauliX(wires=q_i)

    def theorem2(self, chk=False):
        @qml.qnode(device=self.dev, interface="torch")
        def inner_theorem2():
            self.outer_theorem2()
            return qml.state()
        if chk:
            print(qml.draw_mpl(self.outer_theorem2)())
        return inner_theorem2()

    def corollary2(self, k, w_index):
        '''
            as same as col 1,
            k를 input으로 받아, |N-1>(q)|2^k - 1>(a) state에 대한 amplitude를 return
        '''
        result = self.theorem2()
        w_bitstring = '0' * (self.s - len(bin(w_index)[2:])) + bin(w_index)[2:]
        bitstring = w_bitstring + ('0' * self.n) + ('0' * (self.d ))
        index = int(bitstring, 2)

        return result[index] * (2 ** (self.s / 2 + self.d / 2)) * self.C_d # * C_d

    def get_z_list(self):
        result = self.theorem2()
        z_list= []
        for i in range(self.output_num):
            w_bitstring = '0' * (self.s - len(bin(i)[2:])) + bin(i)[2:]
            bitstring = w_bitstring + ('0' * self.n) + ('0' * (self.d ))
            index = int(bitstring, 2)
            z_list.append(result[index] * (2 ** (self.s / 2 + self.d / 2)) * self.C_d)

        return torch.tensor(z_list)