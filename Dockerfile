FROM node:12 as npmdepedencies
WORKDIR /app
COPY package*.json .
RUN npm install

FROM gcr.io/distroless/nodejs:12
COPY --from=npmdepedencies /app/node_modules /app/node_modules
WORKDIR /app

FROM python:3.10-slim-buster as build
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-slim-buster 
COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY --from=build /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY . /app
WORKDIR /app

USER 1000

