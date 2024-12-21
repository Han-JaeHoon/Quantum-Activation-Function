# Quantum Activation Function

# Task

Implement Quantum Multi-Perceptron Layer with Arbitrary Activation Function

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

![2d](3.3_Experiment/imgs/lemma1.png)|


- $Theorem1$

![2d](3.3_Experiment/imgs/Theorem1.png)|


- $Theorem2$

![2d](3.3_Experiment/imgs/Theorem2.png)|

- Result

![2d](3.3_Experiment/imgs/output.png)|
