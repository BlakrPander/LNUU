FROM python:3.8-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install Flask gunicorn
RUN pip install selenium
RUN pip install Pillow
RUN pip install image

CMD exec gunicorn --bind :80 --workers 1 --threads 8 --timeout 0 main:app