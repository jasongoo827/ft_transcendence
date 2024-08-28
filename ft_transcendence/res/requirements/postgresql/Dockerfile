FROM postgres:16-alpine

# 환경 변수 설정
ENV POSTGRES_PASSWORD=password
ENV DB_NAME=mydatabase
ENV DB_USER=mkong
ENV DB_USER_PASSWORD=password

# 초기화 스크립트 추가
COPY init.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init.sh

EXPOSE 5432