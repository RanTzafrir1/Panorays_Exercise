FROM python:3.7.5-slim-buster
LABEL version="1.0"
LABEL description="This project is created for recruitment purposes for Panorays"

ENV INSTALL_PATH /panorays
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8002 --access-logfile - "panorays.app:create_app()"
