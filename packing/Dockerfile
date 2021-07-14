FROM python:3.7
LABEL maintainer="lichanghong <hehuoya@gmail.com>"
MAINTAINER lichanghong
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www/html/packing
COPY . /var/www/html/packing
#RUN apt-get update && \
#pip install -i https://pypi.douban.com/simple/ -r requirements.txt

RUN pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt

ENTRYPOINT ["sh","/var/www/html/packing/start.sh"]
