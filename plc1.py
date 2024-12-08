"""
swat-s1 plc1.py
"""

###### Existing emulator libraries ################
from minicps.devices import PLC
from utils import PLC1_DATA, STATE, PLC1_PROTOCOL
from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP
import time
###### Existing simulator libraries ################
from IO import *
from logicblock.logicblock import SETD
from logicblock.logicblock import TONR
from controlblock.controlblock import *
from HMI.HMI import *
from datetime import datetime
import pandas as pd
import os.path
import os

PLC1_ADDR = IP['plc1']
PLCX_ADDR = IP['plcx']

class SwatPLC1(PLC):

    def pre_loop(self, sleep=0):
        time.sleep(5)
        print('DEBUG: swat-s1 plc1 enters pre_loop')
        # print
        # time.sleep(sleep)


        self.processctr = 0
        self.logdf = pd.DataFrame()
        logname = './log_'+str(self.processctr)+'_plc1.pkl'
        while not os.path.exists(logname):
            time.sleep(0.0001)

        self.logdf = pd.read_pickle(logname)
        # print self.logdf.head(10)
        # self.logdf = self.logdf.set_index('Tag')
        self.logdf['Value'] = self.logdf['Value'].astype(float)


        self.IO_P1 = P1()
        self.logdf.loc['P1.MV101.DI_ZSO','Value'] = 0
        self.logdf.loc['P1.MV101.DI_ZSC','Value'] = 1
        self.logdf.loc['P1.MV101.DO_Open','Value'] = 0
        self.logdf.loc['P1.MV101.DO_Close','Value'] = 0
        self.logdf.loc['P1.P101.DI_Run','Value'] = 0
        self.logdf.loc['P1.P101.DO_Start','Value'] = 0
        self.logdf.loc['P1.P102.DI_Run','Value'] = 0
        self.logdf.loc['P1.P102.DO_Start','Value'] = 0
        print("IO Module Initialized")

        self.P1 = HMI_phase()
        self.LIT101 = HMI_LIT(1100.0,800.0,500.0,250.0)
        self.logdf.loc['HMI_LIT101_AHH','Value'] = 0
        try:
            self.send(('HMI_LIT101_AHH',1), 0, PLC1_ADDR)
        except:
            pass
        self.logdf.loc['HMI_LIT101_Pv','Value'] = 0
        try:
            self.send(('HMI_LIT101_Pv',1), 0, PLC1_ADDR)
        except:
            pass
        self.MV101  = HMI_mv()
        self.FIT101 = HMI_FIT(3.0,2.6,2.5,0.0)
        self.P101   = HMI_pump()
        self.P102   = HMI_pump()
        self.P_RAW_WATER_DUTY = HMI_duty2()
        # print("SubProcess1 Components Initialized")

        self.P_RAW_WATER_DUTY_FB = Duty2_FBD()
		# print("P_RAW_WATER_DUTY_FB Initialized")
        self.P101_FB = PMP_FBD(self.P101)
		# print ("P101_FB Initialized")
        self.P102_FB = PMP_FBD(self.P102)
		# print ("P102_FB Initialized")
        self.LIT101_FB = AIN_FBD(self.LIT101)
		# print ("LIT101_FB Initialized")
        self.MV101_FB = MV_FBD(self.MV101)
		# print ("MV101_FB Initialized")
        self.FIT101_FB = FIT_FBD(self.FIT101)
		# print ("FIT101_FB Initialized")
        print ("All Phase 1 Function Blocks Initialized Successfully\n")

        self.TON_FIT102_P1_TM = TONR(10)
        self.TON_FIT102_P2_TM = TONR(10)
        self.Mid_MV101_AutoInp = self.MV101.Status-1
        self.Mid_P_RAW_WATER_DUTY_AutoInp = self.P101.Status-1
		#Initialization
        self.Mid_FIT101_Flow_Hty = 1
        self.Mid_P_RAW_WATER_DUTY_AutoInp = 1
        self.Min_Test = 0

        # time.sleep(1)

    def Pre_Main_Raw_Water(self,IO,datafile,plc1s):
        datafile.write(str(datetime.now().strftime("%m/%d/%Y-%H:%M:%S.%f"))+','+str(self.P1.State)+'\n')
        # Updating LIT101.Pv variable value
        self.LIT101.Pv = float(plc1s.logdf.loc['HMI_LIT101_Pv','Value'])
        try:
            self.send(('HMI_LIT101_Pv',1), self.LIT101.Pv, PLC1_ADDR)
        except:
            pass
        self.LIT101.set_alarm()
        plc1s.logdf.loc['HMI_LIT101_AHH','Value'] = self.LIT101.AHH
        try:
            self.send(('HMI_LIT101_AHH',1),self.LIT101.AHH,PLC1_ADDR)
        except:
            pass

        # Updating IO variable VALUES
        self.IO_P1.MV101.DI_ZSO = int(plc1s.logdf.loc['P1.MV101.DI_ZSO','Value'])
        self.IO_P1.MV101.DI_ZSC = int(plc1s.logdf.loc['P1.MV101.DI_ZSC','Value'])
        self.IO_P1.P101.DI_Run = int(plc1s.logdf.loc['P1.P101.DI_Run','Value'])
        self.IO_P1.P102.DI_Run = int(plc1s.logdf.loc['P1.P102.DI_Run','Value'])

        try:
            self.hmi_plant_reset_on = int(self.receive(('HMI_PLANT_RESET_ON',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_PLANT_RESET_ON value")
            pass

        if self.hmi_plant_reset_on:
			self.MV101.Reset = 1
			self.P101.Reset = 1
			self.P102.Reset = 1

        try:
            self.hmi_plant_auto_on = int(self.receive(('HMI_PLANT_AUTO_ON',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_PLANT_AUTO_ON value")
            pass

        if self.hmi_plant_auto_on:
			self.MV101.Auto 	= 1
			self.P101.Auto 	= 1
			self.P102.Auto 	= 1

        try:
            self.hmi_plant_auto_off = int(self.receive(('HMI_PLANT_AUTO_OFF',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_PLANT_AUTO_OFF value")
            pass

        if self.hmi_plant_auto_off:
			self.MV101.Auto = 0
			self.P101.Auto  = 0
			self.P102.Auto  = 0

        self.P1.Permissive_On = self.MV101.Avl and (self.P101.Avl or self.P102.Avl)

        try:
            self.hmi_p2_permissive_on = int(self.receive(('HMI_P2_PERMISSIVE_ON',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_P2_PERMISSIVE_ON value")
            pass
        try:
            self.hmi_p3_permissive_on = int(self.receive(('HMI_P3_PERMISSIVE_ON',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_P3_PERMISSIVE_ON value")
            pass
        try:
            self.hmi_p4_permissive_on = int(self.receive(('HMI_P4_PERMISSIVE_ON',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_P4_PERMISSIVE_ON value")
            pass

        hmi_plant_ready = int(self.P1.Permissive_On and self.hmi_p2_permissive_on and self.hmi_p3_permissive_on and self.hmi_p4_permissive_on)
        try:
            self.send(('HMI_PLANT_READY',2),hmi_plant_ready,PLCX_ADDR)
        except:
            print("Did not receive HMI_PLANT_READY value")
            pass

        self.P101.Permissive[0] = self.LIT101.Hty and not self.LIT101.ALL

        try:
            self.hmi_mv201_status = int(self.receive(('HMI_MV201_STATUS',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_MV201_STATUS value")
            pass
		# self.P101.Permissive[1] = HMI.MV201.Status == 2
        self.P101.Permissive[1] = self.hmi_mv201_status == 2

        self.P101.MSG_Permissive[1] = self.P101.Permissive[0]
        self.P101.MSG_Permissive[2] = self.P101.Permissive[1]
        self.P102.Permissive[0] = self.LIT101.Hty and not self.LIT101.ALL

        try:
            self.hmi_mv201_status = int(self.receive(('HMI_MV201_STATUS',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_MV201_STATUS value")
            pass
		# self.P102.Permissive[1] = (HMI.MV201.Status == 2)
        self.P102.Permissive[1] = (self.hmi_mv201_status == 2)

        self.P102.MSG_Permissive[1] = self.P102.Permissive[0]
        self.P102.MSG_Permissive[2] = self.P102.Permissive[1]
        self.P101.SD[0] = self.LIT101.Hty and self.LIT101.ALL

        try:
            self.hmi_mv201_status = int(self.receive(('HMI_MV201_STATUS',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_MV201_STATUS value")
            pass
		# self.P101.SD[1] = self.P101.Status == 2 and HMI.MV201.Status != 2
        self.P101.SD[1] = self.P101.Status == 2 and self.hmi_mv201_status != 2

        self.P101.SD[2] = self.TON_FIT102_P1_TM.DN
        if self.P101.SD[2]:
           print ("timeout")
        self.P101.MSG_Shutdown[1] = self.P101.Shutdown[0]
        self.P101.MSG_Shutdown[2] = self.P101.Shutdown[1]
        self.P101.MSG_Shutdown[3] = self.P101.Shutdown[2]

        self.P102.SD[0] = self.LIT101.Hty and self.LIT101.ALL

        try:
            self.hmi_mv201_status = int(self.receive(('HMI_MV201_STATUS',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_MV201_STATUS value")
            pass
		# self.P102.SD[1] = self.P102.Status == 2 and HMI.MV201.Status != 2
        self.P102.SD[1] = self.P102.Status == 2 and self.hmi_mv201_status != 2

        self.P102.SD[2] = self.TON_FIT102_P2_TM.DN

        self.P102.MSG_Shutdown[1] = self.P102.Shutdown[0]
        self.P102.MSG_Shutdown[2] = self.P102.Shutdown[1]
        self.P102.MSG_Shutdown[3] = self.P102.Shutdown[2]

        try:
            self.hmi_plant_stop = int(self.receive(('HMI_PLANT_STOP',2),PLCX_ADDR))
        except:
            print("Did not receive HMI_PLANT_STOP value")
            pass
		# if HMI.PLANT.Stop:
        if self.hmi_plant_stop:
			self.P1.Shutdown = 1

        if self.P1.State == 1:
            print("P1 in state 1")
            self.Mid_MV101_AutoInp = 0
            self.Mid_P_RAW_WATER_DUTY_AutoInp = 0
            self.P1.Ready = 0

            try:
                self.hmi_plant_start = int(self.receive(('HMI_PLANT_START',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_PLANT_START value")
                pass
			# if HMI.PLANT.Ready and HMI.PLANT.Start and self.P1.Permissive_On:
            if hmi_plant_ready and self.hmi_plant_start and self.P1.Permissive_On:
               self.P1.State = 2

        elif self.P1.State == 2:
            print("P1 in state 2")
            self.Mid_MV101_AutoInp = SETD(self.LIT101.AL, self.LIT101.AH, self.Mid_MV101_AutoInp)
            # print("Mid_MV101_AutoInp: ", self.Mid_MV101_AutoInp)

			# self.Mid_P_RAW_WATER_DUTY_AutoInp = SETD(HMI.MV201.Status == 2 and HMI.LIT301.AL, HMI.MV201.Status != 2 or HMI.LIT301.AH, self.Mid_P_RAW_WATER_DUTY_AutoInp)
            try:
                self.hmi_mv201_status = int(self.receive(('HMI_MV201_STATUS',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_MV201_STATUS value")
                pass
            try:
                self.hmi_lit301_al = int(self.receive(('HMI_LIT_301_AL',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_LIT_301_AL value")
                pass
            try:
                self.hmi_lit301_ah = int(self.receive(('HMI_LIT_301_AH',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_LIT_301_AH value")
                pass
            self.Mid_P_RAW_WATER_DUTY_AutoInp = SETD(self.hmi_mv201_status == 2 and self.hmi_lit301_al, self.hmi_mv201_status != 2 or self.hmi_lit301_ah, self.Mid_P_RAW_WATER_DUTY_AutoInp)
            # print("Mid_P_RAW_WATER_DUTY_AutoInp: ", self.Mid_P_RAW_WATER_DUTY_AutoInp)
            if self.P1.Shutdown:
                self.P1.State=3
                self.P1.Shutdown=0

        elif self.P1.State == 3:
            print("P1 in state 3")
            self.Mid_MV101_AutoInp = SETD(self.LIT101.AL, self.LIT101.AH, self.Mid_MV101_AutoInp)

            try:
                self.hmi_mv201_status = int(self.receive(('HMI_MV201_STATUS',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_MV201_STATUS value")
                pass
            try:
                self.hmi_lit301_al = int(self.receive(('HMI_LIT_301_AL',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_LIT_301_AL value")
                pass
            try:
                self.hmi_lit301_ah = int(self.receive(('HMI_LIT_301_AH',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_LIT_301_AH value")
                pass
			# self.Mid_P_RAW_WATER_DUTY_AutoInp = SETD(HMI.MV201.Status == 2 and HMI.LIT301.AL, HMI.MV201.Status != 2 or HMI.LIT301.AH, self.Mid_P_RAW_WATER_DUTY_AutoInp)
            self.Mid_P_RAW_WATER_DUTY_AutoInp = SETD(self.hmi_mv201_status == 2 and self.hmi_lit301_al, self.hmi_mv201_status != 2 or self.hmi_lit301_ah, self.Mid_P_RAW_WATER_DUTY_AutoInp)
            # print("Mid_P_RAW_WATER_DUTY_AutoInp: ", self.Mid_P_RAW_WATER_DUTY_AutoInp)
            try:
                self.hmi_lit301_ah = int(self.receive(('HMI_LIT_301_AH',2),PLCX_ADDR))
            except:
                print("Did not receive HMI_LIT_301_AH value")
                pass
            if self.LIT101.AH and self.hmi_lit301_ah:
                self.Mid_MV101_AutoInp=0
                self.Mid_P_RAW_WATER_DUTY_AutoInp=0
                self.P1.State=2

            if self.P1.Shutdown:
                self.P1.State = 1
                self.P1.Shutdown = 0

        self.MV101_FB.MV_FBD(self.Mid_MV101_AutoInp, self.IO_P1.MV101, self.MV101)
        plc1s.logdf.loc['P1.MV101.DO_Open','Value'] = self.IO_P1.MV101.DO_Open
        plc1s.logdf.loc['P1.MV101.DO_Close','Value'] = self.IO_P1.MV101.DO_Close
        self.P_RAW_WATER_DUTY_FB.Duty2_FBD(self.Mid_P_RAW_WATER_DUTY_AutoInp, self.P101, self.P102, self.P_RAW_WATER_DUTY)
        self.P101_FB.PMP_FBD(self.P_RAW_WATER_DUTY_FB.Start_Pmp1, self.IO_P1.P101, self.P101)
        plc1s.logdf.loc['P1.P101.DO_Start','Value'] = self.IO_P1.P101.DO_Start
        self.P102_FB.PMP_FBD(self.P_RAW_WATER_DUTY_FB.Start_Pmp2, self.IO_P1.P102, self.P102)
        plc1s.logdf.loc['P1.P102.DO_Start','Value'] = self.IO_P1.P102.DO_Start


    def main_loop(self):
        """plc1 main loop.

            - reads sensors value
            - drives actuators according to the control strategy
            - updates its enip server
        """

        print 'DEBUG: swat-s1 plc1 enters main_loop.'
        print

        # Pulling values from the DB for initialization purpose - prevents the PLC from crashing in case the network is already under attack when it bootstraps
        # self.hmi_plant_reset_on = int(self.get(('HMI_PLANT_RESET_ON',2)))
        # self.hmi_plant_auto_on = int(self.get(('HMI_PLANT_AUTO_ON',2)))
        # self.hmi_plant_auto_off = int(self.get(('HMI_PLANT_AUTO_OFF',2)))
        # self.hmi_p2_permissive_on = int(self.get(('HMI_P2_PERMISSIVE_ON',2)))
        # self.hmi_p3_permissive_on = int(self.get(('HMI_P3_PERMISSIVE_ON',2)))
        # self.hmi_p4_permissive_on = int(self.get(('HMI_P4_PERMISSIVE_ON',2)))
        # self.hmi_mv201_status = int(self.get(('HMI_MV201_STATUS',2)))
        # self.hmi_plant_stop = int(self.get(('HMI_PLANT_STOP',2)))
        # self.hmi_plant_start = int(self.get(('HMI_PLANT_START',2)))
        # self.hmi_lit301_al = int(self.get(('HMI_LIT_301_AL',2)))
        # self.hmi_lit301_ah = int(self.get(('HMI_LIT_301_AH',2)))
        datafile = open('P1_state.csv','a')
        datafile.write("Time,P1_State\n")

        # Initializing variables to handle network delays and drops
        self.hmi_plant_reset_on = 0
        self.hmi_plant_auto_on = 0
        self.hmi_plant_auto_off = 1
        self.hmi_p2_permissive_on = 0
        self.hmi_p3_permissive_on = 0
        self.hmi_p4_permissive_on = 0
        self.hmi_mv201_status = 0
        self.hmi_plant_stop = 0
        self.hmi_plant_start = 0
        self.hmi_lit301_al = 0
        self.hmi_lit301_ah = 0

        # while(True):
        while(self.processctr<=100):

            print("PLC1 loop starts here")

            if self.processctr > 0:
                self.logdf = pd.DataFrame()
                logname = './log_'+str(self.processctr)+'_plc1.pkl'
                while not os.path.exists(logname):
                    time.sleep(0.0001)

                self.logdf = pd.read_pickle(logname)
                # print self.logdf
                # self.logdf = self.logdf.set_index('Tag')
                self.logdf['Value'] = self.logdf['Value'].astype(float)

            self.Pre_Main_Raw_Water(self.IO_P1,datafile,self)
            newlogname = './log_'+str(self.processctr+1)+'_1.pkl'
            self.logdf.to_pickle(newlogname)
            self.logdf = pd.DataFrame()
            # os.remove('./log_'+str(self.processctr)+'_a.csv')
            self.processctr = self.processctr + 1
            # time.sleep(PLC_PERIOD_SEC)
            # time.sleep(1)

        datafile.close()
        print 'DEBUG swat plc1 shutdown'

if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc1 = SwatPLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)
