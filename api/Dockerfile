FROM python:3.9

WORKDIR /api
EXPOSE 5000

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "/api/__init__.py"]