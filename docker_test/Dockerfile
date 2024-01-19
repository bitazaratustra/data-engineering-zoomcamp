FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipelines.py pipelines.py


ENTRYPOINT [ "python", "pipelines.py"]
