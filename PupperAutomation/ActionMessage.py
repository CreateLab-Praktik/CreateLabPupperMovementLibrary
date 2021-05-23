
class ActionMessage:
    def __init__(self, name = "Neutral MSG"):
        """
            A message template that forms the basis for State altering commands.
                an actionMessage can alter more than one State object atribute 
                e.g. a yaw + y axis message would translate into a right or left turn
                
            !Remember to use actionMessage.parsed before sending through a pipe connection!
        """

        self.name = name
        self.ticks = 0
 
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

        ## currently not used anywhere
        self.hop = 0

    def toDictionary(self, MESSAGE_RATE = 50 ):
        """
            returns this action message as a dictionary that can be converted into a command by a MessageHandler.

        """
        parsedMessage = {

            "name": self.name,
            "ticks": self.ticks,
            
            "y_axis_velocity": -self.y_axis_velocity,
            "x_axis_velocity": self.x_axis_velocity,

            "yaw": self.yaw,
            "pitch": -self.pitch,
            
            "activation": self.activation,
            "trot": self.trot,

            "roll": self.roll_right - self.roll_left,
            "height": self.height_possitive - self.height_negative,

            "hop": self.hop,

            "message_rate": MESSAGE_RATE,
        }

        return parsedMessage