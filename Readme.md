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