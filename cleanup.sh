#!/bin/bash
sudo rm swat_s1_db.sqlite*
sudo rm *.pkl
# sudo rm P1_state.csv TankLevelReadings.csv
sudo rm historian/*.pkl
# sudo rm *.pcap
cp log_0.csv.bkp log_0.csv
