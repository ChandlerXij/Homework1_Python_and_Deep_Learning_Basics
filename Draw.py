import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def Draw_Magnetic_Field(Latitude, Longitude, Variable, year: int, name: str) -> None:
    fig = plt.figure()
    m = Basemap()
    m.drawcoastlines()
    plt.contourf(Latitude * 2.0, Longitude, Variable)
    plt.savefig(f'{name} in year {year}.eps', format='eps')
