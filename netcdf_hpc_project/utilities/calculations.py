import numpy as np


class Calculations:
    """This class containes static calculation methods"""

    @staticmethod
    def calculate_wind_magnitude(u10, w10):
        """
        Helper method. This method is needed because wind data is
        represented as two components, u and v.
        """
        return np.sqrt(np.square(u10)+np.square(w10))

    @staticmethod
    def calculate_wwm(u10, v10):
        """workable wind magnitude"""
        u10[u10 == -32767] = np.nan
        v10[u10 == -32767] = np.nan
        wind_magnitude = Calculations.calculate_wind_magnitude(u10, v10)
        wwm = np.where((wind_magnitude < 5) & (wind_magnitude > 0), 1, 0)
        return wwm

    @staticmethod
    def calculate_wt(t2m):
        """workable temperature"""
        wt = np.where((t2m < 278) & (t2m > 273), 1, 0)
        return wt

    @staticmethod
    def calculate_wp(tp):
        """workable precipitation"""
        wp = np.where((tp < 0.007) & (tp > 0.004), 1, 0)
        return wp

    @staticmethod
    def calculate_summary(wwm_data, wt_data, wp_data):
        """Logical and of the three calculated variables"""
        temp = np.logical_and(wwm_data, wt_data).astype(int)
        res = np.logical_and(temp, wp_data).astype(int)
        return res

    @staticmethod
    def get_year(timecode):
        """Not used in the project. Only written for development"""
        c = 8760
        year = int(1900 + timecode/8760)
        return year

    @staticmethod
    def year_to_months(year_data):
        """Not used in the project. Only written for development"""
        days = year_data.shape[0]
        partitions = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        if(days == 366):  # leap year
            partitions = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        return np.array(np.split(year_data, partitions, axis=0), dtype=object)

    @staticmethod
    def monthly_averages(year):
        """Not used in the project. Only written for development"""
        m_avg = []
        for month in year:
            avg = np.average(month, axis=0)
            m_avg.append(avg)
        return np.array(m_avg)
