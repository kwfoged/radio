#ifndef COMMON_h
#define COMMON_h

#include <Arduino.h>
#include <RF24.h>
#include <SPI.h>

const short RADIO_ADDR_LEN = 5;

enum radio_type { MASTER_RX = 1,
                  SLAVE_TX};


enum SlaveTelegram {
  nodeID,
  temp1_MSB,
  temp1_LSB,
  temp2_MSB,
  temp2_LSB,
  temp3_MSB,
  temp3_LSB,
  light1_MSB,
  light1_LSB,
  light2_MSB,
  light2_LSB,
  light3_MSB,
  light4_LSB,
  CO_2,
  humidity,
  num_of_bytes_telegram  
};

// Global array
//const short SLAVE_TO_MASTER_LEN = 32;
//uint8_t Slave_to_master_telegram[SLAVE_TO_MASTER_LEN];



const byte wAddress[] =  "1Node" "2Node" "3Node" "4Node" "5Node";
const byte wAddress2[] = "1Mode" "2Mode" "3Mode" "4Mode" "5Mode";
const byte rAddress[] =  "1Node" "2Node" "3Node" "4Node" "5Node";
const byte rAddress2[] = "1Mode" "2Mode" "3Mode" "4Mode" "5Mode";

#endif
