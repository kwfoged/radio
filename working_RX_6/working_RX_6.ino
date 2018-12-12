#include<SPI.h>
#include<nRF24L01.h>
#include<RF24.h>

RF24 radio(9,10);

byte ackData[8];
const byte wAddress[] =  "1Node" "2Node" "3Node" "4Node" "5Node";
const short RADIO_ADDR_LEN = 5;


struct telegram {
  byte nodeID;
  byte unitNo;
  byte msgNo;
  unsigned short temp1;
  unsigned short temp2;
  
} ;
telegram my_telegram[6]; 


void loadAckData(byte pipeNum) {
  ackData[0] = my_telegram[pipeNum].msgNo;
  radio.writeAckPayload(pipeNum, &ackData, sizeof(ackData));
}


void setup_radio()
{
  radio.begin();
  radio.setDataRate( RF24_250KBPS ); // RF24_2MBPS
  radio.setAutoAck(true);
  radio.enableAckPayload();
  radio.enableDynamicPayloads();
  for (byte i = 0; i < 5; i++) {
    radio.openReadingPipe(i + 1, &wAddress[i * 5]);
  }
  radio.startListening();
  delay(100);
}

void loop_radio()
{
  byte pipeNum = 0;
  if ( radio.available(&pipeNum) ) 
  {
    if (pipeNum == 1 || pipeNum == 2 || pipeNum == 3) 
      loadAckData(pipeNum);
      
    byte len = radio.getDynamicPayloadSize();
    radio.read(&my_telegram[pipeNum], len);

    Serial.print(" Pipe No: ");
    Serial.print(my_telegram[pipeNum].nodeID);
    Serial.print(" Msg No: ");
    Serial.print(my_telegram[pipeNum].msgNo);
    Serial.print("  Time : ");
    Serial.println(millis());
    
  }
}
