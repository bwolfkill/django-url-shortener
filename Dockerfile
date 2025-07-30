FROM python:3.13.5

WORKDIR /url_project

COPY . /url_project/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]