# FROM python:3
# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install --requirement /tmp/requirements.txt
# COPY . /tmp/
# COPY . /app
# CMD python

FROM python:3
# COPY ./requirements.txt /app/requirements.txt

RUN pip install flask
RUN pip install uuid
WORKDIR /app
COPY . .
# ENTRYPOINT [ "python" ]
CMD ["python3","-m", "flask", "run", "--host=0.0.0.0"]