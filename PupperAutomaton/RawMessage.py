## TODO incorporate this as a dictionary with the number of ticks as a Key:Value Pair.
class RawMessage:
    def __init__(self, name = "Raw MSG"):
        """
            A message template that forms the basis for State altering commands.
                !must be parsed before a messageHandler object can convert its data into a Command.

                name is used for debugging

                ticks are the duration or amount of ticks a message should be send   
        """
        self.ticks = 0
        self.name = name
        self.values = {
            "x_axis_velocity": 0,
            "y_axis_velocity": 0,
            "yaw": 0,
            "pitch": 0,
            "activation": 0,
            "deactivate": 0,
            "trot": 0,
            "roll_right": 0,
            "roll_left": 0,
            "height_possitive": 0,
            "height_negative": 0,
            "hop": 0,
            }

    def parsed(self, MESSAGE_RATE = 50 ):
        """
            returns this raw message as a dictionary that can be converted into a command by a MessageHandler.

            in this proces the amount of ticks this message will take is lost.
        """

        yaw = self.values["yaw"]
        pitch = -self.values["pitch"]
        x_axis_velocity = self.values["x_axis_velocity"]
        y_axis_velocity = -self.values["y_axis_velocity"]

        activation = self.values["activation"]
        deactivate = self.values["deactivate"]
        trot = self.values["trot"]
        hop = self.values["hop"]

        roll = self.values["roll_right"] - self.values["roll_left"]
        height = self.values["height_possitive"] - self.values["height_negative"]

        parsedMessage = {

            "yaw": yaw,
            "pitch": pitch,
            "y_axis_velocity": y_axis_velocity,
            "x_axis_velocity": x_axis_velocity,
            
            "activation": activation,
            "trot": trot,
            "roll": roll,

            "height": height,
            "hop": hop,
            "deactivate": deactivate,
            "message_rate": MESSAGE_RATE,
        }

        return parsedMessage