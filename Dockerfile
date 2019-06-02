FROM python:3.6

ADD . /usr/src/personal-blog
WORKDIR /usr/src/personal-blog

LABEL Name=Personal-Blog Version=0.0.1
EXPOSE 5000

RUN python -m pip install -r requirements.txt
CMD ["python", "app/app.py"]