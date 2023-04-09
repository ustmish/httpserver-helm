FROM python:3.9

WORKDIR /opt/app

RUN pip install requests psycopg2

COPY httpserver.py .

CMD ["python", "httpserver.py"] 
