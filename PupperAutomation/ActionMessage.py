## TODO incorporate this as a dictionary with the number of ticks as a Key:Value Pair.
class ActionMessage:
    def __init__(self, name = "Neutral MSG"):
        """
            A message template that forms the basis for State altering commands.
                !must be parsed before a messageHandler object can convert its data into a Command.

                name is used for debugging

                ticks are the duration or amount of ticks a message should be send   
        """
        self.ticks = 0
        self.name = name
        self.x_axis_velocity = 0
        self.y_axis_velocity = 0
        self.yaw = 0
        self.pitch = 0
        self.activation = 0
        self.trot = 0
        self.roll_right = 0
        self.roll_left = 0
        self.height_possitive = 0
        self.height_negative = 0
        self.hop = 0

    def parsed(self, MESSAGE_RATE = 50 ):
        """
            returns this action message as a dictionary that can be converted into a command by a MessageHandler.

            in this proces the amount of ticks this message will take is lost.
        """

        yaw = self.yaw
        pitch = -self.pitch
        x_axis_velocity = self.x_axis_velocity
        y_axis_velocity = -self.y_axis_velocity

        activation = self.activation
        trot = self.trot
        hop = self.hop

        roll = self.roll_right - self.roll_left
        height = self.height_possitive - self.height_negative

        parsedMessage = {

            "name": self.name,
            "ticks": self.ticks,

            "yaw": yaw,
            "pitch": pitch,

            "y_axis_velocity": y_axis_velocity,
            "x_axis_velocity": x_axis_velocity,
            
            "activation": activation,
            "trot": trot,

            "roll": roll,
            "height": height,

            "hop": hop,

            "message_rate": MESSAGE_RATE,
        }

        return parsedMessage