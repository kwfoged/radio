#include "Temperature3.h"
#include "Radio_TX.h"
#include "Radio_RX.h"
#include <Task.h>
#include "Common.h"

Task SlaveTask(500);
Task MasterTask(200);

void (*ptrSetup)(void);
void (*ptrLoop)(void);

// 1: MASTER_RX
// 2: SLAVE_TX
short radioType = SLAVE_TX;

void setup() {
  // put your setup code here, to run once:

  if (radioType == MASTER_RX)
  {
    ptrSetup = master_rx_setup;
    ptrLoop =  master_rx_loop;
  }
  else if (radioType == SLAVE_TX)
  {
    ptrSetup = slave_tx_setup;
    ptrLoop =  slave_tx_loop;
  }

  ptrSetup();


}

void loop() 
{
  ptrLoop();
}






void master_rx_loop(void)
{
  uint8_t Received_telegram[32];
  
  if(MasterTask.StartTask())
    loop_radio_rx(); 
  
}

void slave_tx_loop(void)
{
  uint8_t Slave_to_master_telegram[32];
  Slave_to_master_telegram[nodeID] = 2;
  
  if(SlaveTask.StartTask())
  {
    //loop_temp();
    update_temp(Slave_to_master_telegram);
    loop_radio_tx(Slave_to_master_telegram); 
  }
      
}


void master_rx_setup(void)
{
  setup_radio_rx(); 
}

void slave_tx_setup(void)
{

    setup_temp();
    setup_radio_tx(); 
}





