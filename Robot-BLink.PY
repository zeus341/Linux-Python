# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://raw.githubusercontent.com/jimTheSTEAMClown/RaspberryPi/master/RPi_NeoPixel_Strip.py
# Hacker: Jim Burnham - STEAM Clown, Engineer, Teacher, Maker, Propmaster & Adrenologist  
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name:        RPi_NeoPixel_Strip.py
# Description:    This is a program to drive a set of LEDs (simulating traffic lights) on a Raspberry Pi using gpiozero library.
# Dependencies:   python3
# Inputs: None
# Outputs: Control traffic light LEDs
# Revision: 
#  Revision 0.02 - Updated 03/04/2024 added Raspberry Pi Neopixel libraries and features 
#  Revision 0.01 - Created 03/04/2024
# Additional Comments: 
#==============================================================================
from gpiozero import LED
import time


#Using BCM GPIO3 I/O 
red_led = LED(3) #BCM GPIO3 = BOARD 5

def stop_light(traffic_status):
    print(traffic_status)
    red,yellow,green = traffic_status
    print(traffic_status[red])
    if(traffic_status[red]):
        red_led.on()
    else :
        red_led.off()
#     if(traffic_status[yellow]):
#         yellow_led.on()
#     else :
#         yellow_led.off()


def main():
    print("Welcome To The STEAM Clown Makey Bot")
     while(True):
         print("LED on")
         red_led.on()
         time.sleep(1)
         print("LED off")
         red_led.off()
        time.sleep(1)
    traffic_light = {'red_LED' : 1, 'yellow_LED' : 1, 'green_LED' : 1}
    stop_light(traffic_light)

main()
