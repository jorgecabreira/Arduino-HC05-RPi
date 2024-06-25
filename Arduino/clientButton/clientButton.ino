// Created on Tue Jun 25 2024 10:23

// @author: J. Cabrera-Moreno
// Postdoctoral Fellow
// Evolutionary Cognition Group
// Institue for Evolutionary Anthropology
// University of Zurich

// Description:
//   The following code pairs the ArtduinoUNO with a RaspberryPi
//   through a HC05 module (Bluetooth Module).
//   The Arduino will act as a client sending information about 
//   the state of a button. That will eventually trigger a pump
//   on the server side.

#include <SoftwareSerial.h>

// Define software serial pins for Bluetooth communication
SoftwareSerial btSerial(10, 11); // RX, TX

// Buffer strings for serial communication
String serialBuffer, btSerialBuffer;

// Define the button pin
const int buttonPin = 9;
int buttonState = 0;

void setup() {
  // Initialize the button pin as an input
  pinMode(buttonPin, INPUT);

  // Initialize the hardware serial communication
  Serial.begin(9600);
  while (!Serial);  // Wait for the serial port to connect
  Serial.println("Start serial communication");

  // Initialize the Bluetooth serial communication
  btSerial.begin(115200);
}

void loop() {
  // Read the state of the button
  buttonState = digitalRead(buttonPin);

  // If the button is pressed
  if (buttonState == HIGH) {
    // Print the button state to the serial monitor
    Serial.println(buttonState);

    // Send a message to the Raspberry Pi via Bluetooth
    btSerial.println("Button pressed\r");
  }
  
  // Small delay to debounce the button and avoid multiple readings
  delay(500);
}
