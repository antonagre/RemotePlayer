FROM python:latest
COPY . /tmp/myapp
RUN pip3 install -r /tmp/myapp/requirements.txt

EXPOSE 5550
WORKDIR /tmp/myapp/
CMD ./tmp/myapp/start.sh