from multiprocessing import connection
from .behaviorFunctions import *
import time


class MessageInectionInterface:
    def __init__(self, ActionLoopConnection: connection.Connection) -> None:
        self.connection = ActionLoopConnection

    def injectionLoop(self):
        

        print("Sending interruption in 5 seconds")
        time.sleep(5.0)
        self.connection.send(msg_Trot(interrupt = False))
        print("interruption send")
            
        

