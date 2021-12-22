FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p "/projects/django/shop"

WORKDIR "/projects/django/shop"

COPY . "/projects/django/shop"

RUN pip install -r requirments.txt

EXPOSE 8000

