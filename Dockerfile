FROM python:3.6-alpine
ADD . /
WORKDIR /
CMD ["python", "parsing.py"]
