#!/bin/bash
sudo rm swat_s1_db.sqlite*
sudo rm *.pkl P1_state.csv TankLevelReadings.csv
sudo rm historian/*.pkl
sudo rm *.pcap
# cp log_0.csv.bkp log_0.csv
touch P1-P101-DI_Run.txt
sudo chmod 777 P1-P101-DI_Run.txt

cp log_0.csv.bkp log_0_x.csv
cp log_0.csv.bkp log_0_1.csv
sudo python init.py
# sleep 10
sudo chmod 777 swat_s1_db.sqlite

# create a historian directory
if [[ ! -e ./historian ]]; then
    mkdir ./historian
    sudo chmod -R 777 ./historian
fi

sudo mn -c

touch s1-eth1.pcap s1-eth2.pcap
sudo chmod 777 *.pcap

sudo python run.py

# mate-terminal --tab --title="main-emulation" -e "bash -c 'sudo python run.py &'" &
# mate-terminal --tab --title="packet-capture-1" -e "bash -c 'sudo tshark -i s1-eth1 -w s1-eth1.cap &'" &
# mate-terminal --tab --title="packet-capture-2" -e "bash -c 'sudo tshark -i s1-eth2 -w s1-eth2.cap &'"
