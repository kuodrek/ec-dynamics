# Put the non-dimensional derivatives into the local namespace
locals().update(B747_lat_ders)

Yv = q * S / m / U0 * CY_b
Yp = 0
Yr = 0
Lv = q * S * b / Ixx / U0 * CMl_b
Lp = q * S * b**2 / 2 / Ixx / U0 * CMl_p
Lr = q * S * b**2 / 2 / Ixx / U0 * CMl_r
Nv = q * S * b / Izz / U0 * CMn_b
Np = q * S * b**2 / 2 / Izz / U0 * CMn_p
Nr = q * S * b**2 / 2 / Izz / U0 * CMn_r


print(f"Yv = {Yv:1.4f}")
print(f"Yp = {Yp:1.4f}")
print(f"Yr = {Yr:1.4f}")
print(f"Lv = {Lv:1.4f}")
print(f"Lp = {Lp:1.4f}")
print(f"Lr = {Lr:1.4f}")
print(f"Nv = {Nv:1.4f}")
print(f"Np = {Np:1.4f}")
print(f"Nr = {Nr:1.4f}")

# Do the sadme with the control terms
# 'CMl_da' : 0.0461, 'CMn_da' : 0.0064, 'CY_dr' : 0.175,
#                 'CMl_dr' : 0.007, 'CMn_dr' : -0.109}
Yda = 0
Ydr = q * S / m * CY_dr
Lda = q * S * b / Ixx * CMl_da
Ldr = q * S * b / Ixx * CMl_dr
Nda = q * S * b / Izz * CMn_da
Ndr = q * S * b / Izz * CMn_dr

# Making the starred terms
Imess = Ixx * Izz / (Ixx * Izz - Ixz**2)
I2 = Ixz / Ixx

# Lstarred terms
Lvstar = Imess * (Lv + I2 * Nv)
Lpstar = Imess * (Lp + I2 * Np)
Lrstar = Imess * (Lr + I2 * Nr)
Ldrstar = Imess * (Ldr + I2 * Ndr)
Ldastar = Imess * (Lda + I2 * Nda)

# Nstarred terms
I2 = Ixz / Izz
Nvstar = Imess * (Nv + I2 * Lv)
Npstar = Imess * (Np + I2 * Lp)
Nrstar = Imess * (Nr + I2 * Lr)
Ndrstar = Imess * (Ndr + I2 * Ldr)
Ndastar = Imess * (Nda + I2 * Lda)

Alat = np.matrix(
    [
        [Yv, 0, -U0, g * np.cos(theta_0), 0],
        [Lvstar, Lpstar, Lrstar, 0, 0],
        [Nvstar, Npstar, Nrstar, 0, 0],
        [0, 1, np.tan(theta_0), 0, 0],
        [0, 0, 1 / np.cos(theta_0), 0, 0],
    ]
)

print("The system matrix for lateral-directional motion is ")
display(Math("[A_{lat}] = " + sp.latex(sp.Matrix(Alat).evalf(5))))

print("The eigenvalues are:", np.linalg.eig(Alat)[0])

print("The coefficients of the CE are:", np.poly(Alat))
