---
name: face-detection-uv4l-pi
title: "Face Detection on Raspberry Pi with UV4L"
description: "Use when building real-time face detection web apps on Raspberry Pi using UV4L Streaming Server with WebRTC and OpenCV.js — covers installation, configuration, and custom web app development."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [raspberry-pi, uv4l, webrtc, face-detection, opencv-js, computer-vision, iot]
---
# Face Detection on Raspberry Pi with UV4L

## Purpose

Build custom web applications for real-time face detection on Raspberry Pi using UV4L Streaming Server with WebRTC signaling and OpenCV.js in the browser.

## When to Use

- Raspberry Pi camera projects with browser-based UI
- Real-time computer vision on edge devices
- WebRTC streaming from Pi camera
- Custom face detection web apps

## When NOT to Use

- High-performance/low-latency requirements (use native OpenCV)
- Production-scale video analytics
- Non-Pi platforms

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug WebRTC signaling, OpenCV.js loading, camera access |
| `executing-plans` | Multi-component setup (UV4L + web server + signaling) |

## Workflow

### Phase 1: UV4L Installation on Raspberry Pi

```bash
# Add UV4L repository
curl https://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
echo "deb https://www.linux-projects.org/listing/uv4l_repo/raspbian/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/uv4l.list

sudo apt update
sudo apt install uv4l uv4l-server uv4l-webrtc uv4l-raspicam uv4l-raspicam-extras
```

### Phase 2: Configuration

Edit `/etc/uv4l/uv4l-raspicam.conf`:

```ini
server-option = --enable-www-server=yes
server-option = --www-root-path=/usr/share/uv4l/demos/facedetection/
server-option = --www-port=80
server-option = --www-webrtc-signaling-path=/webrtc
```

Restart:
```bash
sudo service uv4l_raspicam restart
```

### Phase 3: Access Web App

Open browser: `http://<RaspberryPi-IP>`

- Click "Start Streaming"
- Click "Toggle Face Detection" for real-time detection (red rectangles)

### Phase 4: Source Code Structure

Location: `/usr/share/uv4l/demos/facedetection/`

| File | Purpose |
|------|---------|
| `index.html` | UI with video element and controls |
| `main.js` | User callbacks (start/stop, face detection toggle) |
| `signalling.js` | WebRTC signaling protocol |
| `face-detection.js` | OpenCV.js face detection logic |

### Phase 5: Custom Web App Development

**Key Integration Points:**

1. **WebRTC Connection** — Use `signalling.js` as base
2. **OpenCV.js** — Load from CDN or local:
   ```html
   <script src="https://docs.opencv.org/4.x/opencv.js" async></script>
   ```
3. **Face Detection Loop:**
   ```javascript
   async function detectFaces() {
     const src = cv.imread(videoElement);
     const gray = new cv.Mat();
     cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY);
     const faces = new cv.RectVector();
     faceCascade.detectMultiScale(gray, faces, 1.1, 3, 0, new cv.Size(30, 30));
     // Draw rectangles on canvas
     src.delete(); gray.delete(); faces.delete();
     requestAnimationFrame(detectFaces);
   }
   ```

### Phase 6: Platform Detection

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "linux" and platform.machine() in ("armv7l", "aarch64"):
        print("Raspberry Pi detected — UV4L will work")
    elif system == "linux":
        print("Linux detected — UV4L only works on Pi, not x86 Linux")
    elif system == "windows":
        print("Windows: Cross-compile or use VNC to Pi for development")
    elif system == "darwin":
        print("macOS: SSH/RDP to Pi; no native UV4L")
    return system
```

### Phase 7: Error Handling

```python
# Common UV4L errors
UV4L_ERRORS = {
    "no_camera_detected": "Check camera connection: vcgencmd get_camera",
    "service_not_running": "sudo service uv4l_raspicam restart",
    "port_in_use": "Check /etc/uv4l/uv4l-raspicam.conf for www-port",
    "opencv_not_loaded": "Wait for cv.onRuntimeInitialized before detection",
    "webrtc_signaling_failed": "Check network and firewall on port 80/443",
    "permission_denied": "Add user to video group: sudo usermod -aG video $USER",
}

def resolve_uv4l_error(error: str) -> str:
    for key, message in UV4L_ERRORS.items():
        if key in error:
            return message
    return "Unknown error — check /var/log/uv4l/uv4l.log"
```

### Phase 8: Advanced Use Cases

- Audio processing + bidirectional streaming
- FPV robot control
- Multi-peer video conferencing
- Server-side AI with TensorFlow (Python bridge)

## Pitfalls

- **OpenCV.js load timing** — Must wait for `cv['onRuntimeInitialized']`
- **WebRTC on Pi** — Limited to 1-2 concurrent viewers; use SFU for more
- **Camera permissions** — Browser requires HTTPS for camera (use self-signed or localhost)
- **Performance** — Pi 4 handles ~15fps face detection; Pi 3 struggles
- **UV4L version conflicts** — Pin versions; `apt-mark hold uv4l*`

## Verification Checklist

- [ ] UV4L service running (`systemctl status uv4l_raspicam`)
- [ ] Web UI accessible at Pi IP
- [ ] Video streams (Start Streaming works)
- [ ] Face detection toggles (rectangles appear)
- [ ] Custom app loads OpenCV.js successfully
- [ ] Detection runs at acceptable FPS

## References

- `references/uv4l-config-guide.md` — All config options
- `references/opencv-js-face-detection.md` — OpenCV.js API details
- `references/webrtc-signaling-protocol.md` — Custom signaling

## Templates

- `templates/custom-facedetection.html` — Minimal starter template

## Scripts

- `scripts/install-uv4l.sh` — Automated installation
- `scripts/benchmark-facedetection.py` — FPS measurement