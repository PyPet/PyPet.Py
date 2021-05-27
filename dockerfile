FROM python:3.8.3-slim-buster

ENV TINI_VERSION="v0.19.0"

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini

RUN chmod +x /tini

RUN pip install -U \
    pip \
    setuptools \
    wheel

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/tini", "--"]