4##########################################################
### Rohde & Schwarz Software Test
###
### Purpose: rssd.nrq_common.py software test
### Author:  mclim
### Date:    2018.08.23
##########################################################
### User Entry
##########################################################
host = '192.168.1.40'           #Get local machine name
#host = 'NRQ6-101507.local'            #Get local machine name

##########################################################
### Code Start
##########################################################
from rssd.NRQ_Common import NRQ
import unittest

class TestGeneral(unittest.TestCase):
   def setUp(self):                 #run before each test
      self.NRQ6 = NRQ()
      try:
         self.NRQ6.jav_Open(host)
         self.NRQ6.jav_Reset()
         self.NRQ6.jav_ClrErr()
         self.NRQ6.dLastErr = ""
      except:
         self.assertTrue(1)

   def test_NRQ_Connect(self):
      self.assertEqual(self.NRQ6.Make,"ROHDE&SCHWARZ")

   def test_NRQ_Freq(self):
      SetVal = 1e9
      self.NRQ6.Set_Freq(SetVal)
      GetVal = self.NRQ6.Get_Freq()
      self.assertEqual(SetVal,int(GetVal))

   def test_NRQ_IQ_RecLength(self):
      SetVal = 2468
      self.NRQ6.Set_IQ_RecLength(SetVal)
      GetVal = self.NRQ6.Get_IQ_RecLength()
      self.assertEqual(SetVal,int(GetVal))

   def test_NRQ_IQ_SamplingRate(self):
      SetVal = 12345678
      self.NRQ6.Set_IQ_SamplingRate(SetVal)
      GetVal = self.NRQ6.Get_IQ_SamplingRate()
      self.assertTrue(SetVal<int(GetVal))

   def test_NRQ_Power(self):
      GetVal = self.NRQ6.Get_Power()
      #print(GetVal)
      self.assertTrue(GetVal > -9999)

if __name__ == '__main__':
   #unittest.main()
   suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneral)
   unittest.TextTestRunner(verbosity=4).run(suite)
