#include <SoftwareSerial.h>

SoftwareSerial bt_serial(10, 11); // RX, TX
String serialBuff, bt_serialBuff;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Start serial communication");

  bt_serial.begin(115200);
}

void loop() {

  while (bt_serial.available()) {
    bt_serialBuff += String((char)bt_serial.read()); // gets str from Rpi
  }
  if (bt_serialBuff.length() > 0 ) {
    Serial.println("Server response: " + bt_serialBuff);
    //Serial.print("You response -> ");
    bt_serialBuff = "";

    for (int i = 3; i >= 0; --i) {
      Serial.print(i); // Print the countdown number to the serial monitor
      delay(1000); // Wait for 1 second (1000 milliseconds)
      if (i==0){
        Serial.println("Pump Activated");
        bt_serial.println("Pump Activated\r");
      }
    }
  }
}