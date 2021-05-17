import multiprocessing
import time
import sys

import messageBroadcastPlatform_Pipe as MsgCaster
import run_robot_CreateLab as Robot



def main():

   if __name__ == "__main__":

        robot_conn, caster_conn = multiprocessing.Pipe()

        time.sleep(2)

        robot = multiprocessing.Process(target=Robot.run_robot_CreateLab, args=(robot_conn, True,))
        caster = multiprocessing.Process(target=MsgCaster.broadcast, args=(caster_conn,))

        # running processes
        robot.start()
        time.sleep(1)
                
        caster.start()

        # wait until processes finish
        robot.join()
        caster.join()



main()