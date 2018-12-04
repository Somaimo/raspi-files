#!/usr/bin/env python3

from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from csv import writer as csvwriter
import requests

sense = SenseHat()

dweetio_thing_name = "mytesting20"

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
        post = requests.post("https://dweet.io/dweet/for/{}?temp={}&pressure={}&humidity={}".format(dweetio_thing_name,int(data[0]), int(data[1]), int(data[2])))
        data_writer.writerow(data)
        print(post.status_code, "Text: ", post.text)
        sleep(5)

