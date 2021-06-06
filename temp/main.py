import Adafruit_DHT as AD
import csv
import time
import sys

sensor = AD.DHT22
pin = 4

def record_data(temp, hum, file):
    with open(file, 'a', encoding='utf-8')as f:
        writer = csv.writer(f)
        current_time = str(time.strftime("%Y-%m-%d %H:%M", time.localtime()))
        writer.writerow([current_time, temp, hum])
        
if __name__ == '__main__':
    try:
        file = sys.argv[1]
        flag = True
    except:
        flag = False
    
    # if this script does not run for a long time, it will be inaccurate.
    if not flag:
        _, __ = AD.read_retry(sensor, pin)
    hum, temp = AD.read_retry(sensor, pin)
    if hum is not None and temp is not None:
        hum, temp = float('{:.1f}'.format(hum)), float('{:.1f}'.format(temp))
        print('Temp: {}*C, Hum:{}%'.format(temp, hum))
        if flag:
            record_data(temp=temp, hum=hum, file=file)
    else:
        print('Error!')
