FROM debian:jessie

RUN apt-get update
RUN apt-get install -y \
	python-dev \
	python-pip \
	&& apt-get clean

COPY src/ /opt/test_app

WORKDIR /opt/test_app
RUN python setup.py install

CMD ['/usr/local/bin/run_whoami']