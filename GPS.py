import gpsd
import time


class GPS(object):

    def __init__(self, host_ip: str, port: int):
        """
        GPS initializer

        :param host_ip: host ip of the gpsd daemon
        :param port: port of the gpsd daemon
        """
        print("Connecting to GPS....")
        gpsd.connect(host=host_ip, port=port)
        print("Connected to GPS ! ", host_ip, " port: ", port)

    def track(self):
        """
        Gets the gps location
        """
        while True:
            pack = gpsd.get_current()
            print(pack)
            payload: str = str(pack.lat) + "," + str(pack.lon)
            print(payload)
            time.sleep(1)
