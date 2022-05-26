import numpy as np
from data import get_aircraft_data


def TrimState(Vf, gamma = 0):
    '''This function solves for the longitudinal trim of an aircraft using a Newton-Raphson method'''

    # First guess and increments for the jacobian <---- may need to adjust these
    de = 0*np.pi/180
    dde = .01*np.pi/180
    Theta = 2*np.pi/180
    dTheta = dde

    # Gets the value of the functions at the initial guess
    trim = TotalForces(de, Theta, Vf, gamma)

    Trimstate = np.array([[de], [Theta]])

    itercount = 0
    while max(abs(trim)) > 1e-5:  
        itercount = itercount + 1
        # Get value of the function
        trim = TotalForces(de, Theta, Vf, gamma)

        # Get the Jacobian approximation (3 x 3)
        Jde = np.squeeze(TotalForces(de + dde, Theta, Vf, gamma)/dde)
        JTheta = np.squeeze(TotalForces(de, Theta + dTheta, Vf, gamma)/dTheta)
        Jac = np.transpose(np.array([Jde, JTheta]))

        # Get the next iteration
        Trimstate = Trimstate - np.dot(np.linalg.inv(Jac), trim)

        de = Trimstate[0]
        Theta = Trimstate[1]
    
    print(f"Converged after {itercount} iterations")
    print(f'For inputs of Vf = {Vf:1.2f}m/s, gamma = {gamma:1.2f}deg\n')
    print(f'de = {np.degrees(de[0]):1.2f}deg, Theta = {np.degrees(Theta[0]):1.2f}deg\n')

    return Trimstate


def TotalForces(de, Theta, Vf, gamma):
    '''This gives the total forces for the HS 125 simplified longitudinal
    aircraft
    Inputs: Thrust/N, elevator deflection/deg, theta/rad, flightspeed/m/s,
    flightpath/rad
    altitude/m
    '''
    data_list = get_aircraft_data()
    for data_dict in data_list: locals().update(data_dict)

    q = 0  # Trim definition

    # Get the Ue and Ve
    alpha = Theta - gamma
    CL = CL_0 + CL_a*alpha + CL_de*de
    CD = CD_0 + CD_a*alpha + CD_a2*alpha**2
    CM = CMm_0 + CMm_a*alpha + CMm_de * de + CMm_q*q

    q = .5*rho*Vf**2*sref

    # Dimensional lift
    lift = q*CL
    drag = q*CD
    pm = q*cref*CM

    # Determine lift and drag
    F = np.zeros((2, 1))

    F[0] = -lift*np.cos(alpha) -drag*np.sin(alpha) + m*g*np.cos(Theta)
    F[1] = pm
    return F