// Generic CAN bench reader demo for public portfolio use.
// This sketch prints fictional frames and does not implement proprietary rules.

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("CAN bench reader demo ready");
}

void loop() {
  Serial.println("FRAME id=18FF0101 data=1122334455667788");
  delay(1000);
}
