# This can be directly set in ctrontab as:
# @reboot sleep 60 && sudo rfcomm bind rfcomm0 98:D3:91:FE:97:4E && sleep 10 && python3 /home/pi-ecg1/Arduino-HC05-RPi/Python/clientPump.py
# or can be used as a executable .sh file and call it from crontab
# @reboot sleep 60 && sudo /home/piz-ecg1/GitHub/Arduino-HC05-RPi/AutoBoot/eSeesawBoot.sh

sleep 60 #Waits 60 seconds aferbooting for connecting to the Arduino
sudo rfcomm bind rfcomm0 98:D3:91:FE:97:4E #HC05-module MAC address
sleep 10
sudo python3 /home/pi-ecg1/GitHub/Arduino-HC05-RPi/RaspberryPi/serverPump.py
