
"""
swat-s1 plc2-plc6
"""
###### Existing emulator libraries ################
from minicps.devices import PLC
from utils import PLCX_DATA, STATE, PLCX_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP
# import time as t

###### Existing simulator libraries ################
from IO import *
from SCADA import H
from HMI.HMI import *
from real_plc import plc2,plc3,plc4,plc5,plc6
import pandas as pd
import os.path
import os
import time

PLC1_ADDR = IP['plc1']
PLCX_ADDR = IP['plcx']

time_interval = 1
maxstep = 60*60*10

class SwatPLCX(PLC):

    def pre_loop(self, sleep=0):
        time.sleep(5)
        print 'DEBUG: swat-s1 PLCX enters pre_loop'
        print
        # t.sleep(sleep)
        self.processctr = 0
        self.logdf = pd.DataFrame()
        logname = './log_'+str(self.processctr)+'_plcx.pkl'
        while not os.path.exists(logname):
            time.sleep(0.0001)

        self.logdf = pd.read_pickle(logname)
        # self.logdf = self.logdf.set_index('Tag')
        self.logdf['Value'] = self.logdf['Value'].astype(float)


        print("Initializing IO modules")
        self.IO_P2 = P2()
        self.logdf.loc['P2.MV201.DI_ZSO','Value'] = 0
        self.logdf.loc['P2.MV201.DI_ZSC','Value'] = 1
        self.logdf.loc['P2.MV201.DO_Open','Value'] = 0
        self.logdf.loc['P2.MV201.DO_Close','Value'] = 0
        self.IO_P3 = P3()
        self.logdf.loc['P3.P301.DI_Run','Value'] = 0
        self.logdf.loc['P3.P301.DO_Start','Value'] = 0
        self.logdf.loc['P3.P302.DI_Run','Value'] = 0
        self.logdf.loc['P3.P302.DO_Start','Value'] = 0
        self.logdf.loc['P3.MV301.DI_ZSO','Value'] = 0
        self.logdf.loc['P3.MV302.DI_ZSO','Value'] = 0
        self.logdf.loc['P3.MV303.DI_ZSO','Value'] = 0
        self.logdf.loc['P3.MV304.DI_ZSO','Value'] = 0
        self.logdf.loc['P3.MV301.DI_ZSC','Value'] = 1
        self.logdf.loc['P3.MV302.DI_ZSC','Value'] = 1
        self.logdf.loc['P3.MV303.DI_ZSC','Value'] = 1
        self.logdf.loc['P3.MV304.DI_ZSC','Value'] = 1
        self.logdf.loc['P3.MV301.DO_Open','Value'] = 0
        self.logdf.loc['P3.MV301.DO_Close','Value'] = 0
        self.logdf.loc['P3.MV302.DO_Open','Value'] = 0
        self.logdf.loc['P3.MV302.DO_Close','Value'] = 0
        self.logdf.loc['P3.MV303.DO_Open','Value'] = 0
        self.logdf.loc['P3.MV303.DO_Close','Value'] = 0
        self.logdf.loc['P3.MV304.DO_Open','Value'] = 0
        self.logdf.loc['P3.MV304.DO_Close','Value'] = 0
        self.IO_P4 = P4()
        self.logdf.loc['P4.P401.DI_Run','Value'] = 0
        self.logdf.loc['P4.P401.DO_Start','Value'] = 0
        self.logdf.loc['P4.P402.DI_Run','Value'] = 0
        self.logdf.loc['P4.P402.DO_Start','Value'] = 0
        self.IO_P5 = P5()
        self.logdf.loc['P5.MV501.DI_ZSO','Value'] = 0
        self.logdf.loc['P5.MV502.DI_ZSO','Value'] = 0
        self.logdf.loc['P5.MV503.DI_ZSO','Value'] = 0
        self.logdf.loc['P5.MV504.DI_ZSO','Value'] = 0
        self.logdf.loc['P5.MV501.DI_ZSC','Value'] = 1
        self.logdf.loc['P5.MV502.DI_ZSC','Value'] = 1
        self.logdf.loc['P5.MV503.DI_ZSC','Value'] = 1
        self.logdf.loc['P5.MV504.DI_ZSC','Value'] = 1
        self.logdf.loc['P5.MV501.DO_Open','Value'] = 0
        self.logdf.loc['P5.MV501.DO_Close','Value'] = 0
        self.logdf.loc['P5.MV502.DO_Open','Value'] = 0
        self.logdf.loc['P5.MV502.DO_Close','Value'] = 0
        self.logdf.loc['P5.MV503.DO_Open','Value'] = 0
        self.logdf.loc['P5.MV503.DO_Close','Value'] = 0
        self.logdf.loc['P5.MV504.DO_Open','Value'] = 0
        self.logdf.loc['P5.MV504.DO_Close','Value'] = 0
        self.logdf.loc['P5.P501.DI_Run','Value'] = 0
        self.logdf.loc['P5.P502.DI_Run','Value'] = 0
        self.logdf.loc['P5.P501_VSD_Out.Start','Value'] = 0
        self.logdf.loc['P5.P501_VSD_Out.Stop','Value'] = 0
        self.logdf.loc['P5.P502_VSD_Out.Start','Value'] = 0
        self.logdf.loc['P5.P502_VSD_Out.Stop','Value'] = 0
        self.IO_P6 = P6()
        self.logdf.loc['P6.P601.DI_Run','Value'] = 0
        self.logdf.loc['P6.P601.DO_Start','Value'] = 0
        self.logdf.loc['P6.P602.DI_Run','Value'] = 0
        self.logdf.loc['P6.P602.DO_Start','Value'] = 0
        print ("Initializing SCADA HMI")
        self.HMI = H(self)
        print ("Initializing PLCs\n")
        self.PLC2 = plc2.plc2(self.HMI)
        self.PLC3 = plc3.plc3(self.HMI)
        self.logdf.loc['HMI_LIT301_Pv','Value'] =  0
        self.send(('HMI_LIT301_Pv',2), 0, PLCX_ADDR)
        self.PLC4 = plc4.plc4(self.HMI)
        self.logdf.loc['HMI_LIT401_Pv','Value'] =  0
        self.send(('HMI_LIT401_Pv',2), 0, PLCX_ADDR)
        self.PLC5 = plc5.plc5(self.HMI)
        self.PLC6 = plc6.plc6(self.HMI)
        print ("Exiting PLCX pre-loop\n")

    def main_loop(self):
        """PLCX main loop.
            - read flow level sensors
            - update interal enip server
        """
        print 'DEBUG: swat-s1 PLCX enters main_loop.'
        print

        t = 0
        # while(True):
        while(self.processctr<=100):

            Sec_P = not bool(t%(1/time_interval))
            Min_P = not bool(t%(60/time_interval))

            if self.processctr > 0:
                self.logdf = pd.DataFrame()
                logname = './log_'+str(self.processctr)+'_plcx.pkl'
                while not os.path.exists(logname):
                    time.sleep(0.0001)

                self.logdf = pd.read_pickle(logname)
                # self.logdf = self.logdf.set_index('Tag')
                self.logdf['Value'] = self.logdf['Value'].astype(float)

            print("PLCs start working now")

            # PLC-2
            print("PLC-2")
            # Updating IO values
            self.IO_P2.MV201.DI_ZSO = int(self.logdf.loc['P2.MV201.DI_ZSO','Value'])
            self.IO_P2.MV201.DI_ZSC = int(self.logdf.loc['P2.MV201.DI_ZSC','Value'])
            self.PLC2.Pre_Main_UF_Feed_Dosing(self.IO_P2,self.HMI,self)

            # PLC-3
            print("PLC-3")
            # Updating IO VALUES
            self.IO_P3.MV301.DI_ZSO = int(self.logdf.loc['P3.MV301.DI_ZSO','Value'])
            self.IO_P3.MV301.DI_ZSC = int(self.logdf.loc['P3.MV301.DI_ZSC','Value'])
            self.IO_P3.MV302.DI_ZSO = int(self.logdf.loc['P3.MV302.DI_ZSO','Value'])
            self.IO_P3.MV302.DI_ZSC = int(self.logdf.loc['P3.MV302.DI_ZSC','Value'])
            self.IO_P3.MV303.DI_ZSO = int(self.logdf.loc['P3.MV303.DI_ZSO','Value'])
            self.IO_P3.MV303.DI_ZSC = int(self.logdf.loc['P3.MV303.DI_ZSC','Value'])
            self.IO_P3.MV304.DI_ZSO = int(self.logdf.loc['P3.MV304.DI_ZSO','Value'])
            self.IO_P3.MV304.DI_ZSC = int(self.logdf.loc['P3.MV304.DI_ZSC','Value'])
            self.IO_P3.P301.DI_Run = int(self.logdf.loc['P3.P301.DI_Run','Value'])
            self.IO_P3.P302.DI_Run = int(self.logdf.loc['P3.P302.DI_Run','Value'])
            self.HMI.LIT301.Pv = float(self.logdf.loc['HMI_LIT301_Pv','Value'])
            self.send(('HMI_LIT301_Pv',2), self.HMI.LIT301.Pv, PLCX_ADDR)
            self.HMI.LIT301.set_alarm()
            self.logdf.loc['HMI_LIT_301_AL','Value'] = self.HMI.LIT301.AL
            self.logdf.loc['HMI_LIT_301_AH','Value'] = self.HMI.LIT301.AH
            self.send(('HMI_LIT_301_AL', 2), self.HMI.LIT301.AL, PLCX_ADDR)
            self.send(('HMI_LIT_301_AH', 2), self.HMI.LIT301.AH, PLCX_ADDR)
            self.PLC3.Pre_Main_UF_Feed(self.IO_P3,self.HMI,Sec_P,Min_P,self)

            # PLC-4
            print("PLC-4")
            # Updating IO VALUES
            self.IO_P4.P401.DI_Run = int(self.logdf.loc['P4.P401.DI_Run','Value'])
            self.IO_P4.P402.DI_Run = int(self.logdf.loc['P4.P402.DI_Run','Value'])
            self.HMI.LIT401.Pv = float(self.logdf.loc['HMI_LIT401_Pv','Value'])
            self.send(('HMI_LIT401_Pv',2), self.HMI.LIT401.Pv, PLCX_ADDR)
            self.HMI.LIT401.set_alarm()
            self.PLC4.Pre_Main_RO_Feed_Dosing(self.IO_P4,self.HMI,self)

            # PLC-5
            print("PLC-5")
            # Updating IO VALUES
            self.IO_P5.MV501.DI_ZSO = int(self.logdf.loc['P5.MV501.DI_ZSO','Value'])
            self.IO_P5.MV501.DI_ZSC = int(self.logdf.loc['P5.MV501.DI_ZSC','Value'])
            self.IO_P5.MV502.DI_ZSO = int(self.logdf.loc['P5.MV502.DI_ZSO','Value'])
            self.IO_P5.MV502.DI_ZSC = int(self.logdf.loc['P5.MV502.DI_ZSC','Value'])
            self.IO_P5.MV503.DI_ZSO = int(self.logdf.loc['P5.MV503.DI_ZSO','Value'])
            self.IO_P5.MV503.DI_ZSC = int(self.logdf.loc['P5.MV503.DI_ZSC','Value'])
            self.IO_P5.MV504.DI_ZSO = int(self.logdf.loc['P5.MV504.DI_ZSO','Value'])
            self.IO_P5.MV504.DI_ZSC = int(self.logdf.loc['P5.MV504.DI_ZSC','Value'])
            self.IO_P5.P501.DI_Run = int(self.logdf.loc['P5.P501.DI_Run','Value'])
            self.IO_P5.P502.DI_Run = int(self.logdf.loc['P5.P502.DI_Run','Value'])
            self.PLC5.Pre_Main_High_Pressure_RO(self.IO_P5,self.HMI,Sec_P,Min_P, self)

            # PLC-6
            print("PLC-6")
            # Updating IO VALUES
            self.IO_P6.P601.DI_Run = int(self.logdf.loc['P6.P601.DI_Run','Value'])
            self.IO_P6.P602.DI_Run = int(self.logdf.loc['P6.P602.DI_Run','Value'])
            self.HMI.LSH601.Alarm = int(self.logdf.loc['HMI_LSH601_Alarm','Value'])
            self.HMI.LSL601.Alarm = int(self.logdf.loc['HMI_LSL601_Alarm','Value'])
            self.PLC6.Pre_Main_Product(self.IO_P6,self.HMI,self)

            # t.sleep(PLC_PERIOD_SEC)
            newlogname = './log_'+str(self.processctr+1)+'_x.pkl'
            self.logdf.to_pickle(newlogname)
            self.logdf = pd.DataFrame()
            # os.remove('./log_'+str(self.processctr)+'_b.pkl')
            self.processctr = self.processctr + 1

            # time.sleep(1)
            t = t + 1

        print 'DEBUG swat PLCX shutdown'


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plcx = SwatPLCX(
        name='plcx',
        state=STATE,
        protocol=PLCX_PROTOCOL,
        memory=PLCX_DATA,
        disk=PLCX_DATA)
