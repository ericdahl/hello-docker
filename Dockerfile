FROM ubuntu:latest

#EXPOSE 1111

#ENV PORT

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev # build-essential

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

CMD ["app.py"]

#CMD ["nc", "-lv", "1111"]
