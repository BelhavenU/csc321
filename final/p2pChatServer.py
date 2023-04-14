#By Donovan Givens 
#This is a P2P Chat Server 

import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    #  Waits on the client request
    message = socket.recv()
    print("Client request: %s" % message)

    # replies back to client
    message1 = input("enter in the message here : ")
    socket.send_string(message1)
    print("")
