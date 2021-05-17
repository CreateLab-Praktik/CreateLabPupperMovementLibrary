import multiprocessing
import time
import sys

import behaviorTransmissionLoop as transLoop
import run_robot_CreateLab as Robot




def main():

   if __name__ == "__main__":

        robot_conn, transLoop_conn = multiprocessing.Pipe()

        time.sleep(2)

        robot = multiprocessing.Process(target=Robot.run_robot_CreateLab, args=(robot_conn, True,))
        transmission = multiprocessing.Process(target=transLoop.start, args=(transLoop_conn,True,))

        # running processes
        robot.start()
        time.sleep(1)
                
        transmission.start()

        # wait until processes finish
        robot.join()
        transmission.join()

        robot.terminate()
        transmission.terminate()

 


main()