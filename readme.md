# Pastebin Crawler

### How to run
```shell
git clone git@github.com:mikeler216/pastebin_crawler.git {somedir}
cd {somedir}
```
cd into repository 

1. To run test:
```shell
docker-compose -f dev-docker-compose.yaml build
docker-compose -f dev-docker-compose.yaml run web_crawler python -m pytest /app/tests
```
To avoid collisions run done:
```shell
docker-compose down
```

2. To run app
```shell
docker-compose build
docker-compose run web_crawler python /app/create_tables_for_demo.py
docker-compose run web_crawler python /app/main.py
```

To avoid collisions run when done:
```shell
docker-compose down
```
