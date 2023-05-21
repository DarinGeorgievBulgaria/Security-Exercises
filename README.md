# Security-Exercises

## Repeating XOR Encrypt
This is an implementation of a function which encrypts a finite string by XORing it against a repeating key and returns the hex value as a string. The length of the key is less or equal to the length of the plaintext.

https://github.com/DarinGeorgievBulgaria/Security-Exercises/blob/main/RepeatingXOREncrypt.py

## Diffie-Hellman Encrypt
This is function demonstrates how users A and B use the Diffie-Hellman (DH) key exchange protocol to share a secret key and start encrypting data. It is assumed that users A and B agreed on some DH parameters and calculated their private keys. I used keys below for examples:

User's A private key (in PEM, no password protected):

b'-----BEGIN PRIVATE KEY-----
\nMIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAlry2DwPC+pK/0QiOicVAtt6ANsfjmD9P\nQrDC6Zk
YcrRf0q0RVzMDTnHWk1mRLVvb6av4HOSkIsk1mMogBcqV0wIBAgRCAkBm\nZK4qUqvU6WaPy4fN
G9oWIXchxzztxmA7p9BFXbMzn3rHcW84SDwTWXAjkRd35XPV\n/9RAl06sv191BNFFPyg0\n---
--END PRIVATE KEY-----\n'


User's B private key (in PEM, no password protected):

b'-----BEGIN PRIVATE KEY-----
\nMIGcAgEAMFMGCSqGSIb3DQEDATBGAkEAlry2DwPC+pK/0QiOicVAtt6ANsfjmD9P\nQrDC6Zk
YcrRf0q0RVzMDTnHWk1mRLVvb6av4HOSkIsk1mMogBcqV0wIBAgRCAkBn\n9zn/q8GMs7SJjZ+V
LlPG89bB83Cn1kDRmGEdUQF3OSZWIdMAVJb1/xaR4NAhlRya\n7jZHBW5DlUF5rrmecN4A\n---
--END PRIVATE KEY-----\n'

https://github.com/DarinGeorgievBulgaria/Security-Exercises/blob/main/DHandEncrypt.py

## AES in CTR mode Encryption
The code defines a function called AES_CTR_Encrypt that encrypts a plaintext message using AES-CTR encryption mode. The function takes a hexadecimal string key representing the encryption key, another hexadecimal string nonce_counter representing the initial value of the nonce and counter used by CTR mode, and a plaintext message data represented as a byte string.

The function creates an AES-CTR cipher and encryptor using the key and nonce_counter. It then encrypts the data using the created encryptor and returns the resulting ciphertext.

https://github.com/DarinGeorgievBulgaria/Security-Exercises/blob/main/AES%20CTR%20Encrypt.py

## Annualized Loss Expectancy (ALE) Calculation
### Description
This code implements a set of calculations and simulations to analyze risk exposure and estimate the Annualized Loss Expectancy (ALE) for a given scenario. The code utilizes statistical distributions, such as the triangular, log-normal, and Pareto distributions, as well as the Monte Carlo method to generate probabilistic outcomes.

The Task1 function in the code performs the following tasks:

1. Calculates probabilities related to the Asset Value (AV):

 - It uses a triangular distribution to determine the probability that the AV is no greater than a specified point (point1) and the probability that the AV is greater than another specified point (point2).
 - It calculates the mean and median of the AV based on the triangular distribution.

2. Calculates the mean and variance of a given data set:
- It converts the input data into a numpy array and computes the mean and variance.

3. Performs a Monte Carlo simulation to estimate the probability distribution of the total impact:
- It creates log-normal and Pareto distributions to represent the impact caused by two flaws.
- It samples from these distributions a specified number of times (num) and calculates the total impact as the sum of the samples.
- It determines the probability that the total impact is greater than a specified point (point3) and the probability that it falls within a range defined by two points (point4 and point5).

4. Calculates the Annualized Loss Expectancy (ALE):
- It uses the median of the triangular distribution as the Single Loss Expectancy (SLE) and the probability derived from the Monte Carlo simulation as the Exposure Factor (EF).
- It computes the Annual Rate of Occurrence (ARO) as the mean of the input data set.
- It calculates the ALE as the product of ARO and SLE.

The code allows for customization by providing input values for various parameters such as the limits and mode of the triangular distribution, data set, simulation parameters, and thresholds for impact probability.
The results of the calculations are stored in the results variable and printed to the console.
https://github.com/DarinGeorgievBulgaria/Security-Exercises/blob/main/ALE.py

## Linear Regression and Linear Programming
### Description
This code implements a linear regression and two linear programming tasks to solve optimization problems. The goal is to find optimal weights and values that satisfy certain constraints.
The function performs the following tasks:

1. Linear Regression:
- It performs linear regression using the input data x and corresponding dependent variables y and z.
- The regression equation is solved using the least squares method, and the resulting weights for y and z are obtained.
- The weights are stored in weights_b and weights_d variables.

2. Linear Programming Task 1:
- It formulates a linear programming problem with constraints using the obtained weights and other input parameters.
- The goal is to maximize the value of num5 while satisfying the constraints defined by bound_y and bound_z.
- The linear programming problem is solved using the linprog function from the SciPy library.
- The optimal value of num5 is stored in s_num5.

3. Linear Programming Task 2:
- It formulates another linear programming problem with different constraints using the same weights and additional input parameters.
- The goal is to maximize a cost function defined by the c vector while satisfying constraints defined by se_bound, ml_bound, x_bound, and x_initial.
- The linear programming problem is solved using the linprog function.
- The optimal values for the decision variables are stored in x_i.
- The differences between the optimal values and the initial values of the decision variables are stored in x_add.

The code allows for customization by providing input values for the data matrix x, dependent variables y and z, various parameters for the linear programming tasks, and initial values for the decision variables.
The results of the calculations are stored in the result variable and printed to the console.
https://github.com/DarinGeorgievBulgaria/Security-Exercises/blob/main/Linear%20Programming%20and%20Regression%20.py
