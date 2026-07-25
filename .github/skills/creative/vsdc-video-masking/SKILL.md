---
name: vsdc-video-masking
title: "Video Masking in VSDC Video Editor"
description: "Use when applying video masks in VSDC Pro for face blurring, object tracking, and selective effects — covers inverted masks, motion tracking, and composition modes."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [vsdc, video-editor, masking, face-blur, motion-tracking, video-effects, pro]
---
# Video Masking in VSDC Video Editor

## Purpose

Create professional video masks in VSDC Pro for face blurring, object isolation, color grading regions, and motion-tracked effects.

## When to Use

- Post-production face blurring (not real-time)
- Object tracking with masks
- Selective color/effect application
- Privacy compliance for recorded video

## When NOT to Use

- Real-time video chat (use OBS Virtual Camera)
- Free version (masking requires VSDC Pro, $19.99/year)
- Non-Windows platforms (Windows only)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug motion tracking drift, mask alignment |
| `executing-plans` | Multi-step masking workflow |

## Workflow

### Phase 1: Inverted Mask (Pixelization) - Face Blurring

1. Add video to timeline
2. **Video Effects** → **Filters** → **Pixelize**
3. Select Pixelize layer → **Add Ellipse** (or Rectangle/Free Shape)
4. Position ellipse over face
5. Right-click Ellipse → **Properties** → **Composition mode** → **Mask** → **Inverted mask** → **Yes**
6. Result: Only ellipse area pixelated, rest clear

### Phase 2: Motion Tracking (Follow Moving Face)

1. Right-click video → **"Create a movement map"**
2. Place tracking frame over face
3. Press **Start analysis** → VSDC tracks movement
4. Apply map to Pixelize layer → **Add object** → **Movement** → **Movement map**
5. Preview: pixelation follows face

### Phase 3: Mask Types & Composition Modes

| Mask Type | Use Case |
|-----------|----------|
| Ellipse/Rectangle | Simple face/object blur |
| Free Shape | Complex outlines (ears, hair) |
| Text Mask | Text-shaped effects |

**Composition Modes:**
- **Mask** — Show only masked area
- **Inverted Mask** — Hide masked area, show rest
- **None** — Normal layer behavior

### Phase 4: Advanced Applications

- **Color grading** — Mask → Color Correction → affect only region
- **Object replacement** — Mask → Chroma Key → insert new content
- **Multiple masks** — Layer masks for complex shapes
- **Feathering** — Properties → **Blur** for soft edges

### Phase 5: Export

- **Pro required** for export without watermark
- Hardware acceleration: H.264/H.265 NVENC/QuickSync
- Recommended: MP4, H.264 High Profile, 1080p/4K

### Phase 6: Platform Detection & Error Handling

```python
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        print("Windows: VSDC supports Windows 7+, dx11 required")
    elif system == "darwin":
        print("macOS: VSDC not available — use Final Cut Pro or DaVinci Resolve")
    elif system == "linux":
        print("Linux: VSDC not available — use Kdenlive or DaVinci Resolve")
    return system

# Common VSDC masking issues
MASK_ERRORS = {
    "mask_not_appearing": "Check composition mode (Mask/Inverted Mask), not Normal",
    "tracking_lost": "Reduce movement speed; add manual keyframes",
    "pixelation_too_broad": "Reduce ellipse size or increase feathering",
    "export_watermak": "Pro license required for clean export",
    "performance_slow": "Use proxies for 4K; disable preview effects",
}

def resolve_mask_error(error: str) -> str:
    for key, message in MASK_ERRORS.items():
        if key in error:
            return message
    return "Unknown — check VSDC community forums"
```

## Pitfalls

- **Pro license required** — Free version exports with watermark
- **Tracking drift** → Re-analyze if tracking loses target; add keyframes manually
- **Mask edge artifacts** → Increase feathering; check "Anti-aliasing"
- **Performance** — 4K tracking slow; proxy workflow recommended
- **Windows only** — No Mac/Linux native version

## Verification Checklist

- [ ] Mask covers target in all frames
- [ ] Motion tracking follows smoothly
- [ ] No edge artifacts (feathering applied)
- [ ] Export quality acceptable
- [ ] Pro license active

## References

- `references/vsdc-masking-guide.md` — Detailed workflow with screenshots
- `references/vsdc-motion-tracking.md` — Tracking parameters and troubleshooting
- `references/vsdc-composition-modes.md` — All blend/composition modes
- `references/vsdc-masking-patterns.md` — Video masking workflow patterns

## Templates

- `templates/vsdc-mask-settings.json` — Mask configuration template

## Scripts

- `scripts/vsdc-export-settings.py` — Export settings helper