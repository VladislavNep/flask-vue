FROM node:lts-alpine
COPY package*.json ./
RUN npm install
WORKDIR /frontend
COPY . /frontend
RUN npm run build
RUN npm install -g @vue/cli
CMD [ "vue", "ui", "--headless" , "--port", "8000",  "--host", "0.0.0.0" ]
