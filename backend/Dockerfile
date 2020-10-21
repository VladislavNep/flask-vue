FROM python:3.9.0-alpine3.12 as backend
MAINTAINER Vladislav Nepomnyashchikh 'vladislavnep@gmail.com'
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "backend/views.py"
ENV FLASK_ENV "development"
WORKDIR /backend
COPY . /backend
RUN pip install -r requirements.txt
CMD ['python', 'views.py']