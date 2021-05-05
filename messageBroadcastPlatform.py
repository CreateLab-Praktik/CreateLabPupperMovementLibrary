import behaviorOutput as behaviorOutput
import BehaviorLibrary as Behavior

from UDPComms import Publisher, Subscriber, timeout


import time

## Configurable ##
MESSAGE_RATE = 20

publisher = Publisher(8830)
subcriber = Subscriber(8840, timeout=0.01)


while True:
    print("running")

    ## i want to call a function here, and i want it to beable to exchangable. 

    publisher.send(msg)

    try:
        msg = subcriber.get()
    except timeout:
        pass

    time.sleep(1 / MESSAGE_RATE)



