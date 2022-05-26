import numpy as np
from trim import TrimState
from data import get_aircraft_data

data_list = get_aircraft_data()
for data_dict in data_list: globals().update(data_dict)

def get_A_long():
    S = sref
    c = cref
    U0 = Vinf

    alpha = Theta - gamma
    CL = m*g/(q*S)
    CD = CD_0 + CD_a*alpha

    Xu = -q * S / m / U0 * (2 * CD)
    Xw = q * S / m / U0 * (CL - CD_a)
    Xq = 0
    Zu = -q * S / m / U0 * (2 * CL + M * CL_M)
    Zw = -q * S / m / U0 * (CD + CL_a)
    Zdw = q * S * c / m / 2 / U0**2 * CL_da # This is a NEW term for us, but since it was given as CL_da, must be included
    Zq = -q * S * c / 2 / m / U0 * CL_q
    Mu = q * S * c / Iyy / U0 * M * CMm_M
    Mw = q * S * c / Iyy / U0 * CMm_a
    Mdw = q * S * c**2 / 2 / Iyy / U0**2 * CMm_da
    Mq = q * S * c**2 / 2 / Iyy / U0 * CMm_q
    Mq = q * S * c**2 / 2 / Iyy / U0 * CMm_q
    Zde = -q * S / m * CL_de
    Mde = q * S * c / Iyy * CMm_de

    Mustar = Mu * Zu
    Mwstar = Mw * Zw
    Mqstar = Mq * Zq
    Mthetastar = g * np.sin(theta_0)
    

    Alon = np.matrix(
        [
            [Xu, Xw, 0, -g * np.cos(theta_0)],
            [Zu, Zw, U0 + Zq, -g * np.sin(theta_0)],
            [Mustar, Mwstar, Mqstar, Mthetastar],
            [0, 0, 1, 0],
        ]
    )

    return Alon

def get_B_long():
    Mdestar = Mde * Zde
    Zde = -q * S / m * CL_de

    Blon = np.matrix([[0], [Zde], [Mdestar], [0]])
    Blon = np.radians(Blon)

    return Blon