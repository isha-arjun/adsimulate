# AdSimulate API

FastAPI service for deterministic campaign-economics calculations.

## Endpoints

- `GET /api/v1/health`
- `POST /api/v1/simulate`
- Interactive API documentation at `/docs`

The simulator uses only caller-supplied assumptions. Responses are deterministic scenarios, not measured outcomes or validated performance predictions.

## Local run

From the repository root:

```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --app-dir backend --reload
```
