import threading



def main():
    pupper = threading.Thread(name="pupper")
    messagePublisher = threading.Thread(name="messagePublisher")
    behavior = threading.Thread(name="behavioer")


main()