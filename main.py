from spider import Spider
from Gaussian_Coefficient import *
from magnetic_caculation import *
from ImageDownload_of_Magnetic_Field import Magnetic_ImageDownload

soup = Spider('https://wdc.kugi.kyoto-u.ac.jp/igrf/coef/igrf13coeffs.html')

Table_Content = soup.select('tr')


Gauss = GaussianCoefficient(Table_Content, 1995)

years = Gauss.get_years()
try:
    Gauss.get_index_of_year()
except ValueError:
    print("Input year error!!! Must be a year between 1900 and 2020 \
        which can be exact division by 5!")
    print("Please input another year!")

g_1_0_list = Gauss.get_g_1_0()
g_1_1_list = Gauss.get_g_1_1()
h_1_1_list = Gauss.get_h_1_1()
Gaussian = Gauss.get_Gaussian()
index_of_year = Gauss.get_index_of_year()

g_1_0 = Gaussian[1][index_of_year]
g_1_1 = Gaussian[2][index_of_year]
h_1_1 = Gaussian[3][index_of_year]


Latitude, Longitude = Generate_Theta_Phi(100)

a_1_0, a_1_1, b_1_1 = Caculate_Spherical_Harmonics(Latitude, Longitude)

w_1 = Caculate_Magnetic_Potential(g_1_0, g_1_1, h_1_1, a_1_0, a_1_1, b_1_1)

M_x, M_y, M_z, M = Caculate_Magnetic_Moment(g_1_0, g_1_1, h_1_1)

X, Y, Z, T = Caculate_Magnetic_X_Y_Z(g_1_0, g_1_1, h_1_1, Latitude, Longitude)

theta_0, lambda_0 = Caculate_Polar_Angle(g_1_0, g_1_1, h_1_1)

Magnetic_ImageDownload()


print("Over!")
