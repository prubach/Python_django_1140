FROM python:3.8-buster

# copy source and install dependencies
#RUN apt install -y lynx
RUN mkdir -p /opt/app
COPY requirements.txt start.sh /opt/app/
RUN chmod +x /opt/app/start.sh
COPY bank /opt/app/bank/
WORKDIR /opt/app
RUN pip install -r requirements.txt

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start.sh"]
