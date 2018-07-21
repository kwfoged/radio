#include "Radio_TX.h"

const short NODE_ID = 3; // 0 - 4 = Reading Pipe 1 - 5


byte ackMessg;
RF24 radio_tx(9, 10);

void setup_radio_tx(void) {
  radio_tx.begin();
  radio_tx.setDataRate( RF24_2MBPS );
  radio_tx.setChannel(108);
  radio_tx.enableAckPayload();
}

void loop_radio_tx(uint8_t* slave_telegram) {

    const byte* ptr = &wAddress[NODE_ID * RADIO_ADDR_LEN];
    radio_tx.openWritingPipe(ptr);

    uint8_t analog_data[32];

    for (int i=0; i<32;i++)
      analog_data[i] = slave_telegram[i];

    

 if (radio_tx.write(analog_data, sizeof(analog_data))) 
 {
      if (radio_tx.isAckPayloadAvailable() ) {
        radio_tx.read(&ackMessg, sizeof(ackMessg));
        Serial.print(F("Acknowledge for "));
          Serial.write(*ptr++);

        Serial.print(F(" received: "));
        Serial.println(ackMessg);
      }
    } 
    else {
      Serial.print(F("Send to "));

        Serial.write(*ptr++);

      Serial.println(F(" failed "));
    }
    
    
}

