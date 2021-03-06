FROM python:alpine3.12

RUN pip install --no-cache-dir kubernetes

COPY . /

ENTRYPOINT ["python", "pod.py"]
CMD ["default"]
