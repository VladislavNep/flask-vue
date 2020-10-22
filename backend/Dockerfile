FROM python:3.7-stretch as backend
MAINTAINER Vladislav Nepomnyashchikh 'vladislavnep@gmail.com'
WORKDIR /backend
COPY . /backend
RUN pip install -r requirements.txt
CMD ["uwsgi", "uwsgi.ini"]