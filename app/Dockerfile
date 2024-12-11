FROM python:3.11-slim
WORKDIR /app
COPY app.py /app
RUN apt update
RUN apt -y install python3-dev libpq-dev
RUN pip install flask
RUN pip install psycopg2-binary
EXPOSE 3000
CMD ["python", "app.py"]