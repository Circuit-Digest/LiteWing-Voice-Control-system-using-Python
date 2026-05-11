# 🎙️ LiteWing-Voice-Control-system-using-Python

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An offline voice control interface for the **LiteWing Drone** ecosystem a high-performance **ESP32-based** drone. This module translates natural speech into flight commands and LED states for low-latency, hands-free operation using the Vosk engine.

For a more detailed overview of the project, visit here: [ESP32 Voice Controlled Drone using LiteWing](https://circuitdigest.com/microcontroller-projects/esp32-voice-controlled-drone-using-litewing)

> [!IMPORTANT]
> **Mandatory Hardware Requirements:**
> To use this voice control system, you MUST have the following hardware:
> 1.  **LiteWing Drone**
> 2.  **LiteWing Position Module** (Essential for stable hovering and coordinate-based navigation).

---

## 🚀 Key Features

- **Offline Voice Recognition**: Powered by the Vosk engine for low-latency, private, and reliable control without internet.
- **Microphone Management**: Easy tool to identify and select the correct audio hardware.
- **Flight Safety**: Built-in altitude boundaries, emergency stop commands, and LED status indicators.
- **Multi-Command Support**: Intuitive commands for takeoff, direction, altitude, and lighting.

---

## 🛠️ Installation & Setup

### 1. Firmware Update
Before flying, ensure your drone is updated to the latest firmware to ensure compatibility with the LiteWing library.
🔗 **Download & Guide:** [LiteWing Firmware Update](https://circuitdigest.com/wiki/litewing/)

### 2. Install LiteWing Library
This project requires the official **LiteWing Python Library**. Install it directly from GitHub:
```bash
pip install git+https://github.com/Circuit-Digest/LiteWing-Library.git
```

### 3. Clone and Install Dependencies
```bash
git clone https://github.com/VishnumKer/LiteWing-Voice-Control-system-using-Python
cd LiteWing-Voice-Control-system-using-Python
pip install -r requirements.txt
```

### 4. Vosk Model Setup (Required for Offline Mode)
The system uses the **Vosk** engine for voice recognition. You must download a language model:
1.  Visit the [Vosk Models page](https://alphacephei.com/vosk/models).
2.  Download a small English model (e.g., `vosk-model-small-en-us-0.15`).
3.  Extract the contents into a folder named `model/` in the project root.

> [!IMPORTANT]
> The `model/` folder is excluded via `.gitignore` and should **not** be committed to GitHub due to its size. Users must download their own model as described above.

---

## 🎮 Usage Guide

### 1. Identify Your Microphone
Before flying, find the index of your microphone:
```bash
python list_mics.py
```
Note the **Index number** of your preferred input device.

### 2. Configure the Controller
Open `voice_control.py` and adjust the following constants at the top:
- `DRONE_IP`: Set this to your drone's IP (e.g., `192.168.43.42`).
- `MIC_INDEX`: Set this to the index found in the previous step.
- `MAX_HEIGHT`: Safety ceiling for indoor flight (default: `0.5m`).

### 3. Start the System
```bash
python voice_control.py
```
*Wait for the "Ready" status and the drone LEDs to turn **White**.*

---

## 🗣️ Command Reference

| Action | Commands |
| :--- | :--- |
| **Start Flight** | "Takeoff", "Arm", "Take off" |
| **Navigation** | "Forward", "Backward", "Left", "Right" |
| **Rotation** | "Turn Left", "Turn Right" |
| **Altitude** | "Higher", "Up", "Lower", "Down" |
| **Hover/Stop** | "Stop", "Hover" |
| **Emergency** | "Abort", "Kill", "Emergency" |
| **LED Colors** | "Red", "Blue", "Green", "Yellow", "Purple", "White", "Off" |

---

## 📁 Project Structure

- `voice_control.py`: The heart of the system—handles voice processing and drone telemetry.
- `list_mics.py`: A utility script to help you configure your audio input.
- `requirements.txt`: List of necessary Python libraries.
- `.gitignore`: Ensures your repository stays clean by ignoring local models and temporary files.

---

## ⚠️ Troubleshooting

- **"Model not found"**: Ensure the Vosk model is in a folder named exactly `model` in the root directory.
- **PyAudio Errors**: On Windows, you may need to install the PyAudio wheel directly if `pip install` fails.
- **Drone Connection**: Ensure your computer is on the same Wi-Fi network as the LiteWing drone.

---

*Part of the LiteWing Gesture & Voice Control Project.*
