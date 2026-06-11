# Built-in Personalities (14 Available)

| Name | Vibe | Best For |
|------|------|----------|
| `helpful` | Friendly, general-purpose | Default, everyday use |
| `concise` | Brief, to-the-point | Quick answers, code review |
| `technical` | Detailed, accurate expert | Deep technical discussions |
| `creative` | Innovative, outside-the-box | Brainstorming, design |
| `teacher` | Patient educator with examples | Learning, onboarding |
| `kawaii` | Cute, sparkles, enthusiasm ★ | Fun, lighthearted |
| `catgirl` | Neko-chan, cat expressions, nya~ | Playful, anime fans |
| `pirate` | Captain Hermes, tech-savvy buccaneer | Entertainment, themed sessions |
| `shakespeare` | Bardic prose, dramatic flair | Creative writing, fun |
| `surfer` | Chill bro vibes | Relaxed coding sessions |
| `noir` | Hard-boiled detective narration | Mystery-solving, debugging |
| `uwu` | Maximum cute uwu-speak | Maximum cute |
| `philosopher` | Deep contemplation | Architectural decisions |
| `hype` | MAXIMUM ENERGY!!! | Motivation, celebration |

## Switching
```bash
/personality              # List all
/personality <name>       # Switch for session
```

## Key Insight
`/personality` overlays on top of `SOUL.md` — your global default still applies unless the overlay meaningfully changes it.

## Custom Personalities
Add to `config.yaml`:
```yaml
agent:
  personalities:
    codereviewer: >
      You are a meticulous code reviewer. Identify bugs, security issues,
      performance concerns, and unclear design choices. Be precise and constructive.
```