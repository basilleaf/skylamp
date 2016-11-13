String msg = " ";
int myPins[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once

  int i;
  for (i = 0; i < 15; i = i + 1) {
    pinMode(myPins[i], OUTPUT);
  }

}

void loop() {

  char inByte = ' ';

  while(Serial.available()) { // only send data back if data has been sent

    // turn them all off first
    int i;
    for (i = 0; i < 15; i = i + 1) {
      digitalWrite(myPins[i], LOW);
    }

    char inByte = Serial.read(); // read the incoming data

    if (inByte == ';') {
      Serial.println(msg);
      digitalWrite(myPins[msg.toInt()], HIGH);
      msg = "";

    } else {
      msg += inByte;
    }
  }
  delay(100); // delay for 1/10 of a second

}
