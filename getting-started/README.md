# Getting Started: OpenCode + Featherless

**TL;DR (Event Day)**
- From the repo root run one of:
  - `FEATHERLESS_API_KEY=YOUR_KEY bash ./bootstrap.sh --no-persist`
  - `./bootstrap.sh --key YOUR_KEY --no-persist`
- Launch OpenCode: `opencode --config ./opencode.json`
- Use shortcuts: `/code`, `/reason`, `/ideate`

---

## Prerequisites
- OpenCode CLI installed and on `PATH` (see https://opencode.ai/)
- A Featherless API key provided at the event

## Quick Start (Recommended)

Run one of these from the repo root:

```bash
# Safe for history (recommended)
FEATHERLESS_API_KEY=YOUR_KEY bash ./bootstrap.sh --no-persist

# Simple arg form (may appear in shell history)
./bootstrap.sh --key YOUR_KEY --no-persist

# Interactive (prompts for key and persistence)
bash ./bootstrap.sh
```

The script verifies API access and sets up `opencode.json` (idempotent — won't overwrite if present).

Launch OpenCode:
```bash
opencode --config ./opencode.json
```

## Command Shortcuts

| Shortcut | Model | Best for |
|----------|-------|----------|
| `/code`   | Qwen2.5-Coder-32B-Instruct | Coding |
| `/reason` | Qwen2.5-72B-Instruct | Deeper reasoning |
| `/ideate` | Kimi-K2-Thinking | Ideation, long-context |

## Models Configured

| Alias | Full model ID |
|-------|--------------|
| `qwen25-coder-32b-instruct` | Qwen/Qwen2.5-Coder-32B-Instruct |
| `qwen3-32b` | Qwen/Qwen3-32B |
| `qwen25-72b-instruct` | Qwen/Qwen2.5-72B-Instruct |
| `kimi-k2-instruct` | moonshotai/Kimi-K2-Instruct |
| `kimi-k2-thinking` | moonshotai/Kimi-K2-Thinking (default) |
| `kimi-k2.5` | moonshotai/Kimi-K2.5 |
| `kimi-dev-72b` | moonshotai/Kimi-Dev-72B |

## Manual Setup (Alternative)

```bash
export FEATHERLESS_API_KEY='<your-key>'
# Verify
curl -fsS https://api.featherless.ai/v1/models -H "Authorization: Bearer $FEATHERLESS_API_KEY" | head
# Launch
opencode --config ./opencode.json
```

Switch models manually: `/model featherless/<alias>`

## Persisting The API Key

- **zsh**: add `export FEATHERLESS_API_KEY='<your-key>'` to `~/.zshrc`
- **bash**: add to `~/.bashrc` (or `~/.bash_profile` on macOS)
- Apply: `source ~/.zshrc`

## Troubleshooting

- **Featherless not in `/connect`**: `/connect` is for integrations. Use `/model` or the shortcuts.
- **"Invalid config: unrecognized key"**: Use `provider` (singular), not `providers`.
- **Config not loading**: Run from repo root or pass `--config ./opencode.json`.
- **401/403 on `/v1/models`**: Re-export key and ensure you're in the same shell.
- **Can't switch models**: Try `/settings` → Models if `/model` isn't available.

## Event Day Slack Message

```
OpenCode + Featherless setup (2 minutes)

1) From repo root run ONE of:
   FEATHERLESS_API_KEY=YOUR_KEY bash ./bootstrap.sh --no-persist
   ./bootstrap.sh --key YOUR_KEY --no-persist

2) Launch OpenCode:
   opencode --config ./opencode.json

3) Use shortcuts:
   /code   (Qwen2.5-Coder-32B-Instruct)
   /reason (Qwen2.5-72B-Instruct)
   /ideate (Kimi-K2-Thinking)

Tip: Prefer the env-var form to avoid key in shell history.
```
