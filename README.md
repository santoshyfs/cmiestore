# CMI ChatGPT Product Search API

FastAPI wrapper over Magento GraphQL for ChatGPT Actions.

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints
- GET /health
- GET /search-products?q=shoes
