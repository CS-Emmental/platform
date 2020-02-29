FROM python:3.6

RUN pip install pipenv
COPY Pipfile* /app/
WORKDIR /app
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV=development
CMD flask run