import numpy as np
import control
import control.matlab


def longitudinal_matrix(dimensional_derivatives: dict, flight_conditions: dict):
    locals().update(dimensional_derivatives)
    locals().update(flight_conditions)

    Mustar = Mu * Zu
    Mwstar = Mw * Zw
    Mqstar = Mq * Zq
    Mthetastar = g * np.sin(theta_0)
    Mdestar = Mde * Zde

    Alon = np.matrix(
        [
            [Xu, Xw, 0, -g * np.cos(theta_0)],
            [Zu, Zw, U0 + Zq, -g * np.sin(theta_0)],
            [Mustar, Mwstar, Mqstar, Mthetastar],
            [0, 0, 1, 0],
        ]
    )

    return Alon
