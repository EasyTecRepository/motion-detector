# motion-detector 
Here you can find a simple script, that **detects motions**, **activates a buzzer**, and sends you a **discord notification**

# What is needed?
- RaspberryPi (I use a RaspPi 3b+, but I think it doesn't matter)
- Breadboard or other solutions (maybe you soldering it yourself)
  - Jumper cable (if needed)
- Buzzer
- resistors (1x 330Ω; 1x 10kΩ)

# Setup
The only thing you must do is edit the few variables in my script.

| Variables                    | Description                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
|webhook_url                   | This is your webhook URL (You can get them in the channel settings on your Discord server)                 |
|picture_url                   | This is your picture URL (No matter, the link must be a file! - You can use my [default URL](#picture_url) |
|username                      | This is your username you want. This is the name of the bot that sends Discord notifications.              |
|sleep_after_alert             | Set sleeptime after successful alert                                                                       |
|SENSOR_TRIGGER                | This is the Pin where you have connected the "trigger"-cable of the sensor                                 |
|SENSOR_ECHO                   | This is the Pin where you have connected the "echo"-cable of the sensor                                    |
|PIN_output_BUZ                | This is the Pin where you have connected the positive (+) buzzer-cable of the buzzer                       |
|def_distance                  | This defines your distance, after the alert triggers                                                       |

# picture_url
This is an extra thing because you have the choice to select my default URL.
```
https://img.icons8.com/ios-glyphs/60/FF0000/motion-detector.png
```
Copyright of this picture: [Motion Detector](https://icons8.com/icon/77544/motion-detector) icon by [Icons8](https://icons8.com)
