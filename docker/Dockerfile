FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install git+https://github.com/maistodos/python-creditcard.git@main
RUN pip install -r requirements.txt

COPY src src
COPY run run

WORKDIR /app/src
RUN python manage.py collectstatic

CMD [ "/app/run/entry_point.sh" ]