# Quantum Activation Function

# Task

Implement Quantum Multi-Perceptron Layer with Arbitrary Activation Function

you can see our project detailed in this [report](https://drive.google.com/file/d/1kGv0sO4jSNgf3AKtDqZVUwL6kSgcO_Y6/view?usp=drive_link).


# HOW TO

```bash
cd Quantum-Activation-Function

#use python 3.12.6 version
pip install -r requreiment.txt

#1d-function
cd 1d-function
python3 main.py

#2d-function
cd 2d-image
python3 main.py

#revise config.py for set parameter
python3 main.py
```




## 1d-function
  - Model
    ![2d](2.2_Comparison_of_ML_and_QML/imgs/pqc_1d_color.png)|


- Numerical results
  | layer | $\sin{x}$|$\tanh{x}$ | $\frac{1}{2{\pi}}x$ |
  |---|---|---|---|
  |MLP (3 layers) | 0.0 | 0.0 | 0.0| \\
  |MLP (4 layers) | 0.0 | 0.0 | 0.0 |
  |MLP (5 layers) | 0.0 | 0.0 | 0.0 |
  |PQC (3 layers) | 0.0 | 0.0 | 0.003 |
  |PQC (4 layers) | 0.0 | 0.0 | 0.003 |
  |PQC (5 layers) | 0.0 | 0.0 | 0.003 |

   | $\sin{x}$| $\frac{1}{2{\pi}x}$|
   |---|---|
   | ![2d](2.2_Comparison_of_ML_and_QML/imgs/qml_ml_sin.png)| ![2d](2.2_Comparison_of_ML_and_QML/imgs/qml_ml_x.png)| |




## 2d-function

  - Model
    ![2d](2.2_Comparison_of_ML_and_QML/imgs/pqc_2d_color.png)|


| Image 1 | Image 2 | Image 3 |
|---|---|---|
| MLP (3 layers) | 15.826 | 16.913 | 15.884 |
| MLP (4 layers) | 15.816 | 17.049 | 16.328 |
| MLP (5 layers) | 15.811 | 16.606 | 16.306 |
| PQC (3 layers) | 14.503 | 16.269 | 15.470 |
| PQC (4 layers) | 15.624 | 16.464 | 15.471 |
| PQC (5 layers) | 4.484 | 6.912 | 8.786 |


  |Method | Image1| Image2| Image3|
   |---|---|---|---|
   |Origin|![2d](2.2_Comparison_of_ML_and_QML/2d-image/resize_images/test1.jpg) |![2d](2.2_Comparison_of_ML_and_QML/2d-image/resize_images/test2.jpg) | ![2d](2.2_Comparison_of_ML_and_QML/2d-image/resize_images/test3.jpg)|
   |MLP| ![2d](2.2_Comparison_of_ML_and_QML/imgs/MLP_test_image0.png)| ![2d](2.2_Comparison_of_ML_and_QML/imgs/MLP_test_image1.png)|![2d](2.2_Comparison_of_ML_and_QML/imgs/MLP_test_image2.png) |
   |PQC| ![2d](2.2_Comparison_of_ML_and_QML/imgs/PQC_test_image0.png)| ![2d](2.2_Comparison_of_ML_and_QML/imgs/MLP_test_image1.png)| ![2d](2.2_Comparison_of_ML_and_QML/imgs/PQC_test_image2.png)|



## QAF

- $Lemma1$

Given Input vector $\vec{x} \in [-1, 1]^{N_{in}} $, weight matrix $W:= \begin{pmatrix}
    \vec{w}_0 \\ \vec{w}_1 \\ \vdots \\ \vec{w}_{N_w - 1}
\end{pmatrix} $ , bias vector $\vec{b} \in [-1, 1]^{N_w} $, and given registers s, q with p, n qubit respectively, such that $n = \left\lceil \log_2(N_{in} + 3) \right\rceil, p = \left\lceil \log_2(N_w) \right\rceil $, then, there exists a quantum circuit $U_{\mathbf z}(\vec{x}, W, \vec{b}) $ such that

${}_{s}\langle{i}| {}_{q}\langle N-1|U_{\mathbf z}(\vec{x}, W, \vec{b})\ket{0}_q \ket{0}_s = {\vec{w}_i \cdot {\vec{x} + 1} \over {N_{in} + 1}} \equiv {z_i \over {{2^{p/2}}}} \quad \text{ for } i = 0, 1, \cdots , N_{w} - 1$

$\text{where } \ket{0}_q \equiv \ket{0}^{\otimes n}, \ket{0}_s \equiv \ket{0}^{\otimes p}, \ket{N-1}_q \equiv \ket{1}^{\otimes n},\text{ and } \vec{w}_i \in [-1, 1]^{N_{in}} \text{ for } i = 0, 1, \cdots, N_w - 1$

![2d](3.3_Experiment/imgs/lemma1.png)|


- $Theorem1$

Let $z_i := \left( \vec{w}_i \cdot \vec{x} + b_i \right) / \left( N_{in} + 1 \right)$ where $\vec{x}, \vec{w}_i \in [-1, 1]^{N_{in}}$ and $b_i \in [-1, 1]$ for $i = 0, \cdots, N_w - 1$. Let $q, a, \text{ and } s$ be quantum registers of $n, d, \text{ and } p$ qubits respectively, with $ N = 2^n \ge N_{in} + 3 $ and $ p = \left\lceil \log_2(N_{w}) \right\rceil$. Then there exist a quantum circuit which transforms the three registers from the initial state $\ket{0}_s \ket{0}_a \ket{0}_q$ to (p+n+d)-qubit entangled state $\ket{\psi_{\mathbf z}^d}$ of the form
   $
        \ket{\psi_{\mathbf z}^d} = \ket{\psi_{\mathbf z}^d}_{\perp} + {1 \over {2^{(d + p) / 2}}}\sum_{i=0}^{N_w - 1}\left( \ket{i}_{s} \ket{z_i}_{a}^{\otimes d} \ket{N-1}_q \right)
   $
    where
   $
        \ket{N-1}\bra{N-1}_q \ket{\psi_\mathbf{z}^d}_{\perp} = \mathbf{0}
   $
    and
    $
        \ket{z_i} \equiv \ket{0} + z_i\ket{1}
   $
    The circuit is expressed by $S_V X_q^{\otimes n} H_s^{\otimes p}$ where X is Pauli-X, H is Hadamard gate and
    $
        S_V = V_{d-1} \cdots V_1 V_0
   $
    with
    $
        V_m = C_{a_m}S_{\mathbf{z}}(\vec{x}, W, \vec{b})_q C_{a_m}X^{\otimes n}_q C_q^nH_{a_m} \quad \text{ for } m = 0, 1, \dots, d - 1
   $

![2d](3.3_Experiment/imgs/Theorem1.png)|


- $Theorem2$

    Let $\{f_k, k = 1, \ldots, d\}$ be the family of polynomials in $z$ defined by the following recursive law:

$f_k(z) = f_{k-1}(z) \cos \vartheta_{k-1} - z^k \sin \vartheta_{k-1}, \quad k = 1, \ldots, d.$
with $f_0(z) = 1$ and $\vartheta_k \in \left
[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ for any $k = 0, \ldots, d-1$.

Then there exists a family $\{U_k, k = 1, \ldots, d\}$ of unitary operators such that
$
{}_{a}\bra{0} U_k \ket{z}_a^{\otimes d} = f_k(z).
$

These unitary operators are, in turn, defined by the recursive law:
$
U_k = C_{a_0} X_{a_k} \overline{C}_{a_k} R_y(2 \vartheta_{k-1})_{a_0} U_{k-1}, \quad k = 1, \ldots, d,
$
with $U_0 = \mathbb{1}$.


![2d](3.3_Experiment/imgs/Theorem2.png)|

- Result

![2d](3.3_Experiment/imgs/output.png)|
