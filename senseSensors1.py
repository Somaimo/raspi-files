#!/usr/bin/env python3

from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from csv import writer as csvwriter

sense = SenseHat()

def get_sense_data():
    sense_data = []
    
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())

    sense_data.append(datetime.now())

    return sense_data


with open('data.csv','w', newline='') as f:
    data_writer = csvwriter(f)
    data_writer.writerow(['temp','pres','hum','datetime'])
    
    while True:
        data = get_sense_data()
        data_writer.writerow(data)
        print("recorded the following data:")
        print("----")
        print("Temperature: {}".format(data[0]))
        print("Pressure:    {}".format(data[1]))
        print("Humidity:    {}".format(data[2]))
        print("----")
        sleep(5)

