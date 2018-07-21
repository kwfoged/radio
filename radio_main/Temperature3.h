#include <OneWire.h>
#include <DallasTemperature.h>
#include "Common.h"

void setup_temp(void);
void loop_temp(void);

void printAddress(DeviceAddress);
void printTemperature(DeviceAddress);
void printResolution(DeviceAddress);
void printData(DeviceAddress);
void update_temp(uint8_t*);
