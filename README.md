# Arduino-HC05-RPi
Basic connection between arduino UNO/Micro and Raspberry Pi5 through HC-05 module (Bluetooth).

The idea is to have a central computer (server) that will constantly monitor the state of a button
control by an arduino (client), upon a button press the RPi will then trigger a pump. 
The communication is achieved using a HC-05 module connected to the Arduino. The RPi will use its 
embedded Bluetooth module.
