String msg = " ";

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
}

void loop() {

  char inByte = ' ';

  while(Serial.available()) { // only send data back if data has been sent

    char inByte = Serial.read(); // read the incoming data

    Serial.println(inByte);

    if (inByte == ';') {
      Serial.println("if");
      Serial.println(msg);
      msg = "";

    } else {
      Serial.println("else");
      msg += inByte;
      Serial.println(msg);
    }
  }
  delay(100); // delay for 1/10 of a second

}
