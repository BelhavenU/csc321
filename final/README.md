Network Management Final Project Pcap merge and pull apart instructions
By: Donovan Givens


#The following steps shows how to put each of the pcap files: wuserver.pcap, wuclient.pcap, tasksink.pcap, taskvent.pcap, and taskwork.pcap into to a "fulltake" version.(can run in any node in the docker powershell)

1. step one (merging pcap files): in the docker container run "mergecap wuserver.pcap wuclient.pcap tasksink.pcap taskvent.pcap taskwork.pcap -w fulltake.pcap" to merge all of the pcap files into a "fulltake" file.




#The Following steps Show how to take apart the fulltake.pcap file: weather.pcap, and task.pcap (can run in any node in the docker powershell).

1. step one (removing the weather.pcap port 5556): in the docker container in powershell run " tcpdump -n -r fulltake.pcap port 5556 -w weather.pcap" 

2. step two (removing the task.pcap port 5557 or 5558) run " tcpdump -n -r fulltake.pcap port 5557 or 5558 -w task.pcap"