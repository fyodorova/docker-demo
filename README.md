# docker-demo
A network of 2 Docker containers: one hosts the DB, other is entry point
 
\`\`\`bash 
docker-compose up --build -d 
\`\`\` 
 
\`\`\`bash 
docker logs sqlite-client 
\`\`\` 
 
\`\`\`bash 
docker-compose down 
docker-compose up -d 
docker logs sqlite-client 
\`\`\` 
 
- db-container/ - база данных SQLite 
- app-container/ - клиент для записи/чтения
- docker-compose.yml - сборка и сеть
