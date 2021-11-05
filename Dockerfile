FROM python:3.9.7
MAINTAINER G0Yang<ender35841@gmail.com>

WORKDIR /project/upbitAutTrading
COPY ./src/ /project/upbitAutTrading/

#RUN apt-get update -y && apt-get install git nano vim tzdata -y

#RUN npm install -g pm2 node-gyp
#RUN npm install
#RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

#ARG NODE_ENV=production
#ENV NODE_ENV=${NODE_ENV}
# ENV NODE_ENV development

# 프로덕션을 위한 코드를 빌드하는 경우
# RUN npm ci --only=production

# 앱 소스 추가
#COPY . .

# EXPOSE 8000-9000
#EXPOSE 80 443 8080
#CMD [ "pm2-runtime", "start", "ecosystem.config.js", "--env", "production"]
