from Draw import Draw_Magnetic_Field

def Draw_MF_of_Earth(Latitude, Longitude, w_1, X, Y, Z, T, year) -> None:
    Draw_Magnetic_Field(Latitude, Longitude, w_1,'The 1st order Magnetic Poential of Earth')
    Draw_Magnetic_Field(Latitude, Longitude, X,'The 1st order Magnetic Field (Eastern) of Earth', year)
    Draw_Magnetic_Field(Latitude, Longitude, Y,'The 1st order Magnetic Field (Northern) of Earth', year)
    Draw_Magnetic_Field(Latitude, Longitude, Z,'The 1st order Magnetic Field (Vertical) of Earth', year)
    Draw_Magnetic_Field(Latitude, Longitude, T,'The 1st order Magnetic Field (Total) of Earth', year)
