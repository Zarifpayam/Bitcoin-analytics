FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get install -y \
    libhdf5-dev cython3 python3 python3-numpy python3-nose python3-pandas python-h5py \
    python python-numpy python-nose python-pandas python3-h5py python3-pip vim jq curl

RUN pip3 install --upgrade setuptools pip
RUN pip3 install -U scikit-learn scipy matplotlib numpy

RUN echo 'export PS1="aidin-starter# "' >> /root/.bashrc

WORKDIR /src

#RUN pip install --no-cache-dir -r requirements.txt

