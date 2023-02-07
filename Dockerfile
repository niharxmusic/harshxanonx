FROM  Debian:11
Run apt-get update 
Run apt-get install python3-pip -y
COPY ..
Run pip3 install  -U -r -requriments.txt
CMD python3 main.py
