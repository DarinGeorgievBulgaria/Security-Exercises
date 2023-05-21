import numpy as np
from scipy.optimize import linprog

def LinearRegr(x, y, z, num1, num2, num3, num4, bound_y, bound_z, c,
          se_bound, ml_bound, x_bound, x_initial):

    # (1) - Linear regression
    m = np.transpose(x)
    m = np.column_stack((np.ones(m.shape[0]), m))

    weights_b = np.linalg.lstsq(m, y, rcond=None)[0]
    weights_d = np.linalg.lstsq(m, z, rcond=None)[0]

    #(2) - Linear programming 1
    k = [0, 0, 0, 0, 1]  
    A = [np.negative(weights_b[1:]), weights_d[1:]]
    b = [weights_b[0]-bound_y, bound_z-weights_d[0]]

    res = linprog(k, A_ub=A, b_ub=b, bounds=[(num1, num1), (num2, num2),
        (num3, num3), (num4, num4), (0, None)])

    s_num5 = res.x[-1]

    k = np.negative(k)

    res = linprog(k, A_ub=A, b_ub=b, bounds=[(num1, num1), (num2, num2),
        (num3, num3), (num4, num4), (0, None)])

    l_num5 =res.x[-1]

    #(3) - Linear programming 2
    b = [weights_b[0]-se_bound, ml_bound-weights_d[0]]

    res = linprog(c, A_ub=A, b_ub=b, bounds=[(x_initial[0], x_bound[0]),
        (x_initial[1], x_bound[1]), (x_initial[2], x_bound[2]),
        (x_initial[3], x_bound[3]), (x_initial[4], x_bound[4])])
    
    x_i = np.ceil(res.x)

    x_add = np.subtract(x_i, x_initial)

    return (weights_b, weights_d, s_num5, l_num5, x_add)


# Input data
x = [[5, 4, 8, 8, 2, 5, 5, 7, 8, 8],
     [3, 7, 7, 2, 2, 5, 10, 4, 6, 3],
     [8, 3, 6, 7, 9, 10, 6, 2, 2, 3],
     [9, 3, 9, 3, 10, 4, 2, 3, 7, 5],
     [4, 9, 6, 6, 10, 3, 8, 8, 4, 6]]

y = [176, 170, 215, 146, 228, 145, 183, 151, 160, 151]
z = [352, 384, 471, 358, 412, 345, 449, 357, 366, 349]

num1, num2, num3, num4, bound_y, bound_z = 5, 6, 8, 4, 160, 600

c = [11, 6, 8, 10, 9]
se_bound = 1000
ml_bound = 2000
x_bound = [30, 50, 20, 45, 50] 
x_initial = [3, 5, 4, 2, 1]

result = LinearRegr(x, y, z, num1, num2, num3, num4, bound_y, bound_z, c,
          se_bound, ml_bound, x_bound, x_initial)

print(result)


