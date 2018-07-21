#include <Arduino.h>

class Task
{  
  public:
    Task(unsigned short delta_time);
    bool StartTask(void);
  
    unsigned long   mEntryTime;
    unsigned short mDeltaTime;
  

  };
