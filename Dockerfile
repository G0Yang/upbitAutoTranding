FROM python:3.9.7
MAINTAINER G0Yang<ender35841@gmail.com>

WORKDIR /project/upbitAutTrading
COPY ./src/ /project/upbitAutTrading/

#RUN python -m venv venv

#RUN source ./venv/bin/activate

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "runServer.py" ]

