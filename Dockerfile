FROM python:3.10.13

WORKDIR /app
RUN apt-get install default-libmysqlclient-dev pkg-config
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000
CMD uvicorn main:app --app-dir src --env-file .env --reload --port 4000 --host 0.0.0.0
