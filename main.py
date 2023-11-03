#!/usr/bin/env python3
# coding (edited) by Easy Tec
# based on: http://joe703.de/2021/02/28/abstandsmessung-mit-hc-sr04-ultraschallsensorsensor/

import RPi.GPIO as GPIO
import time
from discord_webhook import DiscordWebhook, DiscordEmbed # pip install discordwebhook

# Discord setup
webhook_url = "your webhook url"
picture_url = "your picture url"
username = "your username"

# sleep time after alert
sleep_after_alert = 120 # in seconds

# sensor ports
SENSOR_TRIGGER = 23
SENSOR_ECHO = 24
PIN_output_BUZ = 25

# Define your Distance
def_distance =  150 # in mm

### PLEASE DO NOT ADJUST ###

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(SENSOR_ECHO, GPIO.IN)
GPIO.setup(PIN_output_BUZ, GPIO.OUT)

measuring_max = 1               # in seconds
measuring_trig = 0.00001        # in seconds
measuring_paus = 0.2            # in seconds
measuring_factor = (343460 / 2)
distance_max = 4000        # Max value in mm
distance_max_err = distance_max + 1

def SENSOR_GetDistance():
    GPIO.output(SENSOR_TRIGGER, True)
    time.sleep(measuring_trig)
    GPIO.output(SENSOR_TRIGGER, False)
    #
    starttime = time.time()
    maxtime = starttime + measuring_max
    #
    while starttime < maxtime and GPIO.input(SENSOR_ECHO) == 0:
        starttime = time.time()
    #
    #
    stoptime = starttime
    #
    while stoptime < maxtime and GPIO.input(SENSOR_ECHO) == 1:
        stoptime = time.time()
    #
    if stoptime < maxtime:
        #
        my_time = stoptime - starttime
        #
        distance = my_time * measuring_factor
    else:
        # set fail value
        distance = distance_max_err
    #
    return int(distance)
#
def SendDiscordNotify():
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title='ALARM: Motion detected!', description='We have noticed a movement.', color=16711680) # 16711680 => other spelling: Means (HEX) FF0000
    embed.set_thumbnail(url=picture_url) # your picture
    embed.add_embed_field(name='Whats next?', value='Check your sensor if necessary.', inline=False)
    webhook.username = username

    webhook.add_embed(embed)
    response = webhook.execute()

    # Check Status
    if response.status_code == 200:
        print("send successful.")
    else:
        print(f"send failed. Statuscode: {response.status_code}")
#
# Initialization of the PWM for the buzzer
pwm = GPIO.PWM(PIN_output_BUZ, 1000)  # 1000 Hz
# Howl sequence
def howl_sequence():
    GPIO.output(PIN_output_BUZ, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(PIN_output_BUZ, GPIO.LOW)
    for i in range(1, 6):
        pwm.ChangeFrequency(100 * i)
        pwm.start(50)
        time.sleep(0.2)
        pwm.stop()
        time.sleep(0.1)
#
if __name__ == '__main__':
    GPIO.output(PIN_output_BUZ, GPIO.LOW)
#
    try:
        while True:
            Spacing = SENSOR_GetDistance()

            if Spacing >= distance_max:
                #
                print ("No Object found")
                GPIO.output(PIN_output_BUZ, GPIO.LOW)
            else:
                #
                print ("Measured distance = %i mm" % Spacing)
                if Spacing >= def_distance:
                    howl_sequence()
                    SendDiscordNotify()
                    print("wait {} seconds".format(sleep_after_alert))
                    time.sleep(sleep_after_alert)

            time.sleep(measuring_paus)

    # if detect keyboard interrupt
    except KeyboardInterrupt:
        print("Stopped by user")
        print("Cleanup GPIO...")
        GPIO.cleanup()
