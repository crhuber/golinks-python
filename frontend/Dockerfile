FROM node:10
COPY ./ /app
WORKDIR /app
ARG VUE_APP_API_BASE_URL
ENV VUE_APP_API_BASE_URL $VUE_APP_API_BASE_URL
RUN npm install && npm run build

FROM nginx
RUN mkdir /app
COPY --from=0 /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf