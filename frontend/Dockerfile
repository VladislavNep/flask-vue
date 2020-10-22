FROM node:lts-alpine
RUN npm install -g @vue/cli
COPY package*.json ./
RUN npm install
COPY . /frontend
RUN npm run build
CMD [ "vue", "ui", "--headless" , "--port", "8000",  "--host", "0.0.0.0" ]
