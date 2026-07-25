# UV4L Face Detection Patterns

## Raspberry Pi Setup

```bash
# Install UV4L
curl http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
echo "deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main" | sudo tee /etc/apt/sources.list.d/uv4l.list
sudo apt-get update
sudo apt-get install uv4l uv4l-raspicam uv4l-raspicam-extras uv4l-server uv4l-webrtc
```

## WebRTC Streaming

```python
# Start UV4L with WebRTC
uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --framerate 30 \
     --encoding h264 --server-option '--port=9000' \
     --server-option '--webrtc=yes' --server-option '--webrtc-port=9001'
```

## Face Detection Integration

```python
import cv2
import requests

# Get stream from UV4L
cap = cv2.VideoCapture("http://pi-ip:9000/stream/video.mjpeg")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Web Interface

Access at `http://pi-ip:9000/stream/webrtc` for WebRTC streaming with face overlay.