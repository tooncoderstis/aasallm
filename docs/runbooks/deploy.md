# Runbook — Build image & deploy ke EasyPanel

> Prosedur deploy demo `aasallm` (FastAPI, model char-level). Mekanisme mengikuti [ADR-0004](../adr/0004-deploy-easypanel.md) (programatik via MCP); **target aktual** ada di [ADR-0007](../adr/0007-target-deploy-aktual.md).
>
> **Status: sudah tayang** → https://aasallm-web.hgteop.easypanel.host/ (`/health = 200`).

## Target aktual (2026-10-17)
| Aspek | Nilai |
|---|---|
| Registry / image | **Docker Hub** `aasatech/aasallm-web:latest` |
| Project | **`m`** (project baru `aasallm` ditolak: batas paket) |
| Service | **`aasallmweb`** (type app, source: Docker image) |
| Domain | **`aasallm-web.hgteop.easypanel.host`** (HTTPS) |
| Port kontainer | `8000` |
| Verifikasi | `GET /health = 200`, `/generate`, `/explain`, `GET /` OK |

## Prasyarat
- Docker lokal (Docker Desktop).
- Kredensial registry (di sini: Docker Hub `aasatech`).
- Akses EasyPanel (MCP `easypanel` aktif; `EASYPANEL_API_KEY` dikelola server MCP).

## 1. Build & push image (lokal)
```powershell
$env:GHCR_OWNER = "aasatech"          # di sini memakai Docker Hub, bukan GHCR
deploy\easypanel-docker\build-push.ps1 -Owner aasatech -Tag latest
# atau manual:
docker build -f deploy/easypanel-docker/Dockerfile -t aasatech/aasallm-web:latest .
docker push aasatech/aasallm-web:latest
```

## 2. Smoke test image lokal (opsional)
```powershell
docker run --rm -p 8123:8000 aasatech/aasallm-web:latest
# lalu:  curl http://127.0.0.1:8123/health   -> {"status":"ok"}
```

## 3. Deploy via MCP EasyPanel (programatik)
1. `search_procedures` → `createAppService` (source image) bila service belum ada; `listProjectsAndServices` untuk cek.
2. Buat service:
   ```json
   {"projectName":"m","serviceName":"aasallmweb",
    "source":{"type":"image","image":"aasatech/aasallm-web:latest"},
    "ports":[{"published":8000,"target":8000}],
    "domains":[{"host":"aasallm-web.hgteop.easypanel.host","https":true,"port":8000,"internalProtocol":"http"}]}
   ```
3. `deployAppService` (project `m`, service `aasallmweb`).

> Ganti tag `latest` dengan tag versi (mis. commit SHA) agar rilis dapat dilacak.

## 4. Verifikasi
```powershell
curl https://aasallm-web.hgteop.easypanel.host/health     # {"status":"ok"}
curl -X POST https://aasallm-web.hgteop.easypanel.host/generate -H "Content-Type: application/json" -d "{\"prompt\":\"Model bahasa\",\"max_new_tokens\":40}"
```
Halaman chat: buka https://aasallm-web.hgteop.easypanel.host/.

## Catatan
- **Model** disajikan adalah GPT **char-level** yang dilatih dari `data/corpus.txt` saat permintaan pertama (malas). Kualitas teks terbatas — demo edukatif, bukan asisten.
- Ada **rate-limit** sederhana per IP (default 30 permintaan/menit) pada `/generate` dan `/explain`.
- Bila paket ditingkatkan / kredensial GHCR tersedia, migrasi ke project `aasallm` + GHCR dapat dilakukan tanpa mengubah image aplikasi (lihat ADR-0007).
