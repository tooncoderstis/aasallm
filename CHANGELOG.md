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

### Changed
- Fase 0 (Setup & Fondasi) dituntaskan ✅; hub portofolio tersinkron (`aasallm`, 13 fase terbaca).
- Keputusan model demo dicatat: mini-LLM Bab 21 = verifikasi, demo = model char-level Fase 11 (ADR-0006).
### Fixed

## [0.1.0] - 2026-10-11
### Added
- Inisialisasi proyek `aasallm`: belajar & membangun LLM dari nol mengikuti buku *"Memahami Matematika di Balik LLM"*.
