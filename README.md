# MiniTV
A miniture TV based on the work of [Brandon Withrow](https://withrow.io/simpsons-tv-build-guide)

## Prerequeset Parts
* [Pi Zero](https://www.adafruit.com/product/2885) or [Pi Zero W](https://www.adafruit.com/product/3400)
* [Adafruit Mono 2.5 W Audio Amplifier](https://www.adafruit.com/product/2130)
* [1.5' 4ohm 3W Audio Speaker](https://www.adafruit.com/product/3968)
* SD Card (8GB or higher)
* [Micro USB DIP Breakout Board](https://www.amazon.co.uk/Breakout-Female-Socket-Adapter-Connector/dp/B07R9SMJKF)
* [Micro USB Male Cable](https://www.amazon.co.uk/Micro-Charger-Cable-Braided-Cables/dp/B08XQRV5W1)
* [1K Trim Potentiometer](https://www.amazon.co.uk/HELLOYEE-Breadboard-Trim-Potentiometer-Arduino/dp/B0777J1618)
* [Micro Push Button Switch](https://www.amazon.co.uk/gp/product/B00R1LI06W)
* Composite Screen [Use sudo mod wiki to figure which one you want to get and how to mod them to use 5V](https://www.sudomod.com/wiki/index.php/GBZ_Screen)
* [Toggle Switch](https://www.amazon.co.uk/dp/B07RR7J2K6)
* [Powerboost 500 Basic](https://www.adafruit.com/product/1903)
* [LiPo Battery 2200mAh](https://www.adafruit.com/product/1781)
* [3D Printed Parts](/3Dfiles/)

## Prerequeset Videos encoding
Your videos must be encoded into the H264 format with a height of 480 pixel. this should not be done on the Pi for it would take a long time to get it done. 
A simple way of doing this first installing [FFMPEG](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg) then copying the script [encode.py](/Code/videos/encode.py), collect all your videos in the same folder as the [encode.py](/Code/videos/encode.py) script, and running the python program. The script will loop through all of the video and encode them one by one, & the videos will be placed in a new sub folder called ‘encoded’. If you want to copy your videos via USB you should move the encoded folder into a thumb drive. 

## Getting Pi SD Ready
1. Install the [Raspberry Pi Imager](https://www.raspberrypi.org/software/)
2. Insert SD Card
3. Select you SD Card From "Storage" button
4. From "Operating System" button navigate through "Raspberry Pi OS (Other)" and select "Raspberry Pi OS Lite (Legacy)"
5. A cog wheel now apears in the bottom right click on it and set the hostname to "raspberrypi", enable ssh and set the username as "pi" & the password as "raspberry"<br/><p align="center"><img src="/Extra/AdvancedOptions.png" alt="drawing" width="250"/><p>
6. If you're using a Pi Zero W then enable "Configure Wireless LAN" and add your Wifi's ssid and password.
7. IMPORTANT: Double Check To Make sure you select the SD card. If you accidentally select, an external hard drive that is plugged into your computer, the next step will erase that hard drive. Once checked click on ‘Write’.
8. After the image is written to the SD card remount (Eject and re-insert) it to your computer.
9. Open the mounded device named "boot"
10. Check if there is a file called "wpa_supplicant.conf" if not then make a file with that name and insert the following code (Replacing ssid and password with your wifi SSID and password):
>country=US
>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
>update_config=1
>
>network={
>    ssid="NETWORK NAME"
>    psk="NETWORK PASSWORD"
>}