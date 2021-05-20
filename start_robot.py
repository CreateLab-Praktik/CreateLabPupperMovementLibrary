import multiprocessing
import time

from PupperAutomation.behaviorTransmissionLoop import transmissionLoopStart as transLoop
from PupperAutomation.run_robot import run_robot as robotLoop




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()

        time.sleep(2)

        robot = multiprocessing.Process(target=robotLoop, args=(robot_conn, True,))
        transmission = multiprocessing.Process(target=transLoop, args=(transLoop_conn,False,))

        
        # running processes
        robot.start()
        ## This sleep timer ensures that the robot is listening before the eventQueue is executed.
        time.sleep(1)
                
        transmission.start()

        # wait until processes finish
        robot.join()
        transmission.join()

        robot.terminate()
        transmission.terminate()

main()