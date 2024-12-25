FROM python:3.10.6
WORKDIR /usr/src/app
ADD ./requirements.txt /usr/src/app
ADD ./chage_asg.py /usr/src/app
ADD ./run_py.sh /usr/src/app
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "/bin/bash", "run_py.sh" ]