# RPi_MoCap
This repository contains files relating to the development of a low-cost motion capture using the Raspberry Pi range of computers. <br /> This work is being conducted as part of the Graphics & Interactive Techniques Research Group at **Western Connecticut State University (WCSU)** (https://www.wcsu.edu/cs/computer-science-research/computer-science-grg/). 

## Team Members

- SGRI 2017
	- William Joel (Faculty Advisor)
	- Paul Canada (Project Lead)
	- Christopher Iossa
	- Orquidia Moreno
	- George Ventura
- SGRI 2018 
	- William Joel (Faculty Advisor)
	- Christopher Iossa (Project Lead)
	- Matheus Alexandre
	- Ty Doris
	- Malik Roc
- SGRI 2019 
	- William Joel (Faculty Advisor)
	- Matheus Alexandre (Project Lead)
	- Ty Doris
	- Malik Roc
	
	


## Description
The goal of this project is to design a cost-effective motion capture system using "off the shelf" components and custom designed software. The project currently uses Raspberry Pi 3 computers for development but is targeting Raspberry Pi Zeroes for deployment. The system also uses NoIR cameras for computer vision purposes The software is written in Python and utilizes the [OpenCV computer vision library](https://opencv.org/).

## History

The initial work on the project was done during Summer 2017. At that point in time Git was not used on the project, so no commit history is available from that time. In the span of 6 short weeks a prototype system was built. This system ran the Raspbian Operating System and was capable of accessing the IR camera and controlling the IR lights. The software was able to detect and label IR reflectors (or blobs).

## Issues 

- Low Framerate on the RPi0
- CPU Overheating when light ring is in use for extended period
- Blobs are detected but not tracked
	- The blobs are labeled in raster order
	- Blobs are labeled on a per frame basis. That is, for each frame, the labels are cleared and numbering starts back at 0.
	- The camera does not detect that a blob that has moved from one frame to another is the same blob.
- The camera does not communicate with the host. In fact the host system has not even been developed.
- The camera is currently controlled via keyboard, however, the final system design should not use a keyboard
- Documentation missing
	- Code documentation is minimal and should be expanded.
	- There is no "instruction manual" for the software.
	# WCSU Motion Capture

[TOC]

## 1 Overview

The Raspberry Pi Motion Capture and Tracking System (name to be changed) is an affordable motion capture system that utilizes low-cost hardware with a free, open-source custom software implemented for the general purpose, educational, and hobbyist market.

## 2 Requirements and Dependencies

### 2.1. Hardware
- Raspberry Pi Zero or Zero W
- Sony IMX219 CMOS image sensor (NoIR camera)
- IR Light Ring (LISIPAROI)
- Host Computer

### 2.2 Software
- Raspbian
- Python 3
- OpenCV
- Video4Linux 

### 2.3 Casing
-

### 2.4 Miscellaneous
- IR Reflectors

### 2.5 System Requirements
- 


## 3 Setup and Installation

### 3.1 Environment
- Room must be of *at least* x sqft
- Cameras must be positioned in a way where the only possible white light is emitted/reflected from the markers ONLY.

### 3.2 Raspberry Pi Setup

### 3.3 Camera Installation

### 3.4 Software Installation

## 4 Files
- Marker.py
    - The class that stores data pertaining to each individual marker
- MotionCapture.py
    - Utilizing the openCV library for tracking and displaying, this is the "driver" class where all the work is done for capturing data.
- RunCamera.py
    - Script that enables the cameras to be turned on for capturing.
- enableCameraDriver.sh
    - Bash script that enables the camera driver to be utilized by host computer.

## 5 Key Bindings

|    Key     |                              Action                             | 
|------------|-----------------------------------------------------------------|
|     S      |          Writes a still image from the camera to drive          |
|     F      |               Toggles the display of FPS counter                |
|     M      |           Displays markers in view of the video frame           |
|     E      |              Enable the light-ring for the camera               |
|     D      |             Disable the light-ring for the camera               |
|  Up-Arrow  |          Decrease the threshold of whitelight capture           |
| Down-Arrow |          Increase the threshold of whitelight capture           |
|     Q      |Close down the video frame, stop capturing, and disable lightring|

## 6 Authors
### SGRI 2017
- William Joel (Faculty Advisor)
- [Paul Canada (Project Lead)](https://github.com/PaulCanada)
- [Christopher Iossa]((https://github.com/ChrisIossa))
- Orquidia Moreno
- [George Ventura](https://github.com/GeorgeVentura)
### SGRI 2018 
- William Joel (Faculty Advisor)
- [Christopher Iossa (Project Lead)](https://github.com/ChrisIossa)
- [Matheus Alexandre](https://github.com/madatedeus)
- Ty Doris
- Malik Roc
### SGRI 2019 
- William Joel (Faculty Advisor)
- [Matheus Alexandre(Project Lead)](https://github.com/madatedeus)
- Ty Doris
- Malik Roc



## 7 License
<img src="https://www.gnu.org/graphics/gplv3-127x51.png" alt="GPLv3 Logo" style="float:right;"> This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details
