# Face Detection on Video Stream with UV4L

> **Source:** https://www.linux-projects.org/uv4l/tutorials/custom-webapp-with-face-detection
> **Retrieved:** 2026-06-01T00:00:00

---

## Overview

UV4L Streaming Server on Raspberry Pi enables custom web apps using HTML5/JavaScript for real-time face detection via WebRTC.

## Setup

Install on Raspberry Pi:
```
uv4l, uv4l-server, uv4l-webrtc, uv4l-raspicam, uv4l-raspicam-extras
```

## Configuration

Edit `/etc/uv4l/uv4l-raspicam.conf`:
```
server-option = --enable-www-server=yes
server-option = --www-root-path=/usr/share/uv4l/demos/facedetection/
server-option = --www-port=80
server-option = --www-webrtc-signaling-path=/webrtc
```

Restart: `sudo service uv4l_raspicam restart`

## Usage

Access at `http://<RaspberryPi-IP>`:
- Click "Start Streaming"
- Click "Toggle Face Detection" for real-time detection (red rectangles)

## Source Code

Located at `/usr/share/uv4l/demos/facedetection/`:
- index.html: UI
- main.js: User callbacks
- signalling.js: WebRTC signaling
- face-detection.js: OpenCV.js face detection

## Advanced Use Cases

- Audio processing + bidirectional streaming
- FPV robot control
- Multi-peer video conferencing
- Server-side AI with TensorFlow

---

*Extracted by web-research-pipeline v1.0.0*