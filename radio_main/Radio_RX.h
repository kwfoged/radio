#ifndef RADIO_RX_h
#define RADIO_RX_h

#include <Arduino.h>
#include "Common.h"


void loadAckData(byte);
void changeAddress(void);
void setup_radio_rx(void);
void loop_radio_rx(uint8_t*);

#endif
