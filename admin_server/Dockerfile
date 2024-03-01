FROM node:21.2-slim

WORKDIR /usr/src/app

COPY package.json .
COPY yarn.lock .

RUN yarn install

COPY . .

EXPOSE 3001
EXPOSE 50051

CMD ["node", "index.js"]
