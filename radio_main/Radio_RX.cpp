#include "Radio_RX.h"

byte ackData = 1;
byte theMessage[32];
bool addresIsNode;

unsigned long startMillis;  //some global variables available anywhere in the program
unsigned long currentMillis;
const unsigned long period = 2000;  //

RF24 radio(9, 10);

void loadAckData(byte pipe) {
  radio.writeAckPayload(pipe, &ackData, sizeof(ackData));
  ackData++;
}

void changeAddress(void) {
    if(addresIsNode)
    {
    for (byte i = 0; i < 5; i++) 
    {
      radio.openReadingPipe(i + 1, &rAddress[i * 5]);
    }
    }
    else
    {
    for (byte i = 0; i < 5; i++) 
    {
      radio.openReadingPipe(i + 1, &rAddress2[i * 5]);
    }
    }
  radio.startListening();
  addresIsNode = !addresIsNode;
  delay(10);
}

void setup_radio_rx(void) {
  Serial.begin(9600);
  radio.begin();
  radio.setChannel(108);
  radio.setDataRate( RF24_2MBPS );
  radio.enableAckPayload();
  radio.enableDynamicPayloads();
  for (byte i = 0; i < 5; i++) {
    radio.openReadingPipe(i + 1, &rAddress[i * 5]);
  }
  loadAckData(2);
  loadAckData(3);
  loadAckData(4);
  radio.startListening();

}


void loop_radio_rx(uint8_t* received_telegram) {
  
  
//  byte pipeNum = 0;
//  if (radio.available(&pipeNum)) {
//    if (pipeNum == 2 || pipeNum == 3 || pipeNum == 4) {
//      loadAckData(pipeNum);
//    }
//    byte len = radio.getDynamicPayloadSize();
//    radio.read(theMessage, len);
//    Serial.print(F("received ["));
//    Serial.print(len);
//    Serial.print(F("] "));
//    for (int x = 0; x < len; x++) {
//      if (theMessage[x] < 16) {
//        Serial.write('0');
//      }
//      Serial.print(theMessage[x]);
//      Serial.print(" , ");
//    }
//    Serial.print(F(" via "));
//    Serial.print(pipeNum);
//    Serial.print(" addr ");
//    Serial.print(addresIsNode);
//    Serial.print("  ");
//   // Serial.println(((theMessage[1] << 8) + theMessage[2]) / 128.0);
//  }

  byte pipeNum = 0;
  if (radio.available(&pipeNum)) {
    if (pipeNum == 2 || pipeNum == 3 || pipeNum == 4) {
      loadAckData(pipeNum);
    }
    byte len = radio.getDynamicPayloadSize();
    radio.read(theMessage, len);
    Serial.print(F("received ["));
    Serial.print(len);
    Serial.print(F("] "));
    for (int x = 0; x < len; x++) {
      if (theMessage[x] < 16) {
        Serial.write('0');
      }
      Serial.print(theMessage[x]);
      Serial.print(" , ");
    }
    Serial.print(F(" via "));
    Serial.print(pipeNum);
    Serial.print(" addr ");
    Serial.println(addresIsNode);
  }



  currentMillis = millis();  //get the current "time" (actually the number of milliseconds since the program started)
  if (currentMillis - startMillis >= period)  //test whether the period has elapsed
  {
    changeAddress();
    startMillis = currentMillis;  //IMPORTANT to save the start time of the current LED state.
  }
 

  
}


