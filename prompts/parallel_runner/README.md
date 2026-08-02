> **Note:** This research was generated using AI assistance (Claude + Parallel.ai) with human expert review. See [methodology](../../docs/methodology.md) for details.

# Parallel.ai Research Runner

Runs the prompts in `05_prompts/research/` through the Parallel.ai Task API and saves results to `research/`.

## Beginner Quickstart

No extra installs required. Just set your API key and run.

```bash
cp 05_prompts/parallel_runner/.env.example 05_prompts/parallel_runner/.env
$EDITOR 05_prompts/parallel_runner/.env   # set PARALLEL_API_KEY=your_key_here

# Run all pending prompts (skips ones with existing output)
python 05_prompts/parallel_runner/run_all.py --processor pro-fast

# Or run one prompt explicitly
python 05_prompts/parallel_runner/run_one.py 05_prompts/research/<your_prompt>.txt --processor pro-fast
```

Optional: If you prefer the SDK for other workflows, install it with `pip install parallel-ai`.

## Usage

**Run all pending prompts** (skips prompts that already have output):
```bash
python 05_prompts/parallel_runner/run_all.py
# or
make run-all
```

**Run a single prompt:**
```bash
python 05_prompts/parallel_runner/run_one.py 05_prompts/research/<your_prompt>.txt
# or
make run-one PROMPT=05_prompts/research/<your_prompt>.txt
```

Note: This pillar stores many prompts under `_admin/05_prompts/research`. You can point the runner there:

```bash
python 05_prompts/parallel_runner/run_all.py _admin/05_prompts/research
# or
make run-all PROMPTS_DIR=_admin/05_prompts/research
```

## Processor Selection

Edit `config.yaml` or pass `--processor`:

| Processor | Speed | Best for |
|-----------|-------|----------|
| `pro` | 2–10 min | Default — good depth, moderate cost |
| `pro-fast` | 30s–5 min | Faster, same cost tier |
| `ultra` | 5–25 min | Hardest prompts, higher cost |
| `ultra-fast` | 1–10 min | Fast + deep |

## Outputs

Each prompt produces a file in `research/`:
- `<basename>.md` — Markdown research report with inline citations

## Contents

- `parallel_client.py` — Minimal client (text-schema mode)
- `run_one.py` — Single-prompt runner
- `run_all.py` — Batch runner with skip/overwrite logic
- `config.yaml` — Processor and path configuration
- `.env.example` — API key template
- `Makefile` — Convenience targets
