import speedtest
from pandas import DataFrame, read_csv
from datetime import datetime

time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

st = speedtest.Speedtest()

server = st.get_best_server()['name']

up = int(st.upload())

down = int(st.download())

try:
    old = read_csv('/home/pi/SpeedMonitor/data.csv')
except:
    old = DataFrame([], columns=['DateTime', 'Upload', 'Download', 'Server'])

df = DataFrame([[time, up, down, server]], columns=['DateTime', 'Upload', 'Download', 'Server'])

old = old.append(df, ignore_index=True)

old.to_csv('/home/pi/SpeedMonitor/data.csv', index=None, header=True)
