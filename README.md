# MiniTV
A miniture TV based on the work of (Brandon Withrow)<https://withrow.io/simpsons-tv-build-guide>

## Prerequeset Parts
* (Pi Zero)<https://www.adafruit.com/product/2885> or (Pi Zero W)<https://www.adafruit.com/product/3400>
* (Adafruit Mono 2.5 W Audio Amplifier)<https://www.adafruit.com/product/2130>
* (1.5' 4ohm 3W Audio Speaker)<https://www.adafruit.com/product/3968>
* SD Card (8GB or higher)
* (Micro USB DIP Breakout Board)<https://www.amazon.co.uk/Breakout-Female-Socket-Adapter-Connector/dp/B07R9SMJKF>
* (Micro USB Male Cable)<https://www.amazon.co.uk/Micro-Charger-Cable-Braided-Cables/dp/B08XQRV5W1>
* (1K Trim Potentiometer)<https://www.amazon.co.uk/HELLOYEE-Breadboard-Trim-Potentiometer-Arduino/dp/B0777J1618>
* (Micro Push Button Switch)<https://www.amazon.co.uk/gp/product/B00R1LI06W>
* Composite Screen (Use sudo mod wiki to figure which one you want to get and how to mod them to use 5V)<https://www.sudomod.com/wiki/index.php/GBZ_Screen>
* (Toggle Switch)<https://www.amazon.co.uk/dp/B07RR7J2K6>
* (Powerboost 500 Basic)<https://www.adafruit.com/product/1903>
* (LiPo Battery 2200mAh)<https://www.adafruit.com/product/1781>
* (3D Printed Parts)</3Dparts/>

## Prerequeset Videos encoding
Your videos must be encoded into the H264 format with a height of 480 pixel. this should not be done on the Pi for it would take a long time to get it done. 
A simple way of doing this first installing (FFMPEG)<https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg> then copying the script (encode.py)</Code/encode.py>, collect all your videos in the same folder as the (encode.py)</Code/encode.py> script, and running the python program. The script will loop through all of the video and encode them one by one, & the videos will be placed in a new sub folder called ‘encoded’. If you want to copy your videos via USB you should move the encoded folder into a thumb drive. 

## Getting Pi SD Ready
1. Install the (Raspberry Pi Imager)<https://www.raspberrypi.org/software/>
2. Insert SD Card
3. Select you SD Card From "Storage" button
4. From "Operating System" button navigate through "Raspberry Pi OS (Other)" and select "Raspberry Pi OS Lite (Legacy)"
5. A cog wheel now apears in the bottom right click on it and set 