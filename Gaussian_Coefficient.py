class GaussianCoefficient:
    """Get the Coefficient of the Gaussian of earth magnetic field."""

    def __init__(self, Table_Content, Target_Year: int = 2005) -> None:
        self.Table = Table_Content
        self.year = Target_Year
        self.years = []
        self.g_1_0 = []
        self.g_1_1 = []
        self.h_1_1 = []
        self.Gaussian = []
        self.index_of_year = 0

    def get_years(self) -> list:
        """Get the years offered by the website."""
        self.years = get_years_or_gaussian(self.Table, 1)
        return self.years

    def get_g_1_0(self) -> list:
        """Get the Gaussian g_1_0 offered by the website."""
        self.g_1_0 = get_years_or_gaussian(self.Table, 2, 0.0, 1.0)
        return self.g_1_0

    def get_g_1_1(self) -> list:
        """Get the Gaussian g_1_1 offered by the website."""
        self.g_1_1 = get_years_or_gaussian(self.Table, 3, 1.0, 1.0)
        return self.g_1_1

    def get_h_1_1(self) -> list:
        """Get the Gaussian h_1_1 offered by the website."""
        self.h_1_1 = get_years_or_gaussian(self.Table, 4, 1.0, 1.0)
        return self.h_1_1

    def get_Gaussian(self):
        """Combine years and Gaussians."""
        import numpy as np
        self.Gaussian = np.array(
            [self.years, self.g_1_0, self.g_1_1, self.h_1_1])
        return self.Gaussian

    def get_index_of_year(self) -> int:
        """Index the targeted year in the list of years."""
        years:list = self.years
        year:int = self.year
        self.index_of_year = years.index(year)
        return self.index_of_year


def is_number(s: str) -> bool:
    """Decide whether the input object is a number. Even it is not integer."""

    """
        The function is from : https://m.py.cn/faq/python/12900.html
        Which is originated from : silencement
        copyright is belong to originator, not me.
    """
    try:  # If run float(s) without error，return True（The strings s is float）
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)  # Turn a string representing number into float
        return True
    except (TypeError, ValueError):
        pass
        return False


def get_years_or_gaussian(tables, decide: int, *removes: float) -> list:
    """Generate the list storing the years or the Coefficient of the Gaussian."""

    y_g_h = []

    ind = tables[decide].contents
    for content in ind:
        if content != '\n' and is_number(content.next):
            # Some '\n' in the table and float like '1995.0' can't be recognized
            y_g_h.append(float(content.next))

    if decide == 2 or decide == 3 or decide == 4:
        for remove in removes:  # Remove the numbers represent the order of Gaussian
            y_g_h.remove(remove)
        y_g_h.pop()  # Remove the SV values, which cannot be caculate the magnetic potential

    return y_g_h
