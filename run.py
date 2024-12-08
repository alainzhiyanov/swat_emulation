"""
swat-s1 run.py
"""

from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS

from topo import SwatTopo

import sys
import subprocess

class SwatS1CPS(MiniCPS):

    """Main container used to run the simulation."""

    def __init__(self, name, net):

        self.name = name
        self.net = net

        net.start()

        net.pingAll()

        # start devices
        plc1, scada, s1 = self.net.get(
            'plc1', 'plcx', 's1')

        #SPHINX_SWAT_TUTORIAL RUN(
        #plc2.cmd(sys.executable + ' plc2.py &')
        #plc3.cmd(sys.executable + ' plc3.py &')
        #plc1.cmd(sys.executable + ' plc1.py &')
        #s1.cmd(sys.executable + ' physical_process.py &')
        #SPHINX_SWAT_TUTORIAL RUN)


        cmd1 = "sudo tshark -q -i s1-eth1 -w s1-eth1.pcap"
        cmd2 = "sudo tshark -q -i s1-eth2 -w s1-eth2.pcap"
        process1 = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE)
        process2 = subprocess.Popen(cmd2.split(), stdout=subprocess.PIPE)
        # output, error = process.communicate()

        CLI(self.net)

        #self.net.stop()

if __name__ == "__main__":

    topo = SwatTopo()
    net = Mininet(topo=topo)

    swat_s1_cps = SwatS1CPS(
        name='swat_s1',
        net=net)
