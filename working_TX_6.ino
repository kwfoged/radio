#include<SPI.h>
#include<nRF24L01.h>
#include<RF24.h>
#include <Task.h>

RF24 radio(9,10);

const byte wAddress[] =  "1Node" "2Node" "3Node" "4Node" "5Node";
const short RADIO_ADDR_LEN = 5;
const short NODE_ID = 3; // Reading Pipe 1 - 5
byte unit_nr = 4;
byte ackMessg[8];
byte msg_no;

struct telegram {
  byte nodeID;
  byte unitNo;
  byte msgNo;
  unsigned short temp1;
  unsigned short temp2;
  
} my_telegram;


Task SendTask(1000);
  
void setup_radio()
{
  radio.begin();
  radio.setDataRate( RF24_250KBPS ); // RF24_2MBPS
  radio.setAutoAck(true);
  radio.enableAckPayload();
  radio.enableDynamicPayloads();
  const byte* ptr = &wAddress[(NODE_ID - 1) * RADIO_ADDR_LEN];
  radio.openWritingPipe(ptr);
  //radio.setRetries(2,4);
  radio.stopListening();
  delay(100);
 }
 
void loop_radio()
{
  if(SendTask.StartTask())
  {

    my_telegram.nodeID = NODE_ID;
    my_telegram.msgNo = msg_no;
    
    if(radio.write(&my_telegram, sizeof(my_telegram)))
    {
      Serial.print( msg_no );
      Serial.print("...tx success");
      msg_no++;
      
      if(radio.isAckPayloadAvailable())
      {
        radio.read(&ackMessg,sizeof(ackMessg));
        Serial.print("  Ack Message : ");
        Serial.print(ackMessg[0]);

      }
      Serial.println("");
     }
     else
     {
      Serial.println("Write failed");
     }
  }
  
  
 }

