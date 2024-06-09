/* Example sketch to control a stepper motor with TB6600 stepper motor driver, 
  AccelStepper library and Arduino: acceleration and deceleration. 
  More info: https://www.makerguides.com */

// Include the AccelStepper library:
#include "AccelStepper.h"

// Define stepper motor connections and motor interface type. 
// Motor interface type must be set to 1 when using a driver:
#define dirPin 2
#define stepPin 5
String inString = "";
int speed = 2500;

// Create a new instance of the AccelStepper class:
AccelStepper stepper = AccelStepper(AccelStepper::DRIVER, stepPin, dirPin);

void setup() {
  Serial.begin(9600);
  stepper.setMaxSpeed(speed);
  stepper.setAcceleration(speed - 100);

  while (!Serial) {}
}

void loop() {
  stepper.run();

  if (stepper.isRunning()) {
    if (Serial.available() > 0) {Serial.read();}
    return;
  }
  
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    inString += (char)inChar;

    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);

      stepper.move(inString.toInt());
      inString="";
    }
  }
}