FROM amazonlinux:2.0.20200602.0

RUN yum update -y \
    && yum install -y \
        python3-pip \
        zip \
    && yum -y clean all

RUN python3.7 -m pip install --upgrade pip