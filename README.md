# Проект:

**Бот для мемов в Телеграм**

## Суть проекта:
Это телеграм бот для создания и работы с мемами. Бот содержит меню с различными функциями, такими как: добавление мема, просмотр всех мемов или мемов в личной коллекции и оценка мемов.

## Функционал:
- пользователь 
- меню
  - добавить мем (фото + текст) 
  - после нажатия диалог с помощью которого можно добавить фото + текст
  - возможность добавить в общую корзину мемов и в личную
  - выбрать рандомный мем из общей
  - оценить лайк или дизлайк
  - выбрать рандомный мем из личной
  - посмотреть свой список мемов
  - выбрать самый популярный

**Требования:**

- Упаковка проекта в докер-компоуз и запуск через docker compose up без дополнительной настройки
- Два формата запуска - через polling и через webhook
- прохождение flake8 + mypy в соответствии с конфигурациями проекта
- Стейт отдельный под каждого пользователя
- Без доступа к бд
- Метрики: 
  - TODO
  - Время выполнения всех интеграционных методов (запросы на бекенд и телеграм)
- Настройки в env
  - Без дублирования кода
- poetry как сборщик пакетов
- Обработка ошибок и соответствующие ответы от бота
- Обработка флуда
- В README.md ожидается увидеть как что работает, чтобы можно было ознакомиться проще с проектом
- Сквозное логирование

---

## 🔧 Запуск проекта

1. Склонируйте этот репозиторий и перейдите в папку с ним

2. Создайте файл `.env` с необходимыми переменными:

```bash
cd conf
ср .env.example .env
```

```env
BOT_TOKEN=токен тг бота
BIND_IP=ip адрес
BIND_PORT=порт
MEM_BACKEND_HOST=адрес бэкенда
REDIS_PASSWORD=пароль редис
LOG_LEVEL=уровень логирования
NGROK_TOKEN=токен сервиса резервирования dns
```

3. Вернитесь в корневую папку и запустите контейнеры:

```bash
docker-compose up
```
---