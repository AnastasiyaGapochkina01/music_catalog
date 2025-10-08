# Задача
Докеризовать приложение, по нашему плану

---

# Music Catalog
Проект состоит из четырех микросервисов:
1. Backend (FastAPI) — REST API музыкального каталога с CRUD операциями по жанрам, исполнителям и альбомам.
2. Admin (Go) — простой сервис-админка (фейковый сервер), отдающий базовые ответы.
3. Nginx — обратный прокси, который проксирует HTTP-запросы на backend.
4. Базы данных postgresql

## Примеры запросов
Добавить жанр 
```bash
curl -X POST http://localhost/genres/ -H "Content-Type: application/json" -d '{"name": "Rock"}'
```
Проверить что добавился
```bash
curl -X GET http://localhost/genres
```
ответ на GET-запрос
```json
[{"name":"Rock","id":1,"artists":[]}]
```

Для агента
```bash
curl http://localhost:8080/
```
ответ
```text
Fake Admin Panel - Hello!
```

или
```bash
curl http://localhost:8080/metrics
```
ответ
```text
metrics: up
```

