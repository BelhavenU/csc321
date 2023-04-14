import zmq

context = zmq.Context()

#  connects to the server
print("awaiting hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://node00:5556")

# awaits repsonse 
while True:
    message = input("Type your message here : ")
    socket.send_string(message)

    #  Get the reply.
    response = socket.recv()
    print("Received reply %s " % response)