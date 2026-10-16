# Runbooks

Prosedur operasional. Satu berkas per prosedur.

| Runbook | Status |
|---|---|
| `deploy.md` — build image & deploy ke EasyPanel | ⬜ (Fase 12) |
| `kegunaan-llm.md` — apa gunanya LLM & bagaimana cara kerjanya (edukatif) | ⬜ (Fase 12) |

## Ringkas: operasional lokal
```sh
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
.venv\Scripts\pytest
.venv\Scripts\ruff check .
```
