from Draw import Draw_Magnetic_Field

def Draw_MF_of_Earth(Latitude, Longitude, w_1, X, Y, Z, T, year) -> None:
    Draw_Magnetic_Field(Latitude, Longitude, w_1, year,'The 1st order Magnetic Poential of Earth')
    Draw_Magnetic_Field(Latitude, Longitude, X, year,'The 1st order Magnetic Field (Eastern) of Earth')
    Draw_Magnetic_Field(Latitude, Longitude, Y, year,'The 1st order Magnetic Field (Northern) of Earth')
    Draw_Magnetic_Field(Latitude, Longitude, Z, year,'The 1st order Magnetic Field (Vertical) of Earth')
    Draw_Magnetic_Field(Latitude, Longitude, T, year,'The 1st order Magnetic Field (Total) of Earth')
