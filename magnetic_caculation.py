import numpy as np
from scipy import special


def Generate_Theta_Phi(num_of_dots: int = 100) -> np.ndarray:
    """Generate the latitude and longitude value of earth and expand to 2-D."""

    latitude = np.linspace(-np.pi/2, np.pi/2, num_of_dots)
    longitude = np.linspace(-np.pi, np.pi, num_of_dots)

    Latitude, Longitude = np.meshgrid(latitude, longitude)
    return Latitude, Longitude


def Caculate_Spherical_Harmonics(Latitude: np.ndarray, Longitude: np.ndarray) -> np.ndarray:
    """Use special functions to caculate the part of Spherical Harmonics."""

    # I only caculate the 1st order of Spherical Harmonics(geocentric magnetic dipole).
    a_1_0_ = special.sph_harm(0, 1, Longitude + np.pi, np.pi/2 - Latitude)
    a_1_0 = a_1_0_.real

    a_1_1_ = special.sph_harm(1, 1, Longitude + np.pi, np.pi/2 - Latitude)
    a_1_1 = a_1_1_.real
    b_1_1 = a_1_1_.imag

    return a_1_0, a_1_1, b_1_1


def Caculate_Magnetic_Potential(g_1_0: float, g_1_1: float, h_1_1: float,
                                a_1_0: np.ndarray, a_1_1: np.ndarray, b_1_1: np.ndarray) -> np.ndarray:
    """Caculate the magnetic potential(use International System of Units)."""

    mu_0 = 4 * np.pi * 1e-7
    R = 6371e3

    # I only caculate the 1st order of magnetic potential(geocentric magnetic dipole).
    w_1 = R / mu_0 * (g_1_0 * a_1_0 + g_1_1 * a_1_1 + h_1_1 * b_1_1)

    return w_1


def Caculate_Magnetic_Moment(g_1_0: float, g_1_1: float, h_1_1: float) -> float:
    """Caculate the magnetic moment(use International System of Units)."""

    mu_0 = 4 * np.pi * 1e-7
    R = 6371e3

    # I only caculate magnetic moment in the 1st order approximation(geocentric magnetic dipole).
    M_x = (4 * np.pi / mu_0) * R ** 3 * g_1_1
    M_y = (4 * np.pi / mu_0) * R ** 3 * h_1_1
    M_z = (4 * np.pi / mu_0) * R ** 3 * g_1_0

    M = (4 * np.pi / mu_0) * R ** 3 * \
        np.sqrt(g_1_1 ** 2 + h_1_1 ** 2 + g_1_0 ** 2)

    return M_x, M_y, M_z, M


def Caculate_Magnetic_X_Y_Z(g_1_0: float, g_1_1: float, h_1_1: float,
                            Latitude: np.ndarray, Longitude: np.ndarray) -> np.ndarray:
    """Caculate the magnetic field(use International System of Units)."""

    # I only caculate magnetic field in the 1st order approximation(geocentric magnetic dipole).
    X = -g_1_0 * np.sin(Latitude) + \
        (g_1_1 * np.cos(Longitude) + h_1_1 * np.sin(Longitude)) * np.cos(Latitude)
    Y = g_1_1 * np.sin(Longitude) - h_1_1 * np.cos(Longitude)
    Z = -2 * (g_1_0 * np.cos(Latitude) +
              (g_1_1 * np.cos(Longitude) + h_1_1 * np.sin(Longitude)) * np.sin(Latitude))

    T = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)

    return X, Y, Z, T


def Caculate_Polar_Angle(g_1_0: float, g_1_1: float, h_1_1: float) -> float:
    """Caculate the polar angle of magnetic field."""

    """I only caculate the polar angle of magnetic field in the 1st order approximation
    (geocentric magnetic dipole)."""
    theta_0 = np.arctan(np.sqrt(g_1_1 ** 2 + h_1_1 ** 2) / np.abs(g_F1_0))
    lambda_0 = np.arctan(h_1_1 / g_1_1)

    return theta_0, lambda_0


def Turn_RAD_to_Degree(Latitude: np.ndarray, Longitude: np.ndarray) -> np.ndarray:
    """When show the map, use degree rather than radian."""

    Latitude_Degree = Latitude * 180.0 / np.pi
    Longitude_Degree = Longitude * 180.0 / np.pi

    return Latitude_Degree, Longitude_Degree
