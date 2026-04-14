Here’s a clean README.md for your project:


---

📺 OscyStreamer (drafted by chat)

Real-time webcam → vector graphics → XY oscilloscope renderer

OscyStreamer converts live camera input into simplified vector paths and streams them as analog XY signals for display on an oscilloscope in XY mode (or any XY deflection display system).

It is essentially a pipeline that turns vision into continuous analog waveforms.


---

🧠 Overview

OscyStreamer processes visual input through the following stages:

Webcam Frame
    ↓
Edge Detection (Canny)
    ↓
Contour Extraction
    ↓
Path Simplification (Douglas–Peucker)
    ↓
Vector Interpolation
    ↓
Normalization (-1..1)
    ↓
Serial Streaming
    ↓
ESP32 DAC Output
    ↓
Oscilloscope XY Display


---

✨ Features

🎥 Real-time webcam capture

🧠 Edge-based vectorization

✂️ Path simplification for stable traces

📡 Live serial streaming to microcontroller

⚡ ESP32 dual-DAC XY output support

📺 Oscilloscope XY mode visualization



---

🧰 Requirements

Python Dependencies

pip install numpy opencv-python pyserial

Hardware (Optional but intended)

ESP32 (recommended: ESP32-S3 or ESP32 DevKit)

Analog oscilloscope with XY mode

2-channel DAC output (ESP32 internal DAC supported)

USB serial connection



---

📁 Project Structure

OscyStreamer/
│
├── python/
│   ├── capture.py
│   ├── vectorize.py
│   ├── path_simplify.py
│   ├── waveform.py
│   ├── serial_stream.py
│   └── main.py
│
├── esp32/
│   └── xy_dac_driver.ino
│
├── requirements.txt
└── README.md


---

🚀 Quick Start

1. Clone / Setup

git clone <repo-url>
cd OscyStreamer
pip install -r requirements.txt


---

2. Connect Hardware (optional)

Wire ESP32 DAC outputs:

Signal	ESP32 Pin

X-axis	GPIO25 (DAC1)
Y-axis	GPIO26 (DAC2)


Connect:

DAC1 → Oscilloscope CH1 (X input)

DAC2 → Oscilloscope CH2 (Y input)

Common GND required



---

3. Upload ESP32 Firmware

Open:

esp32/xy_dac_driver.ino

Upload via Arduino IDE or PlatformIO.


---

4. Run Python Streamer

python python/main.py

Press:

Q → quit


---

⚙️ Configuration

Inside main.py:

STREAM_PORT = "COM3"   # or /dev/ttyUSB0
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

Inside waveform tuning:

samples=20        # smoothness of curves
epsilon=2.0       # simplification strength


---

📺 Oscilloscope Setup

Set oscilloscope to:

Mode: XY mode

Channel 1 → X input

Channel 2 → Y input

Adjust gain until full screen fill

Enable persistence (optional for drawing effect)



---

🧠 How It Works

1. Vision → edges

Uses Canny edge detection to extract structure.

2. Edges → contours

Finds closed and open shapes in the image.

3. Contours → simplified paths

Reduces noise and unnecessary points.

4. Paths → continuous waveforms

Interpolates between points for smooth analog motion.

5. Waveforms → DAC signals

Maps normalized coordinates into analog voltages.


---

⚡ Performance Notes

Lower resolution = faster + more stable output

Fewer contour points = less flicker

Higher interpolation = smoother curves but more data

Serial speed is a limiting factor (~115200 baud recommended minimum)



---

🧪 Limitations

No pen lift simulation (continuous drawing only)

Serial bandwidth limits high-resolution detail

ESP32 DAC is 8-bit (256 levels)

Oscilloscope bandwidth affects smoothness



---

🔥 Possible Upgrades

🧠 Smart stroke ordering

Reduces beam travel distance (improves image stability)

🧲 Bézier curve smoothing

More natural analog motion

⚡ Direct USB DAC / higher-speed SPI DAC

Higher resolution rendering

🎯 Laser / galvanometer adaptation

Convert output to laser projector system

🧩 AI contour selection

Prioritize perceptual features instead of raw edges


---

🧬 Philosophy

OscyStreamer treats images not as pixels, but as continuous motion through space, turning visual data into a physical trajectory.

It is closer to:

analog synthesis

motion sculpture

vector handwriting


than traditional raster graphics.


---

📜 License

MIT

