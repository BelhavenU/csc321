#Donovan  Givens
#This program runs the server for Hello World Testing
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  allow it to Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    # allow it to Do some 'work'
    time.sleep(1)

    #  Sends replies back to client
    socket.send_string("World")