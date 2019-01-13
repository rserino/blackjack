FROM node:8

WORKDIR /usr/src/app

COPY . . 
# package*.json ./

RUN npm install
# If building code for prod, RUN npm install --only=production

COPY . .

EXPOSE 5000

CMD [ "npm", "run", "start" ]