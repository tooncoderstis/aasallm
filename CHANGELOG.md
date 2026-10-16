# Changelog

Semua perubahan penting didokumentasikan di file ini.

Format mengikuti [Keep a Changelog](https://keepachangelog.com) dan proyek ini menganut [Semantic Versioning](https://semver.org).

Status terkini: [`STATUS.md`](STATUS.md).

## [Unreleased]
### Added
- Fase 0: scaffold dokumen proyek (PRD, STATUS, CHANGELOG, ADR, runbook, catatan index).
- Struktur paket `src/aasallm` (np, torch, serve), `pyproject.toml`, smoke test.
- CI GitHub Actions (ruff + pytest), health files, secret scan.
- Pelaporan hub portofolio (`scripts/hub-report.mjs`, `npm run hub:report`).
- Fase 1: catatan Bab 1 (`docs/belajar/bab-01-apa-yang-dihitung-llm.md`) + seed `cheatsheet.md` & `glosarium.md`.
- Fase 1: catatan Bab 2 (`docs/belajar/bab-02-notasi.md`); `cheatsheet.md` & `glosarium.md` diperluas (notasi, eksponensial, logaritma).
- Fase 1: modul vektor NumPy (`src/aasallm/np/vectors.py`) + uji (`tests/test_vectors.py`) + catatan Bab 3 (`docs/belajar/bab-03-vektor.md`).
- Fase 1: modul matriks NumPy (`src/aasallm/np/matrices.py`) + uji (`tests/test_matrices.py`) + catatan Bab 4 (`docs/belajar/bab-04-matriks.md`).
- Fase 1: modul probabilitas NumPy (`src/aasallm/np/probability.py`) + uji (`tests/test_probability.py`) + catatan Bab 5 (`docs/belajar/bab-05-probabilitas.md`).
- Fase 1: modul teori informasi NumPy (`src/aasallm/np/information.py`) + uji (`tests/test_information.py`) + catatan Bab 6 (`docs/belajar/bab-06-informasi.md`).
- Fase 1: modul turunan/gradien NumPy (`src/aasallm/np/calculus.py`) + uji (`tests/test_calculus.py`) + catatan Bab 7 (`docs/belajar/bab-07-turunan.md`).
- Fase 1: catatan Bab 1–7, `cheatsheet.md`, dan `glosarium.md` lengkap untuk fondasi.

### Changed
- Fase 0 (Setup & Fondasi) dituntaskan ✅; hub portofolio tersinkron (`aasallm`, 13 fase terbaca).
- Keputusan model demo dicatat: mini-LLM Bab 21 = verifikasi, demo = model char-level Fase 11 (ADR-0006).
- Fase 1 (Fondasi Matematika, Bab 1–7) dimulai 🔄 lalu dituntaskan ✅: 5 modul NumPy (`vectors`, `matrices`, `probability`, `information`, `calculus`) + 7 catatan bab, seluruh uji hijau.
### Fixed

## [0.1.0] - 2026-10-11
### Added
- Inisialisasi proyek `aasallm`: belajar & membangun LLM dari nol mengikuti buku *"Memahami Matematika di Balik LLM"*.
