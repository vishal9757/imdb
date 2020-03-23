#Download base image Python 3.6
FROM python:3.6

RUN mkdir fynd_project

WORKDIR /fynd_project

#Copy the current dir contents into the container at WORKDIR

COPY . /fynd_project

RUN pip install --upgrade pip

RUN pip install -r /fynd_project/requirements.txt

EXPOSE 5000

CMD ["uwsgi", "uwsgi.ini"]
