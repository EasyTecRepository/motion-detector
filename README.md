# motion-detector 
Here you can find a simple script, that **detects motions**, **activates a buzzer**, and sends you a **discord notification**

# What is needed?
- RaspberryPi (I use a RaspPi 3b+, but I think it doesn't matter)
- Breadboard or other solutions (maybe you soldering it yourself)
  - Jumper cable (if needed)
- Buzzer
- resistors (1x 330Ω; 1x 10kΩ)

# connection diagram
First of all, the hardware must be connected.
If you like, you can also use a different PIN assignment, **but don't forget that you have to adjust it in the script!**
![Connection Diagram](https://github.com/EasyTecRepository/motion-detector/blob/main/pictures/pi_motion_detection_Steckplatine.png)

# Setup
You must edit a few variables in my script.

| Variables                    | Description                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
|webhook_url                   | This is your webhook URL (You can get them in the channel settings on your Discord server)                 |
|picture_url                   | This is your picture URL (No matter, the link must be a file! - You can use my [default URL](#picture_url) |
|username                      | This is the username you want. This is the name of the bot that sends Discord notifications.               |
|sleep_after_alert             | Set sleep time after successful alert                                                                      |
|SENSOR_TRIGGER                | This is the Pin where you have connected the "trigger"-cable of the sensor                                 |
|SENSOR_ECHO                   | This is the Pin where you have connected the "echo"-cable of the sensor                                    |
|PIN_output_BUZ                | This is the Pin where you have connected the positive (+) buzzer-cable of the buzzer                       |
|def_distance                  | This defines your distance, after the alert triggers                                                       |

Furthermore, you must install Python3 and Python3-pip, if not already done.
```
sudo apt-get update && sudo apt-get install python3 python3-pip
```
After that, we need to install the library discord_webhook.
```
pip install discord_webhook
```

Now, we're ready to create this script on the Raspberry Pi.
First, we create a file, no matter in which folder.
The name of your script doesn't matter.
```
nano motion_detection.py
```
Afterward, you paste the [script from this repository](https://github.com/EasyTecRepository/motion-detector/blob/main/main.py) into your editor.
After you have changed all the above-mentioned variables you can save the script with:
- control+O & control+X (macOS)
- STRG+O & STRG+X (Windows)

Finally, you can run the following command:
```
python3 motion_detection.py
```

# automation
If you want the script to start when your Raspberry Pi starts:
I use autostart ([Based on this Tutorial](https://tutorials-raspberrypi.de/raspberry-pi-autostart-programm-skript/)). Here is how it works:
First, we need to create another script.
In my case, the name is motion_detector.
This will be the name of your service.
The name of this script doesn't matter.
```
sudo nano /etc/init.d/motion_detector
```
Here you must paste this:
```
#! /bin/sh
### BEGIN INIT INFO
# Provides: motion detection script
# Short-Description: start motion detection script
### END INIT INFO
 
case "$1" in
    start)
        echo "start motion detection..."
        # start program
        python3 /home/your_user/motion_detection.py
        ;;
    stop)
        echo "kill all Python3-commands"
        # stop all Python3-commands
        killall python3
        ;;
    *)
        echo "Use: /etc/init.d/motion_detector {start|stop}"
        exit 1
        ;;
esac
 
exit 0
```
Here you must edit a few things.
Please be save, that your path of the Python script is correct.
In my example is the path ```/home/your_user/motion_detection.py```.
If you're not sure, what the right path is, go in he folder where your Python script is and type in: ```pwd```
This command outputs the complete path in which you are located. Now you only need to append the name of your script and you have the complete path.
Keep in mind that if you **stop this service**, **all Python3 scripts will be terminated**.

After that, we give the script more rights.
```
sudo chmod 755 /etc/init.d/motion_detector
```
Note that this path must be the same as the one you specified earlier.

Now you can add this service to autostart.
```
sudo update-rc.d motion_detector defaults
```
Here too, use the same name as the service!

If you don't want autostart anymore, run this:
```
sudo update-rc.d -f  motion_detector remove
```
And when you want to start/stop your script manually, you can do this:
```
sudo /etc/init.d/motion_detector start
```
```
sudo /etc/init.d/motion_detector stop
```

# picture_url
This is an extra thing because you have the choice to select my default URL.
```
https://img.icons8.com/ios-glyphs/60/FF0000/motion-detector.png
```
Copyright of this Icon: [Motion Detector](https://icons8.com/icon/77544/motion-detector) icon by [Icons8](https://icons8.com)
