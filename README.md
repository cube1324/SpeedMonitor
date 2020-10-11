# SpeedMonitor

Ever wanted to know how much your ISP fucks you over? Just yeet [speedmonitor.py](https://github.com/cube1324/SpeedMonitor/blob/master/speedmonitor.py) on your pi and put it in a cronjob. Guaranteed Dissapointment.

### Set up:
Install requirements.txt with pip3. Sometimes numpy is broken on Pi, use `sudo apt-get install python3-numpy`

Allow script to be executed `chmod +x speedmonitor.py`

Open cronjobs with `crontab -e`

Add `0 * * * * /path/to/speedmonitor.py` at the end of the file.
This executes a Speedtest every Hour and save the results into data.csv

![Histogramm](https://github.com/cube1324/SpeedMonitor/blob/master/example%20data/data.png)
