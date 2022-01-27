FROM python:3.8
RUN mkdir /opt/discordbot
RUN mkdir /opt/etc
COPY . /opt/discordbot
RUN pip install --no-cache-dir -r /opt/discordbot/requirements.txt
VOLUME /opt/etc
WORKDIR /opt/discordbot
CMD ["python3", "./main.py"]
