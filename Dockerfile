FROM python:3.9

WORKDIR /app

RUN apt-get update

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x gunicorn.sh

ENTRYPOINT ["./gunicorn.sh"]
