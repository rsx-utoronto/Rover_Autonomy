#cd /dev/
#sudo apt-get install gpsd gpsd-clients python-gps
#sudo systemctl stop gpsd.socket
#sudo systemctl disable gpsd.socket
#sudo vim /lib/systemd/system/gpsd.socket

#sudo kilall gpsd
#sudo gpsd /dev/ttyACM0 -F /var/run/gpsd.sock

from gps3 import gps3
import time

gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        print('Lat ', data_stream.TPV['lat'], '\tLon ', data_stream.TPV['lon'], '\tAlt ', data_stream.TPV['alt'])
