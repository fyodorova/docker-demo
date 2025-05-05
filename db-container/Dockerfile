FROM alpine:latest 
RUN apk add --no-cache sqlite 
WORKDIR /data 
VOLUME /data 
RUN sqlite3 mydata.db "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, txt TEXT);" 
CMD ["sh", "-c", "while true; do sleep 3600; done"] 
