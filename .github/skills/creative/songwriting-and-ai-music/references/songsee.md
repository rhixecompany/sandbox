# Songsee — Audio Feature Visualization (reference)

> Demoted from the standalone `songsee` skill during umbrella consolidation.
> Use this when the user wants to *inspect* audio (spectrograms, MFCC, chroma, tempo)
> rather than *generate* it — e.g. comparing AI-music outputs, debugging synthesis, or
> documenting an audio pipeline.

Part of the `songwriting-and-ai-music` class: generation + analysis of music.

## Prerequisites
Requires [Go](https://go.dev/doc/install):
```bash
go install github.com/steipete/songsee/cmd/songsee@latest
```
Optional: `ffmpeg` for formats beyond WAV/MP3.

## Quick Start
```bash
songsee track.mp3                                   # Basic spectrogram
songsee track.mp3 -o spectrogram.png               # Save to file
songsee track.mp3 --viz spectrogram,mel,chroma,hpss,selfsim,loudness,tempogram,mfcc,flux
songsee track.mp3 --start 12.5 --duration 8 -o slice.jpg
cat track.mp3 | songsee - --format png -o out.png
```

## Visualization Types (`--viz`, comma-separated)
| Type | Description |
|------|-------------|
| `spectrogram` | Standard frequency spectrogram |
| `mel` | Mel-scaled spectrogram |
| `chroma` | Pitch class distribution |
| `hpss` | Harmonic/percussive separation |
| `selfsim` | Self-similarity matrix |
| `loudness` | Loudness over time |
| `tempogram` | Tempo estimation |
| `mfcc` | Mel-frequency cepstral coefficients |
| `flux` | Spectral flux (onset detection) |

Multiple `--viz` types render as a grid in a single image.

## Common Flags
| Flag | Description |
|------|-------------|
| `--style` | Color palette: `classic`, `magma`, `inferno`, `viridis`, `gray` |
| `--width` / `--height` | Output image dimensions |
| `--window` / `--hop` | FFT window and hop size |
| `--min-freq` / `--max-freq` | Frequency range filter |
| `--start` / `--duration` | Time slice of the audio |
| `--format` | Output format: `jpg` or `png` |

## Notes
- WAV and MP3 are decoded natively; other formats require `ffmpeg`.
- Output images can be inspected with `vision_analyze` for automated audio analysis.
