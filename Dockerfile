# Using official python runtime base image
FROM centos:centos7

RUN yum install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install ./google-chrome-stable_current_x86_64.rpm -y
RUN yum install python3 -y
RUN yum install python3-pip -y

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app

# Define our command to be run when launching the container
CMD ["python3", "make_swimming_reservation.py"]