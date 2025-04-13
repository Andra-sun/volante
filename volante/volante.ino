const int potPin = A0;         // volante
const int aceleradorPin = 2;   // botão do acelerador
const int marchaUpPin = 3;     // subir marcha
const int marchaDownPin = 4;   // descer marcha

void setup() {
  Serial.begin(9600);
  pinMode(aceleradorPin, INPUT_PULLUP);
  pinMode(marchaUpPin, INPUT_PULLUP);
  pinMode(marchaDownPin, INPUT_PULLUP);
}

void loop() {
  int potValue = analogRead(potPin);
  bool acelerando = !digitalRead(aceleradorPin);
  bool marchaUp = !digitalRead(marchaUpPin);
  bool marchaDown = !digitalRead(marchaDownPin);

  Serial.print(potValue);
  Serial.print(",");
  Serial.print(acelerando);
  Serial.print(",");
  Serial.print(marchaUp);
  Serial.print(",");
  Serial.println(marchaDown);

  delay(10);
}
