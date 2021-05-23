from .ActionMessage import *
from queue import Queue
from multiprocessing import connection


class ActionLoop:
    def __init__(self,  PipeConnection: connection.Connection):
        """
            ActionLoop needs one end of a connection pipe tied to a Multiprocessing object.
        """

        self.pipe = PipeConnection

        self.actionQueue = Queue()

        
    def transmissionLoopStart(self):
        """
            When called starts sending one message at a time from the actionQueue to the other end of the Multiprocessing pipe connection.
        """

        while True:

            if self.actionQueue.qsize() != 0:

                currentActionMsg: ActionMessage = self.actionQueue.get()
                ticks = currentActionMsg.ticks
                messageDone = False

                while messageDone == False:

                    self.pipe.send(currentActionMsg.toDictionary())

                    ticks -= 1

                    if ticks <= 0:
                        messageDone = True

            ## TODO test if sending a neutral message still is necessery
            self.pipe.send(ActionMessage().toDictionary())




