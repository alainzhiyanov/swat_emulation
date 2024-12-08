#  AWS Instances #

## Creating Security Groups #
 - Navigate to EC2 Dashboard on Region 1. 
 - On left side bar, select Security Groups under Network & Security. 
 - Create Security Group 
 - Inbound rules:
   - Type: All traffic
   - Source: Anywhere-IPv4
 - Outbound rules:
   - Type: All traffic
   - Destination: Anywhere IPv4. 
 - Repeat the above on Region 2. 
## Launching Instances

- On Region 1, navigate to Instances. 
- Select Launch Instances.
- launch an EC2 instance with the following configuration:
  - Application and OS Image. Navigate to Quick start. 
    - AMI: Select Ubuntu Server 22.04 LTS (HVM), SSD Volume Type (Confirm warning).
    - Architecture 64-bit (x86)
  - Instance Type: t2.micro
  - Create key pair. 
  - Network Settings:
    - Firewall: Select existing security group and select the group we created above. 
  - Rest of settings can be left as defaults. 
  - Select Launch instance. 
  - Connect to instance. This can be done from Instances, select instance, connect. 
- Repeat the above on Region 2. 
- One instance will be plcx and the other will be plc1. 

For the following instructions, execute on both hosts. 

# Installations #
- `sudo su`
- `apt update`
- `apt install net-tools`
- `apt install docker.io`
- `git clone https://github.com/alainzhiyanov/swat_emulation.git`
- Run `ifconfig` and change IPs, netmask, and MAC in `swat_emulation/utils.py`. 
  - IPs will be the public IPs of the ec2 hosts and netmask and MACs will be under eth0. 
  - Netmask is /20. 

# Docker #
- `git clone https://github.com/alainzhiyanov/ics-sniper-docker.git`
- `cd ics-sniper-docker/docker-for-py2-ics-sniper`
- `docker build -t ics-sniper-py2 -f Dockerfile_py2 .` This will build the docker image. This will take a few minutes. 
- `sudo docker run -it --rm --privileged  --network host  -e DISPLAY     -v /tmp/.X11-unix:/tmp/.X11-unix     -v /lib/modules:/lib/modules     -v /home/ubuntu/swat_emulation:/swat_emulation    ics-sniper-py2` This will run the docker container. 

# Code Change #
- Navigate to minicps package. `cd /usr/local/lib/python2.7/dist-packages/minicps/`
- Edit `protocols.py`. Change line 332 to `ADDRESS = '--address ' + '0.0.0.0' + ' '`

# Opening up New Terminal Windows #
- Open up new terminal windows. Can start by duplicating current terminal tab. 
- On the new terminal:
- `sudo su`
- `docker ps`. Copy container id.
-  `docker exec -it <container_id> /bin/bash`
- If you'd like to capture packets, you'll need to repeat this for a third terminal window and run tshark command there. 

# Running Emulation #
- On all terminal windows, `cd /swat_emulation`. 
- Run `mkdir ./historian`, then `sudo chmod -R 777 ./historian`. 
- `python2 init.py`
- On plcx host: `python2 physical_process_x.py `
- On plc1 host: `python2 physical_process_1.py`
- On plcx host: `python2 plcx.py`
- On plc1 host: `python2 plc1.py`
