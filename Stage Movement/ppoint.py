import numpy as np
import matplotlib.pyplot as plt

CA_ref = np.array([80, 0, 250])

# user desired displacements
ux = 0
uy = 0
uz = 0

theta_x_deg = 1
theta_y_deg = 0
theta_z_deg = 0

QP = np.array([ux, uy, uz]) # Vector from reference position on sample (Q) to desired position on sample (P)

def c(theta):
    return np.cos(theta)

def s(theta):
    return np.sin(theta)

def rotation_x(theta):
    R = np.array([[1, 0, 0], [0, c(theta), -s(theta)], [0, s(theta), c(theta)]])
    return R

def rotation_y(theta):
    R = np.array([[c(theta), 0, s(theta)], [0, 1, 0], [-s(theta), 0, c(theta)]])
    return R

def rotation_z(theta):
    R = np.array([[c(theta), -s(theta), 0], [s(theta), c(theta), 0], [0, 0, 1]])
    return R

def calc_rotation_matrix(theta_x_deg, theta_y_deg, theta_z_deg):
    R_x = rotation_x(np.deg2rad(theta_x_deg))

    R_y = rotation_y(np.deg2rad(theta_y_deg))

    R_z = rotation_z(np.deg2rad(theta_z_deg))

    R = np.matmul(R_y, R_z)
    R = np.matmul(R_x, R)
    return R

R = calc_rotation_matrix(theta_x_deg, theta_y_deg, theta_z_deg)

OC = QP + CA_ref - np.matmul(R, CA_ref)

print("Requires stage translation of:")
print("x = {0:.3f}mm".format(OC[0]))
print("y = {0:.3f}mm".format(OC[1]))
print("z = {0:.3f}mm".format(OC[2]))