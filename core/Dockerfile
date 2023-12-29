FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /drf_src

RUN ls .

RUN pip install -r requirements.txt

VOLUME /drf_src

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000