From centos:latest
COPY salary.pk1  /root/
COPY main.py /root/
RUN yum install python36 -y\
    && yum install /usr/bin/clear  -y \
    && pip3 install scikit-learn -q
CMD ["python3", "/root/main.py"]
