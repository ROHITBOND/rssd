########################################################################
### Rohde & Schwarz Automation for demonstration use.
###
### Purpose: OSP Switch Matrix Example
### Author:  mclim
### Date:    2018.09.09 
###
### Rack3 Switch Configuration
### ================================================================
### K10:A11-01:A11-P0	K50:A11-55:A11-P10-K1	K70:A11-49:A11-P09-K1
### K11:A11-14:A11-P0	K51:A11-56:A11-P10-K2	K71:A11-67:A11-P12
### K12:A11-26:A11-P0	K52:A11-43:A11-P08-K1	K72:A11-50:A11-P09-K2
### K13:A11-15:A11-P0	K53:A11-44:A11-P08-K2	K73:A11-61:A11-P11
### K14:A11-27:A11-P0	   	   	   			K74:A12-49:A12-P09
### K15:A11-13:A11-P0	   	   	   			K75:A12-37:A12-P07-K1
### K16:A11-25:A11-P0	   	   	   			K76:A12-67:A12-P12
### K17:A11-02:A11-P0	   	   	   			K77:A12-55:A12-P10
### K18:A11-03:A11-P0	   	   	   			K78:A12-61:A12-P11
###
########################################################################
### User Entry
########################################################################
OSP_IP    = '192.168.1.150'                    #IP Address
RF1ThruSA = [[12,67,3],[12,49,1],[11,61,1],[11,67,2],[11,49,1]] #K76(RF1)-K74-K73(Thru)K71-K70
RF1HP5GSA = [[12,67,3],[12,49,1],[11,61,2],[11,67,1],[11,49,1]] #K76(RF1)-K74-K73(HP5G)K71-K70
RF1LNASA  = [[12,67,3],[12,49,1],[11,61,5],[11,67,3],[11,49,1]] #K76(RF1)-K74-K73(LNA)K71-K70
IFHtoSA   = [[11,43,0],[11,56,0],[11,55,1],[11,67,5],[11,49,1]] #K52-K51-K50(Thru)K71-K70
IFHtoSA   = [[11,43,0],[11,56,0],[11,55,0],[11,67,6],[11,49,1]] #K52-K51-K50(HP5G)K71-K70
IFVtoSA   = [[11,44,0],[11,56,1],[11,55,1],[11,67,5],[11,49,1]] #K53-K51-K50(Thru)K71-K70
RF21Noise = [[12,37,0],[12,49,2],[11,61,4]]                     #K75-K74-K73
RF1toRF21 = [[12,67,3],[12,49,1],[11,61,1],[12,37,0]]           #K76(RF1)-K74-K73-75(RF21)
Path = RF1ThruSA

########################################################################
### Code Start
########################################################################
from rssd.OSP_Common import OSP
Rack3 = OSP()
Rack3.jav_openvisa('TCPIP0::192.168.1.150::INSTR')
#Rack3.Set_SW(11,49,0)
for sw in Path:
   Rack3.Set_SW(sw[0],sw[1],sw[2])
Rack3.jav_ClrErr()                          #Clear Errors
