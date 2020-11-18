FROM python:3.8-slim

WORKDIR /bot

COPY ./requirements.txt .
RUN apt-get update\
    && apt-get upgrade gcc -y\
    && pip install --upgrade pip\
    && pip install -r requirements.txt\
    && rm requirements.txt\
    && mkdir ./cogs\
    && mkdir ./tc_pc_scan

COPY ./cogs/* ./cogs/
COPY ./tc_pc_scan/scan_rooms.py ./tc_pc_scan/scan_rooms.py
COPY ./tc_pc_scan/__init__.py ./tc_pc_scan/__init__.py
COPY ./bot.py .
COPY ./start.py .

CMD ["python", "start.py"]