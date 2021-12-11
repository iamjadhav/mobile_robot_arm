import numpy as np
import sympy as sy
from sympy import nsimplify
from sympy.physics import mechanics as mc

def s(x):
    return sy.sin(x)


def c(x):
    return sy.cos(x)


pi = np.pi
armTh = mc.dynamicsymbols('armTh')

th, al, a, d, th1, th2, th3, th4, Z1, Z2, Z3, Z4, d1, d2, d3, d4, t = sy.symbols(
    'th, al, a, d, th1, th2, th3, th4, Z1, Z2, Z3, Z4, d1, d2, d3, d4, t')

A = sy.Matrix([[c(th), -s(th) * c(al), s(th) * s(al), a * c(th)],
               [s(th), c(th) * c(al), -c(th) * s(al), a * s(th)],
               [0, s(al), c(al), d],
               [0, 0, 0, 1]])

th_list = [th1, th2, th3, th4]
al_list = [pi / 2, 0, 0, pi / 2]
d_list = [290, 840, 795, 320]
a_list = [154, 330, 400, 0]
init_th = [pi/3, 0, -pi/4, pi]


def calculate_A_matrix(ali, ai, thi, di):
    global A, e
    A_transform = nsimplify(A.subs({al: ali, a: ai, th: thi, d: di}), tolerance=1e-3, rational=True)
    return A_transform


def calculate_T_matrix():
    A1 = calculate_A_matrix(al_list[0], a_list[0], th_list[0], d_list[0])
    A2 = calculate_A_matrix(al_list[1], a_list[1], th_list[1], d_list[1])
    A3 = calculate_A_matrix(al_list[2], a_list[2], th_list[2], d_list[2])
    A4 = calculate_A_matrix(al_list[3], a_list[3], th_list[3], d_list[3])

    T1 = A1
    T2 = (T1 * A2)
    T3 = (T2 * A3)
    T4 = (T3 * A4)
    return T1, T2, T3, T4


T1, T2, T3, T4 = calculate_T_matrix()


def ZMatrix_calculator(T1, T2, T3, T4):
    Z1 = T1[:3, 2]
    Z2 = T2[:3, 2]
    Z3 = T3[:3, 2]
    Z4 = T4[:3, 2]
    ZMatrix = [Z1, Z2, Z3, Z4]
    return ZMatrix


def Jcalculator(joint_angle):
    global T4
    th = [th1, th2, th3, th4]
    Th_values = [joint_angle[0], joint_angle[1], joint_angle[2], joint_angle[3]]

    j = T4[:3, 3]
    ZMatrices = ZMatrix_calculator(T1, T2, T3, T4)

    j1 = j.jacobian(th)

    Z = ZMatrices[0].row_join(ZMatrices[1].row_join(ZMatrices[2].row_join(ZMatrices[3])))

    j2 = j1.col_join(Z)
    j2 = nsimplify(change_values(j2, Th_values), tolerance=1e-3, rational=True)
    j2 = np.array(j2)
    return j2

def change_values(J_updated, theta):
    J_updated = J_updated.subs({th1: theta[0],
                                th2: theta[1], th3: theta[2], th4: theta[3]})
    J_updated = nsimplify(J_updated, tolerance=1e-3, rational=True)
    return J_updated


joint_angles =[0, 0, pi/2, 0]
T4 = nsimplify(T4.subs({th1:joint_angles[0], th2:joint_angles[1], th3:joint_angles[2], th4:joint_angles[3]}), tolerance=1e-5, rational=True)
disp_mat = list(np.array(T4).astype(float)[:3,2])
J = Jcalculator(th_list)
print("Final Transformation Matrix", T4)
print("Jacobian Matrix", J)