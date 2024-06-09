## Проект:

Бот для мемов

**Суть проекта:**
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