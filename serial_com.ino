#include <PCM.h> // PCM Library
int ledPin = 12;
int speakerpin = 11;
int data; // Pin connected to the LED

const unsigned char sample[] PROGMEM = {
  
};
void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(ledPin, OUTPUT);
  pinMode(speakerpin,OUTPUT);// Set the LED pin as an output
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    data = Serial.read(); // Read the incoming byte
    if (data == '1') { // If '1' is received
      digitalWrite(ledPin, HIGH); // Turn on the LED
    } else if (data == '0') { // If '0' is received
      digitalWrite(ledPin, LOW); // Turn off the LED
    }
    else if(data == '3'){
      tone(11,5000);
    }
    else if(data == '4'){
      noTone(11);
    }
  }
}
