# VSDC Video Masking Patterns

## Face Blurring Workflow

1. **Import Video** → Add to timeline
2. **Video Effects** → Filters → **Mask**
3. **Mask Shape** → Ellipse/Rectangle/Freeform
4. **Position** → Place over face
5. **Blur Settings** → Gaussian/Box blur, intensity
6. **Keyframes** → Animate mask position for moving faces

## Object Tracking

```
Video Effects → Movement → Motion Tracking
→ Select tracker type (Point/Planar)
→ Track object
→ Apply mask to tracked data
```

## Selective Effects

```python
# VSDC Pro scripting (conceptual)
effect = video_effects.Mask(
    shape="ellipse",
    position=(x, y),
    size=(w, h),
    feather=10,
    blur_type="gaussian",
    blur_radius=25
)
effect.keyframes.add(frame=0, position=(x1, y1))
effect.keyframes.add(frame=100, position=(x2, y2))
```

## Export Settings

- **Format**: MP4 (H.264) for compatibility
- **Bitrate**: 10-20 Mbps for HD
- **Keyframe interval**: 2s for streaming