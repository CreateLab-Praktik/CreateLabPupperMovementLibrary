from .ActionMessage import *
from queue import Queue


class ActionLoop:
    def __init__(self, TransmissionPipe):

        self.pipe = TransmissionPipe

        self.actionQueue = Queue()

        
    def transmissionLoopStart(self):

        while True:

            if self.actionQueue.qsize() != 0:

                currentActionMsg = self.actionQueue.get()
                ticks = currentActionMsg.ticks
                messageDone = False

                while messageDone == False:

                    self.pipe.send(currentActionMsg.parsed())

                    ticks -= 1

                    if ticks <= 0:
                        messageDone = True

            self.pipe.send(ActionMessage().parsed())




