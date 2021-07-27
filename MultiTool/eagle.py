import os
from colorama import Fore
from colorama.ansi import clear_screen
import sys
import time

("""@G.eKqDGhadkUG#
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?An)R=""")


def Loading():
    print("██ 39%")
    print("███ 49%")
    print("█████ 89%")
    print("██████████████]99%")
    time.sleep(0.2)
    print("Finished. By stoned.eagle#0001 & kojimu#1916")

("""@G.eKqDGhadkUG#
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?An)R=""")



Loading()






time.sleep(0.2)

("""@G.eKqDGhadkUG#
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7bcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
G#XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?A
XniHN7-!):z.hkNdS6DbcVctURB]Xah9MR9-mR6wnd%7/H/Rt2ptpb,uxBDLAQWht&Hz5)V+6(Mt%Fq].+{n2@dNHiAQRm,F6:S4fW9(uymL=&FR6R5JMDi{m/H]G.uA+!2D;Ew?iF:vVT,PSEu)62[hNiMXee3+2S*A]+V[/Uu:]3XM[pd%&bxZB/8_aNjv#H{;cU;qjE=4f3:GrPgy}@.qHAeg3gb_r7t)&!?A{:f(9Lp+$vwEfyRXX:TCa7z=#ChGZYByaE;{vx=-ymGP6ke?An)R=""")

print = True

if print == True:
    print("its true uwu baka")

for x in "banana":
  print(x)

os.system("cls && title Eagle Multi Tool")




def Design():
    print(f''' 
    
    
    
 {Fore.RED}______            _       {Fore.BLUE} __  __       _ _   _  {Fore.RED} _______          _ 
 {Fore.RED}| ____|          | |      {Fore.BLUE}|  \/  |     | | | (_) {Fore.RED}|__   __|        | |
 {Fore.RED} | |__   __ _  __ _| | ___{Fore.BLUE}  | \  / |_   _| | |_ _{Fore.RED}     | | ___   ___ | |
 {Fore.RED} |  __| / _` |/ _` | |/ _ \{Fore.BLUE} | |\/| | | | | | __| |{Fore.RED}    | |/ _ \ / _ \| |
 {Fore.RED}| |___| (_| | (_| | |  __/ {Fore.BLUE}| |  | | |_| | | |_| | {Fore.RED}   | | (_) | (_) | |
 {Fore.RED}|______\__,_|\__, |_|\___| {Fore.BLUE}|_|  |_|\__,_|_|\__|_| {Fore.RED}   |_|\___/ \___/|_|
               __/ |                                                 
               
               {Fore.YELLOW} By Stoned.eagle#0001
               {Fore.WHITE} https://discord.gg/U2XbZx8M


               ''')           






Design()

for x in "banana":
  print(x)



print("")
print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] {Fore.RED} Hacking Tools ')
print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}2{Fore.LIGHTWHITE_EX}] {Fore.RED} Roblox Tools ')
print(f'{Fore.RED}[{Fore.LIGHTCYAN_EX}3{Fore.LIGHTWHITE_EX}] {Fore.RED} Discord Tools ')



{Fore.WHITE}



answer = input("> ")

if answer == "1":
    print("opening")
    time.sleep(0.8)
    exec(open('hack.py').read())
else:
    print("Not an answer lol?")


if answer == "2":
    exec(open('roblox.py').read())
else:
    print("Not an answer lol?")


if answer == "3":
    exec(open('discord.py').read())
else:
    print("Not an answer lol?")








def Design():
    print(f''' 
    
    


    
 {Fore.RED}______            _       {Fore.BLUE} __  __       _ _   _  {Fore.RED} _______          _ 
 {Fore.RED}| ____|          | |      {Fore.BLUE}|  \/  |     | | | (_) {Fore.RED}|__   __|        | |
 {Fore.RED} | |__   __ _  __ _| | ___{Fore.BLUE}  | \  / |_   _| | |_ _{Fore.RED}     | | ___   ___ | |
 {Fore.RED} |  __| / _` |/ _` | |/ _ \{Fore.BLUE} | |\/| | | | | | __| |{Fore.RED}    | |/ _ \ / _ \| |
 {Fore.RED}| |___| (_| | (_| | |  __/ {Fore.BLUE}| |  | | |_| | | |_| | {Fore.RED}   | | (_) | (_) | |
 {Fore.RED}|______\__,_|\__, |_|\___| {Fore.BLUE}|_|  |_|\__,_|_|\__|_| {Fore.RED}   |_|\___/ \___/|_|
               __/ |                                                 
               
               {Fore.YELLOW} By Stoned.eagle#0003 & kojimu#1916
               {Fore.WHITE} https://discord.gg/U2XbZx8M


               ''')           

Design()



os.system



