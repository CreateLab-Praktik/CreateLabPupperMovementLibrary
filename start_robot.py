import multiprocessing
import time

from PupperAutomation.ActionLoop import ActionLoop
from PupperAutomation.preLoadedQueues import walkTest
from PupperAutomation.run_robot import run_robot as robotLoop




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()

        actionLoop = ActionLoop(transLoop_conn)

        actionLoop.actionQueue = walkTest()

        time.sleep(2)

        robot = multiprocessing.Process(target=robotLoop, args=(robot_conn, True,))
        transmission = multiprocessing.Process(target=actionLoop.transmissionLoopStart, args=())

        
        # running processes
        robot.start()
        ## This sleep timer ensures that the robot is listening before the action transmission starts.
        time.sleep(1)
                
        transmission.start()

        # wait until processes finish
        robot.join()
        transmission.join()

        robot.terminate()
        transmission.terminate()

main()