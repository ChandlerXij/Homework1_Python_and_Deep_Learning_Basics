import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def Draw_Magnetic_Field(Latitude, Longitude, Variable, name: str, year: int = 2005) -> None:
    fig = plt.figure()
    m = Basemap()
    m.drawcoastlines()
    plt.contourf(Latitude * 2.0, Longitude, Variable)
    plt.savefig(f'{name} in year {year}.eps', format='eps')
