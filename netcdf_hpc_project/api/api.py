import threading
import cdsapi

# Data has already been fetched locally and not on the remote host.
# It has then been transferred to the remote host via scp.
# It´s located in the 'repository' folder.
# It is comprised of 10 netcdf files representing a respective year.


class Api:
    def __init__(self):
        self.client = cdsapi.Client()

    def retrieve(self, west, east, south, north, years, months, days, index):
        self.client.retrieve('reanalysis-era5-land',
                             {
                                 'variable': [
                                     '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
                                     'total_precipitation',
                                 ],
                                 'year': years,
                                 'month': months,
                                 'day': days,
                                 'time': [
                                     '00:00', '03:00', '06:00',
                                     '09:00', '12:00', '15:00',
                                     '18:00', '21:00',
                                 ],
                                 'area': [
                                     north, west, south,
                                     east,
                                 ],
                                 'format': 'netcdf',
                             },
                             '../repository/year_'+str(index)+'.nc')


# This is a script for using the api to download netCDF files from Copernicus


api = Api()

north = '67'
east = '-13'
south = '63'
west = '-25'

# years = ['2011', '2012', '2013', '2014', '2015',
#          '2016', '2017', '2018', '2019', '2020']
months = ['06',
          '07', '08']
days = ['01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14',
        '15', '16', '17', '18', '19', '20', '21',
        '22', '23', '24', '25', '26', '27', '28',
        '29', '30', '31']


def get_data(idx):
    base_year = 2011
    api.retrieve(west, east, south, north, str(
        base_year+idx), months, days, idx)


def run_threads():
    """ 
    We use threads so we can await multiple api calls at once 
    The Copernicus API can take over an hour to deliver one request
    so it´s helpful to run the requests in parallel
    """
    threads = []
    for i in range(0, 10):
        threads.append(threading.Thread(target=get_data, args=(i,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Done!")


run_threads()
