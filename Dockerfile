FROM python:3.6.5
LABEL maintainer chris
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
ADD . /docker_api
RUN pip install -i https://pypi.douban.com/simple --upgrade pip
RUN  pip install -i https://pypi.douban.com/simple -r requirements.txt

RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]


