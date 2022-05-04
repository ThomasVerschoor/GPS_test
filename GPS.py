import gpsd
import time


class GPS(object):

    def __init__(self, host_ip: str, port: int):
        print("Connecting to GPS....")
        gpsd.connect(host=host_ip, port=port)
        print("Connected to GPS ! ", host_ip, " port: ", port)


    def track(self):
        while True:
            pack = gpsd.get_current()
            print(pack)
            payload: str = str(pack.lat)+","+str(pack.lon)
            print(payload)
            time.sleep(1)