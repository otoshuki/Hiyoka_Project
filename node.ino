//NodeMCU microcontroller for conrolling relays
//Relays will be directly connected to RPi later

//Import libraries
#include <ESP8266WiFi.h>

//Network credentials
const char* ssid      = "ENTER SSID";
const char* password  = "ENTER PASSWORD";

//Pins
int relay1 = 8;
int relay2 = 7;
int relay3 = 3;
int relay4 = 4;

//Setup function
void setup()
{
  Serial.begin(115200);
  //Connect to WiFi
  Serial.print("Connecting to : ");
  Serial.println(ssid);
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  //Printing local IP
  Serial.print("\n");
  Serial.println("WiFi connected");
  Serial.print("IP address : ");
  Serial.println(WiFi.localIP());
  //Set pins
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  //Shut down pins
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  digitalWrite(relay3, HIGH);
  digitalWrite(relay4, HIGH);
}

//Loop function
void loop()
{
  //Get input
  if (Serial.available())
  {
    input = atoi(Serial.readStringUntil(','));
    Serial.println(input);
  }
  //Turn on devices
  if input == 1
  {
    Serial.println("Relay1 : Lights1 ON");
    digitalWrite(relay1, LOW);
  }
  else if input == 2
  {
    Serial.println("Relay2 ON");
    digitalWrite(relay2, LOW);
  }
  else if input == 3
  {
    Serial.println("Relay3 ON");
    digitalWrite(relay3, LOW);
  }
  else if input == 4
  {
    Serial.println("Relay4 ON");
    digitalWrite(relay4, LOW);
  }
  //Turn off devices
  if input == 5
  {
    Serial.println("Relay1 : Lights1 OFF");
    digitalWrite(relay1, HIGH);
  }
  else if input == 6
  {
    Serial.println("Relay2 OFF");
    digitalWrite(relay2, HIGH);
  }
  else if input == 7
  {
    Serial.println("Relay3 OFF");
    digitalWrite(relay3, HIGH);
  }
  else if input == 8
  {
    Serial.println("Relay4 OFF");
    digitalWrite(relay4, HIGH);
  }

  delay(1000);
}
