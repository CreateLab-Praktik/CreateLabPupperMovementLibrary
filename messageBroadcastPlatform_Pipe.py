import BehaviorLibrary as BL
import DemoQueues as Demos
import time

from UDPComms import Publisher, Subscriber, timeout


def broadcast(connectionPipe):

    ## Configurable ##
    MESSAGE_RATE = 20

    pipe = connectionPipe
   
    rawMessageQueue = Demos.TrotMode()

        ## Raw message Loop

    while True:
        print("Message loop started")
        print("message count: ", len(rawMessageQueue))

        if len(rawMessageQueue) != 0:
            currentRawMsg = rawMessageQueue.pop()
            ticks = currentRawMsg.ticks
            flag = 1
            while flag == 1:
                pipe.send(BL.messageParser(currentRawMsg))
                print("Msg send", currentRawMsg.name)
                time.sleep(1 / MESSAGE_RATE)
                ticks -= 1
                if ticks <= 0:
                    flag = 0
        
            
        pipe.send(BL.messageParser(BL.RawMessage()))
        print("Raw MSG send")


        time.sleep(1 / MESSAGE_RATE)



