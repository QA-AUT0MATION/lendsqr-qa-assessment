# Lendsqr Adjutor API QA Assessment

This repository contains a small Pytest + Requests API automation framework for validating selected Adjutor API endpoints.

## Covered APIs

1. Karma Lookup
2. Bank Account BVN Verification

## Security Note

API keys must not be committed to GitHub. The framework reads the key from an environment variable.

## Setup

```bash
pip install -r requirements.txt
```

Set your API key:

Windows PowerShell:

```powershell
$env:ADJUTOR_API_KEY="your_api_key_here"
```

Mac/Linux:

```bash
export ADJUTOR_API_KEY="your_api_key_here"
```

## Run Tests

```bash
pytest
```

HTML report will be generated at:

```text
reports/test_report.html
```
