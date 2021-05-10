import multiprocessing
import time
import sys

from messageBroadcastPlatform import broadcast as MsgCaster
import run_robot_CreateLab as Robot



def main():

    print("hihi")
    
    
    
    if __name__ == '__main__':
        pupper = multiprocessing.Process(name="pupper", target=Robot )
        print("Pupper Process starting...")
        pupper.daemon = True
        pupper.start()
        print("Pupper Proces started...")
        print("Messeging proces starting in 2 seconds...")
        time.sleep(2)
        messagePublisher = multiprocessing.Process(name="messagePublisher", target = MsgCaster)
        messagePublisher.daemon = True
        messagePublisher.start()
        print("Messeging proces started")
        print("Main thread will sleep for 60 seconds, then terminate ")
        time.sleep(60)

        pupper.terminate()
        print("Pupper proces terminated")
        messagePublisher.terminate()
        print("Messegign proces terminated")



main()