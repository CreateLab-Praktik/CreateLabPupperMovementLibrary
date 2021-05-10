from BehaviorLibrary import raw_Activation_Msg, raw_Height_Msg, messageParser,raw_Trot_Msg, RawMessage
import time

from UDPComms import Publisher, Subscriber, timeout


def broadcast():

    ## Configurable ##
    MESSAGE_RATE = 20

    publisher = Publisher(8830)
    subcriber = Subscriber(8840, timeout=0.01)

    ## Message should be objects instead of functions
    
    rawMessageQueue = list()

    rawMessageQueue.append(raw_Activation_Msg())
    rawMessageQueue.append(raw_Height_Msg(2))

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
                publisher.send(messageParser(currentRawMsg))
                print("Msg send", currentRawMsg.name)
                time.sleep(1 / MESSAGE_RATE)
                duration -= 1
                if duration <= 0:
                    flag = 0
        
            
        publisher.send(messageParser(RawMessage()))
        print("Raw MSG send")

        try:
            msg = subcriber.get()
        except timeout:
            pass

        time.sleep(1 / MESSAGE_RATE)



