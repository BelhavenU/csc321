#Donovan Givens 
#This program runs the client for Hello World Server
import zmq

context = zmq.Context()

#  Allows the Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://node00:5555")

#  Do 9 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send_string("Hello")

    #  Get the reply.
    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")