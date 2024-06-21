#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:32:23 2024

@author: J.Cabrera-Moreno
Postdoctoral Fellow
Evolutionary Cognition Group
Institute of Evolutionary Anthropology
University of Zürich

Description:
    The following code pairs with an Arduino client via Bluetooth
    using a HC-05 module. The Arduino client monitors the state of
    a button that upon press sends a message via Bluetooth to the
    Raspberry Pi which is read by this code. Then when the message
    arrives this code logs the time and the event (ButtonPressed 
    or RewardDelivered).
"""

import time
import serial
import atexit
from gpiozero import OutputDevice
from FileManager import FileManager

# Initialize GPIO for pump control
pinPump = OutputDevice(2)

# Initialize serial communication with Arduino
try:
    ser = serial.Serial(
        port='/dev/rfcomm0',
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    # Ensure the serial port is open    
    if ser.isOpen():
        print("Serial port is open")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)  # Exit the program if serial port cannot be opened

# Initialize file manager
directory = '/home/pi-ecg1/Desktop/DATA'  # Replace with pertinent directory
file_manager = FileManager(directory)
file_path = file_manager.create_file()
print(f"File created: {file_path}")


# Function to clean up GPIO
def cleanup():
    pinPump.close()  # Close GPIO pin

# Register cleanup function with atexit
atexit.register(cleanup)


# Main loop to handle Arduino communication
try:
    while True :
        if ser.inWaiting() > 0:
            recv = ser.readline()
    
            if recv != '':
                print("Arduino Status >> " + str(recv, 'utf-8'))
                
                # Get and append current datetime to the file
                formattedDateTime = file_manager.get_current_datetime(False)
                file_manager.log_to_file(file_path,f"{formattedDateTime},ButtonPressed")
                
                # Activate pump
                pinPump.on()
                time.sleep(2)
                pinPump.off()
                response = "Pump activated\r"
                
                # Get and append current datetime to the file
                formattedDateTime = file_manager.get_current_datetime(False)
                file_manager.log_to_file(file_path,f"{formattedDateTime},RewardReleased")
                
                # Send reply to Arduino with successful pump activation
                ser.write(response.encode())
                print("Response sent: Pump activated")


except KeyboardInterrupt:
    print("Program terminated by user")
except Exception as e:
    print(f"Exception ocurred: {e}")
finally:
    # Cleanup: Close serial port
    if ser.isOpen():
        ser.close()
        print("Serial port closed")
