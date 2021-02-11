FROM python:3

RUN pip install --no-cache-dir kubernetes

COPY . /

ENTRYPOINT ["python", "pod.py"]
CMD ["default"]
