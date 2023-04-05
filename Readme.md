# Up and Running CyberPi + RaspberryPi
## Configure Raspberry pi

1. Download the [Raspberry Pi Imager](URL "https://www.raspberrypi.org/software/") (i used Etcher first but this one makes the process much easier and faster)

2. Download the [Raspberry Pi OS](URL "https://www.raspberrypi.com/software/operating-systems/") (make sure to download the Raspberry Pi OS (64-bit) Lite ) this is a very important step, since at the time i did this, i only had raspberries B with very little memory, which is the main reason i suspect many installation attempts failed.
3. Connect your SD card to your computer and start te imager.
4. on the imager, select "operating system" ==> "custom" ==> (the image from step 2)
5. select the sd card for storage
6. BEFORE WRITING click on the settings and configure everything (this saves a lot of time)
7. Now you can flash😄
8. Turn the Raspberry pi on, since we used the lite version, it does not come with any sotware or graphics, so don't bother on connecting a monitor or keyboard. Because we already activated the ssh on step 4. we can do everything from our host computer.
9. open a terminal and run:  ssh gary@TMRPI.local   and that's it! 🥳

## Install OpenCV
10. `sudo apt-get update`
11. `sudo apt-get upgrade`
12. `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev`
13. `sudo apt install python3-pip`
14. `pip install --upgrade pip setuptools wheel`
15. `sudo shutdown -r now`
16. `pip install opencv-python-headless`

## Install The Picamera library

`sudo apt-get install python3-picamera`

## Install the cyberpi library

`pip3 install cyberpi`

## Run Program
Clone this repository in the raspberry pi using:

 `git clone https://github.com/gary-vladimir/2023_T003`

 if you don't have git on your raspberry pi you can add it with: `sudo apt-get install git`

 if you already had the Repo make sure it's updated with `git pull origin main`

Make sure you have python 3 installed and run:

`python program.py`
