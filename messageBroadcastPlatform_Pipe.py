from BehaviorLibrary import raw_Activation_Msg, raw_Height_Msg, messageParser,raw_Trot_Msg, RawMessage
import time

from UDPComms import Publisher, Subscriber, timeout


def broadcast(connectionPipe):

    ## Configurable ##
    MESSAGE_RATE = 20

    pipe = connectionPipe
   

    ## Message should be objects instead of functions
    
    rawMessageQueue = list()

    rawMessageQueue.append(raw_Activation_Msg())
    rawMessageQueue.append(raw_Height_Msg(20))

    ## reversing list since pop takes the last item.
    rawMessageQueue.reverse()

        ## Raw message Loop

    while True:
        print("Message loop started")
        print("message count: ", len(rawMessageQueue))

        if len(rawMessageQueue) != 0:
            currentRawMsg = rawMessageQueue.pop()
            duration = currentRawMsg.duration
            flag = 1
            while flag == 1:
                pipe.send(messageParser(currentRawMsg))
                print("Msg send", currentRawMsg.name)
                time.sleep(1 / MESSAGE_RATE)
                duration -= 1
                if duration <= 0:
                    flag = 0
        
            
        pipe.send(messageParser(RawMessage()))
        print("Raw MSG send")


        time.sleep(1 / MESSAGE_RATE)



