export PYTHONDONTWRITEBYTECODE=1
uvicorn main:app --app-dir src --env-file .env --reload --port 3000 --host localhost
