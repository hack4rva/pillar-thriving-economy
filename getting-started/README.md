Getting Started: OpenCode + Featherless

**TL;DR (Event Day)**
- From the repo root run one of:
  - `FEATHERLESS_API_KEY=YOUR_KEY bash ./bootstrap.sh --no-persist`
  - `./bootstrap.sh --key YOUR_KEY --no-persist`
- Launch OpenCode: `opencode --config ./opencode.json`
- Use shortcuts: `/code`, `/reason`, `/ideate`

**What You Get**
- OpenAI‑compatible Featherless provider preconfigured in `opencode.json`.
- Default model: `featherless/kimi-k2-thinking` (ideation, long‑context).
- One‑tap commands:
  - `/code` → `featherless/qwen25-coder-32b-instruct` (coding)
  - `/reason` → `featherless/qwen25-72b-instruct` (reasoning)
  - `/ideate` → `featherless/kimi-k2-thinking` (ideation)
- Provider locked to Featherless via `enabled_providers`.

**Prerequisites**
- OpenCode CLI installed and on `PATH` (see `https://opencode.ai/`).
- A Featherless API key provided at the event.

**Bootstrap Options**
- Safer for history: `FEATHERLESS_API_KEY=YOUR_KEY bash ./bootstrap.sh --no-persist`
- CLI arg: `./bootstrap.sh --key YOUR_KEY --no-persist`
- Interactive: `bash ./bootstrap.sh` (prompts for key and persistence)
- The script verifies API access and prepares `opencode.json` (idempotent).

**Launch & Shortcuts**
- Start: `opencode --config ./opencode.json`
- Use:
  - `/code Review this PR and suggest fixes`
  - `/reason Outline the service architecture and tradeoffs`
  - `/ideate Brainstorm product directions for Q4`

**Models Configured**
- `featherless/qwen25-coder-32b-instruct` → Qwen/Qwen2.5-Coder-32B-Instruct
- `featherless/qwen3-32b` → Qwen/Qwen3-32B
- `featherless/qwen25-72b-instruct` → Qwen/Qwen2.5-72B-Instruct
- `featherless/kimi-k2-instruct` → moonshotai/Kimi-K2-Instruct
- `featherless/kimi-k2-thinking` → moonshotai/Kimi-K2-Thinking (default)
- `featherless/kimi-k2.5` → moonshotai/Kimi-K2.5
- `featherless/kimi-dev-72b` → moonshotai/Kimi-Dev-72B

**Persist The Key (Optional)**
- zsh: add to `~/.zshrc` → `export FEATHERLESS_API_KEY='YOUR_KEY'`
- bash: add to `~/.bashrc` (or `~/.bash_profile` on macOS)
- Apply in current shell: `source ~/.zshrc` (or appropriate file)

**Troubleshooting**
- Not in `/connect`: Use `/model` or shortcuts; `/connect` is for integrations.
- Invalid config keys: Only `provider` (singular) is valid.
- Didn’t load config: Run from repo root or pass `--config ./opencode.json`.
- 401/403 on `/v1/models`: Re‑export key and retry.
- No `/model` command: Use `/settings` → Models to switch.

**Slack Message Template**
- Share on event day for quick setup:

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

Tip: Prefer the env-var form to avoid key in shell history. Ping here if you hit issues.
```

See `getting-started/opencode-featherless-setup.md` for full details.

