FROM python:3.10
RUN apt-get update
RUN apt-get install -y libglib2.0-0
RUN pip3 install libopencv-dev
COPY requirements.txt app/requirements.txt
COPY . app/
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]