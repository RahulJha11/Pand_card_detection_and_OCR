FROM python:3.10
COPY requirements.txt app/requirements.txt
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["streamlit_app.py"]