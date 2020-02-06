FROM python:3.7.2-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev


# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app
EXPOSE 5006
# run server
CMD python manage.py run -h 0.0.0.0