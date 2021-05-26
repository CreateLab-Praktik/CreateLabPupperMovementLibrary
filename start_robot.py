import multiprocessing
import time

from PupperAutomation.ActionLoop import ActionLoop
from PupperAutomation.MessageInjectionInterface import MessageInectionInterface
import PupperAutomation.preLoadedQueues as Demos
from PupperAutomation.run_robot import run_robot as robotLoop




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()
        injection_conn, transLoop_reciever_conn = multiprocessing.Pipe()

        actionLoop = ActionLoop(transLoop_conn, transLoop_reciever_conn)

        injectionInterface = MessageInectionInterface(injection_conn)

        actionLoop.actionQueue = Demos.turningTest()

        time.sleep(2)

        robot = multiprocessing.Process(target=robotLoop, args=(robot_conn, False,))
        transmission = multiprocessing.Process(target=actionLoop.start, args=())
        injecter = multiprocessing.Process(target=injectionInterface.injectionLoop, args=())

        
        # running processes
        robot.start()
        ## This sleep timer ensures that the robot is listening before the action transmission starts.
        time.sleep(1)
                
        transmission.start()
        # injecter.start()

        # wait until processes finish
        robot.join()
        transmission.join()
        injecter.join()

        robot.terminate()
        transmission.terminate()
        injecter.terminate()

main()