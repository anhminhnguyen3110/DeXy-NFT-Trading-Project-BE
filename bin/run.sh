export PYTHONDONTWRITEBYTECODE=1
black src/ --line-length=80 
uvicorn main:app --app-dir src --env-file .env --reload --port 3000 --host localhost
