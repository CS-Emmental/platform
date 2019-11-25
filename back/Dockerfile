FROM python:3.6-alpine

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run