# Package stage
FROM python:3.6 as package-stage

WORKDIR /app/Emmental
COPY Pipfile* ./

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

# Package the back server in ./dist folder
RUN pip install wheel
COPY ./ ./
RUN mv setup.py /app
WORKDIR /app
RUN python setup.py bdist_wheel

# Install back server packaged
WORKDIR /app/dist
RUN pip install Emmental*.whl

# Launch uwsgi server 
RUN pip install uwsgi
EXPOSE 5000
WORKDIR /app/Emmental
CMD uwsgi --ini uwsgi.ini
