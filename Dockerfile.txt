FROM python:3.11
WORKDIR /
COPY choisir_restaurant.py .
RUN python choisir_restaurant.py