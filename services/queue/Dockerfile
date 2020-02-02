# base image
FROM python:3.7.2-slim



# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


# copy project
COPY . /usr/src/app
EXPOSE 5004
RUN pip install rq-dashboard

EXPOSE 9181

CMD ["rq-dashboard"]
EXPOSE 9181

CMD ["rq-dashboard"]
CMD python manage.py run -h 0.0.0.0
# run server
# CMD ["/usr/src/app/entrypoint.sh"]