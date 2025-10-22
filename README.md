\# ISDN3000C_Lab06
# ISDN3000C_Lab06

##  Overview
This repository contains the solutions for **Lab 06** of ISDN3000C.  
The lab consists of two main parts:
1. **PWM LED Control** – fading an LED and controlling brightness with a push button.
2. **Camera with OpenCV** – capturing images, applying Canny edge detection, and integrating with a button + LED indicator.

---

## ️ Hardware Setup
- RDK-X5 development board
- USB camera module
- LED + resistor
- Push button
- Breadboard and jumper wires

### Circuit Diagram / Photo
![Circuit Photo](./circuit.jpg)  
*(Replace with your actual circuit photo)*

---

## Repository Structure

ISDN3000C_Lab06/ │ ├── led_fade.py # PWM LED fading example ├── camera_test.py # Basic camera test ├── camera_edges.py # Camera with Canny edge detection ├── camera_button_led.py # Group assignment: button + LED + camera ├── requirements.txt # Python dependencies ├── .gitignore # Ignore vt├── .gitignore # Ignore virtual environment and cache files └── README.md # Project documentation
---

```bash
git clone https://github.com/haochunzhang9-droid/ISDN3000C_Lab06.git


python3 -m venv lab06_venv
source lab06_venv/bin/activate


pip install -r requirements.txt

python3 led_fade.py

python3 camera_test.py

python3 camera_edges.py

python3 camera_button_led.py


SHEN Yuming：20945165
ZHANG Haochun：21147459

