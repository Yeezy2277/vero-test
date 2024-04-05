# Инструкция по запуску
Для запуска необходим установленный docker и свободный 80 порт(в ином случае указать -p <свой порт>:80). Команда для запуска: 
```sh
docker build --tag <image-name> . 
docker container run -d -p 80:80 --name <container-name> <image-name>
```