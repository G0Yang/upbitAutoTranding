FROM python:3.9.7
MAINTAINER G0Yang<ender35841@gmail.com>

WORKDIR /project/upbitAutTrading

COPY ./src/ /project/upbitAutTrading/

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "runServer.py" ]

