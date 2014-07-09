#!/bin/bash

clear

URLTAG=$(zenity --entry --title="MoonBeam v1.0" --text="Enter Moonbeam Tag: "); cd ~/Desktop && git clone http://github.com/alectramell/$URLTAG.git
