# csc321
CSC-321 Networking

# csc321
CSC-321 Networking

Layer 2: Datalink
How many different things are listed in the output of the arp -a command?
2

 import netlayers netlayers.arp_table()
  File "<ipython-input-2-ede670f9d5b1>", line 1
    import netlayers netlayers.arp_table()
                     ^
SyntaxError: invalid syntax

What are the different devices connected to your home network? Can you identify what they are based on this information?
printer, computer, mouse, and router.

Layer 3: Network

 ping google.com                                                                              
Pinging google.com [172.217.12.78] with 32 bytes of data:
Reply from 172.217.12.78: bytes=32 time=34ms TTL=119
Reply from 172.217.12.78: bytes=32 time=23ms TTL=119
Reply from 172.217.12.78: bytes=32 time=18ms TTL=119
Reply from 172.217.12.78: bytes=32 time=29ms TTL=119

Ping statistics for 172.217.12.78:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 18ms, Maximum = 34ms, Average = 26ms
    
 ping localhost

Pinging LAPTOP-334LIKCT [::1] with 32 bytes of data:
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms

Ping statistics for ::1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
 
What are the differences between the two commands?
The minimum, maximum, and average numbers are different from each other.
For the ping google.com command:
Minimim = 15ms, Maximum = 49ms, and Average = 24ms

For the ping localhost command:
Minimum = 0ms, Maximum = 0ms, and Average = 0ms

