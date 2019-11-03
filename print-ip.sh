#!/bin/bash

while true
do
    #Init variables
    # The ip won't change often. However, including the instruction in the loop
    # will assure us that it will always be up to date
    FULL_IP=$(hostname -I)
    IP=$(hostname -I | cut -f1 -d ' ')
    echo "Host: $FULL_IP"
    
    #Execute the python script to show the IP using the sensehat
    python3 1_text_scroll-accelerometer.py $IP
    
    #Reading the temperature
    temperature=$(/opt/vc/bin/vcgencmd measure_temp)
    echo "the temperature is: $temperature"
    #Execute the python script to show the temperature using the sensehat
    python3 1_text_scroll-accelerometer.py $temperature
    
    #wait 1s and repeat the loop
    sleep 1s
done
