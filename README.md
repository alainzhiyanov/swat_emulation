# Starting the emulation #

- Make sure the files start_emulation.sh and cleanup.sh have execution permission
- This code is compatible only with cpppo version 4.3.0. If you have any other version, force install v4.3.0 using the command 'sudo pip install --force-reinstall -v "cpppo==4.3.0"'
- Open Terminal and set the working directory to swat_emulation
- Run 'sudo bash start_emulation.sh' - This will clear all old log files and start the SWaT emulation. This will also create a 'historian' folder where process logs will be saved, and two pcap files that will record the network traffic.
  - Occasionally, you may encounter an error message as follows: "Exception: Please shut down the controller which is running on port 6653"
    In this case, run the command 'sudo fuser -k 6653/tcp', and rerun the start_emulation.sh script.
- Once the start_emulation.sh script starts, hit Enter on the terminal to enter the Mininet terminal (mininet>) and execute the following 3 commands to open three different terminals, one for plc1, one for plcx (contains the logic of plc2 - plc6), and one for s1 (node from where we execute the physical process)
  - xterm plc1
  - xterm plcx
  - xterm s1
- If you want to capture traffic, open two more s1 terminals using 'xterm s1'.
  From one of these terminals run the command 'sudo tshark -i s1-eth1 -w s1-eth1.pcap &' and from the other one run the command 'sudo tshark -i s1-eth2 -w s1-eth2.pcap &'.  
- Start executing the PLC logic and the physical process logic now. Run the following commands in quick succession in the exact same order mentioned below.
  - From s1 terminal, run 'sudo python physical_process.py'
  - From plcx terminal, run 'sudo python plcx.py'
  - From plc1 terminal, run 'sudo python plc1.py'
- Once the experiments are over, close the mininet terminals, and hit Ctrl+D in the main terminal to exit mininet. Typically, it would take around 18 hours for the testbed to complete one operational cycle.  
- At this point, we have the traffic captured in the files s1-eth1.pcap and s1-eth2.pcap, the log files are inside the 'historian' directory, and the temp files are in the 'swat_emulation' directory. For the sake of our experiments, the emulation also generates two additional log files, P1_state.csv and TankLevelReadings.csv.
- To construct a singular historian file from the logs, run the command 'python compile_historian.py -in historian/ -out .'. This will create a file historian.csv in the working directory.
- To clean up the log and temp files, execute the command 'sudo ./cleanup.sh'.
- The pcap files, log files, and historian file can be saved in a separate directory manually for future use. These files should be maintained on an external storage (not Github), as they would typically be very large in size. We have maintained the files at https://drive.google.com/drive/folders/16QZqrv7dX48T-xbKSHisK5XKlwGQAHFm?usp=sharing.


### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)


# Scratch #
vpn experiments
- h1 openvpn --config /home/gargi/Desktop/ICS_Sec/vpn_expt/server.conf &
- h2 openvpn --config /home/gargi/Desktop/ICS_Sec/vpn_expt/client.conf &
- h3 openvpn --config /home/gargi/Desktop/ICS_Sec/vpn_expt/client.conf &
- h4 openvpn --config /home/gargi/Desktop/ICS_Sec/vpn_expt/client.conf &
- h2 ping h1
