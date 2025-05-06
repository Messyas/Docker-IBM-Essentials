FROM python:3.12-slim
RUN pip install --upgrade pip
RUN pip install flask
CMD ["python", "app.py"]
COPY app.py /app.py
