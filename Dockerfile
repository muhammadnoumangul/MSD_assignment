From python:3.11

ADD main.py .
ADD EC2.txt .

RUN pip install Counter

CMD [ "python", "./main.py"]
