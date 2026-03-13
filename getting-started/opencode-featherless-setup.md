OpenCode + Featherless Setup

- Goal: Enable Featherless as an OpenAI‑compatible provider in OpenCode with one‑tap model shortcuts for coding, reasoning, and ideation.
- Audience: Engineers using this repo (macOS/Linux/WSL).

Prerequisites
- OpenCode CLI installed and on PATH (see https://opencode.ai/).
- A Featherless API key per engineer.

Quick Start (Recommended)
- In a terminal at the repo root, run one of these:
  - Safe for history (recommended):
    - `FEATHERLESS_API_KEY=YOUR_KEY bash ./bootstrap.sh --no-persist`
  - Simple arg form (may appear in shell history/process list):
    - `./bootstrap.sh --key YOUR_KEY --no-persist`
- Or run interactively (prompts for the key and persistence):
  - `bash ./bootstrap.sh`
- The script verifies API access and sets up `opencode.json` (idempotent; it won’t overwrite if present).
- Launch OpenCode:
  - `opencode --config ./opencode.json`
- Use the built‑in command shortcuts:
  - `/code`   → Qwen2.5‑Coder‑32B‑Instruct (coding)
  - `/reason` → Qwen2.5‑72B‑Instruct (deeper reasoning)
  - `/ideate` → Kimi‑K2‑Thinking (ideation, long‑context)

What’s In The Repo Config
- File: `opencode.json` (auto‑loaded by OpenCode from the current directory)
- Default model: `featherless/kimi-k2-thinking`
- Custom provider: `featherless` (OpenAI‑compatible)
- Model aliases under `provider.featherless.models`:
  - `qwen25-coder-32b-instruct` → Qwen/Qwen2.5-Coder-32B-Instruct
  - `qwen3-32b` → Qwen/Qwen3-32B
  - `qwen25-72b-instruct` → Qwen/Qwen2.5-72B-Instruct
  - `kimi-k2-instruct` → moonshotai/Kimi-K2-Instruct
  - `kimi-k2-thinking` → moonshotai/Kimi-K2-Thinking
  - `kimi-k2.5` → moonshotai/Kimi-K2.5
  - `kimi-dev-72b` → moonshotai/Kimi-Dev-72B
- Command shortcuts (under `command`):
  - `/code` uses `featherless/qwen25-coder-32b-instruct`
  - `/reason` uses `featherless/qwen25-72b-instruct`
  - `/ideate` uses `featherless/kimi-k2-thinking`

Manual Setup (Alternative)
- Export your key in the same shell you will use:
  - `export FEATHERLESS_API_KEY='<your-key>'`
- Verify the key:
  - `curl -fsS https://api.featherless.ai/v1/models -H "Authorization: Bearer $FEATHERLESS_API_KEY" | head`
  - Expect a JSON list; HTTP 401/403 indicates a key issue.
- Launch OpenCode from the repo root:
  - `opencode --config ./opencode.json`
- Switch models with `/model featherless/<alias>` if you prefer manual control:
  - e.g., `/model featherless/kimi-k2-thinking`

Persisting The API Key
- zsh: append to `~/.zshrc` → `export FEATHERLESS_API_KEY='<your-key>'`
- bash: append to `~/.bashrc` (or `~/.bash_profile` on macOS)
- Apply in current shell: `source ~/.zshrc` (or the appropriate file)
- Security note: dotfiles are plaintext. Prefer per‑user keys and avoid committing or sharing.

Troubleshooting
- “Featherless not in /connect”: `/connect` is for third‑party integrations. Featherless is a model provider. Use `/model` or the shortcuts above.
- “Invalid config: unrecognized key”: Only use `provider` (singular). Do not use `providers`.
- Config not loading: Start OpenCode from the repo root or pass `--config ./opencode.json`.
- 401/403 on `/v1/models`: Re‑export your key and ensure you’re in the same shell that launches OpenCode.
- Can’t switch models: Try `/help` and `/settings` → Models if `/model` is not available in your build.
- Concerned about key exposure: Prefer the env‑var one‑liner to avoid the key in shell history.

Scale‑Out Tips (for Team Leads)
- Share `bootstrap.sh` and this page; ask engineers to run the script from the repo root.
- Keys: issue per‑engineer keys via SSO/Secrets Manager (avoid Slack/email). Rotate when needed.
- Lock to Featherless only (optional): add `"enabled_providers": ["featherless"]` to `opencode.json`.
- Add more shortcuts: extend the `command` section for common workflows (e.g., `/test`, `/doc`, `/refactor`).

FAQ
- Q: Where do I see the current model?
  - A: In the TUI status bar. After running a shortcut, it updates immediately.
- Q: Can I use other Featherless models?
  - A: Yes. Use `/model featherless/<alias>` or add a new alias under `provider.featherless.models`.

