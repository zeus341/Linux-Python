from gpiozero import Servo,LED,PWMLED
from time import sleep
import time
# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

warning_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if warning_messages : print("Warning Message are 'ON'")
else : print("Warning Message are 'OFF'")
# Raspberry Pi Pins
r_red_pwm_pin = PWMLED(23)
r_green_pwm_pin = PWMLED(24)
r_blue_pwm_pin = PWMLED(25)

l_red_pwm_pin = PWMLED(17)
l_green_pwm_pin = PWMLED(22)
l_blue_pwm_pin = PWMLED(27)


wave_servo = Servo(26)
max_correction = 0.45
min_correction = 0.15
maxPW = (2.0 + max_correction) / 1000
minPW = (1.0 - min_correction + 0.15) / 1000

# Example of a second servo arm on pin 21
arm = Servo(21, min_pulse_width=minPW, max_pulse_width=maxPW)


red_led = LED(2)
yellow_led = LED(3)
green_led = LED(4)

#print(dir(r_red_pwm_pin))

def stop_light(traffic_status):
    if debug_messages : print("Running stop_light function")
    print("Going down from the top to the bottom")
    stop_light_data = {'red_LED': 1, 'yellow_LED':2, 'green_LED':3}
    red,yellow,green = traffic_status
    print(traffic_status[red])
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    if(traffic_status[red]):
        red_led.on()
    else :
        red_led.off()
    time.sleep(1)
    red_led.off()
    if(traffic_status[yellow]):
        yellow_led.on()
    else :
        yellow_led.off()
    time.sleep(1)
    yellow_led.off()
    if(traffic_status[green]):
        green_led.on()
    else :
        green_led.off()
    time.sleep(1)
    green_led.off()

def eyes_RGB(eyes):
    if debug_messages:
        print("Running eyes_RGB function")
        print(eyes)
    left_eye ={'lefe_red_RGBLED':.44,'leye_green_RGBLED':.5,'reye_blue_RGBLED':.99}
    right_eye = {'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.9}
    left_eye, right_eye= eyes
def reye_RGB(r_brightness, g_brightness, b_brightness):
    if debug_messages:
        print("Running reye_RGB function")
        print(f"R: {r_brightness}, G: {g_brightness}, B:  {b_brightness}")
        
        r_red_pwm_pin.value = r_brightness
        r_green_pwm_pin.value = g_brightness
        r_blue_pwm_pin.value = b_brightness
def leye_RGB(r_brightness, g_brightness, b_brightness):
    if debug_messages:
        print("Runnig reye_RGB function")
        print(f"R: {r_brightness}, G: {g_brightness}, B:  {b_brightness}")
        
        l_red_pwm_pin.value = r_brightness
        l_green_pwm_pin.value = g_brightness
        l_blue_pwm_pin.value = b_brightness

def wave():
   print("Now testing out the servo")
   time.sleep(1)# Running the waving servo continuously
   while True:
        wave_servo.mid()
        print("Mid:", wave_servo.value)
        sleep(0.5)
        
        wave_servo.min()
        print("Min:", wave_servo.value)
        sleep(1)
        
        wave_servo.mid()
        print("Mid:", wave_servo.value)
        sleep(0.5)
        
        wave_servo.max()
        print("Max:", wave_servo.value)
        sleep(1)




        
def get_robot_feature_data():
    if debug_messages : print("Runninng get_robot_feature_data function")
    robot_feature_data ={'stop_light': stop_light_data,
                         'left_eye': left_eye,
                         'right_eye': right_eye,
                         'servo': {
                             'min_pulse_width': minPW,
                             'max_pulse_width': maxPW,
                             'current_value': wave_servo.value
                             } }
    rfd = [stop_light, left_eye, right_eye]
    if debug_messages : print(rfd)
    if debug_messages : print("Returning get_robot_feature_data function")
    return(rfd)
    return(robot_feature_data)

def main():
    print("Welcome To The STEAM Clown Makey Bot")
#     if debug_messages : print("Calling get_robot_feature_data function")
# #    robot_features = get_robot_feature_data()
#     stop_light_LEDs, left_RGB, right_RGB = get_robot_feature_data()
#     if debug_messages : print(stop_light_LEDs)
#     if debug_messages : print(left_RGB)
#     if debug_messages : print(right_RGB)
# 
#     if debug_messages : print("Calling stop_light function")
#     stop_light(stop_light_LEDs)
#     if debug_messages : print("Returned from stop_light function")
# 
#     if debug_messages : print("Calling eyes_RGB function")
#     eyes_RGB([left_RGB,right_RGB])
#     if debug_messages : print("Returned from eyes_RGB function")
#
#     if debug_messafe :print ("calling servo wave function")
while True:
    try:
        print("Welcome to my robot code, you are going to be manually entering the color for the eyes")
        print("Start by inputing the brightness for the left eye")
        r_value = float(input("enter red brightness (0-1)for left eye:"))
        g_value = float(input("enter green brightness (0-1)for left eye:"))
        b_value = float(input("enter blue brightness(0-1)for left eye:"))
            
        if debug_messages:
            print("calaling led_RGB function")
        leye_RGB(r_value, g_value, b_value)
        
        if debug_messages:
            print("returned from left eye RGB function")
    except ValueError:
        print("Please enter a valid number .")
        
    try:
        print("Great Job, now enter the same input but the for the other eye")
        r_value = float(input("enter red brightness (0-1)for right eye:"))
        g_value = float(input("enter green brightness (0-1)for right eye:"))
        b_value = float(input("enter blue brightness(0-1)for right eye:"))

        if debug_messages:
            print("calling right eye RGB function")
        reye_RGB(r_value, g_value, b_value)
        if debug_messages:
            print("returned from right eye RGB function")
    except ValueError:
            print("please enter a valid number")
    traffic_light = {'red_LED' : 1, 'yellow_LED' : 1, 'green_LED' : 1}
    stop_light(traffic_light)
    wave()
    main()

