#include "Task.h"

Task::Task(unsigned short delta_time)
{
  mDeltaTime = delta_time;
  mEntryTime = 0;
}

bool Task::StartTask(void)
{
  if(millis() > mEntryTime + mDeltaTime)
  {
   mEntryTime = millis();
   return true;  
  }
  else
    return false;   
}
  
