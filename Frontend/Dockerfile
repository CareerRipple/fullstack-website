FROM node:20-alpine

WORKDIR /app

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install

COPY . .

#RUN nom run build

CMD [ "npm", "run", "build" ]