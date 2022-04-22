FROM node:16

RUN apt update \
  && apt install -y --no-install-recommends \
    libasound2 \
    libatk1.0 \
    libatk-bridge2.0 \
    libdrm-common \
    libgbm1 \
    libgtk-3-bin \
    libnss3 \
    xauth \
    xvfb

WORKDIR /app
COPY package*.json ./
RUN npm i
COPY . .
RUN xvfb-run -a npm start
