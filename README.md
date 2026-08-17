# LIVEHACKATHON

Agents for Humans — **Bill & Subscription Watchdog** (Everyday track).

## Setup (Windows)

```powershell
cd $HOME\Desktop\LIVEHACKATHON
.\.venv\Scripts\Activate.ps1
python --version
```

Strands is already installed in `.venv`.

## AWS (required for hello.py)

1. Create team AWS account + enable Bedrock model access (Claude).
2. Configure credentials:

```powershell
aws configure
```

Or set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION` (e.g. `us-west-2`).

## Smoke test

```powershell
.\.venv\Scripts\Activate.ps1
python hello.py
```

If it answers, Strands + Bedrock are working.
