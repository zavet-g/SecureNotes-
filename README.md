# SecureNotes-

**SecureNotes** — это простое приложение для безопасного хранения заметок с системой регистрации и авторизации пользователей. Приложение использует Flask для серверной логики, SQLAlchemy для работы с базой данных и Flask-Login для аутентификации.

## Описание

Это приложение позволяет пользователям:

- Регистрироваться с уникальным логином и паролем.
- Входить в систему через авторизацию с кодовым словом.
- Добавлять, просматривать и удалять свои заметки.
- Использовать безопасное хранение паролей с помощью Flask-Bcrypt.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/SecureNotes-.git
   cd SecureNotes-

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt

3. Настройте базу данных. В проекте используется SQLite, для этого выполните команду:

   ```bash
   python db_init.py

4. Запустите приложение:

   ```bash
   python app.py


## Структура проекта

   ```csharp
   SecureNotes/
│
├── app.py                # Основной файл приложения с роутами и логикой
├── config.py             # Конфигурация проекта (например, URI базы данных, секретный ключ)
├── db_init.py            # Инициализация базы данных
├── models.py             # Модели базы данных (User и Note)
├── requirements.txt      # Зависимости проекта
├── static/               # Статические файлы (CSS, изображения и т.д.)
│   └── styles.css        # Основной файл стилей
└── templates/            # Шаблоны HTML для отображения данных
    ├── home.html         # Страница входа
    ├── register.html     # Страница регистрации
    ├── code.html         # Страница для ввода кодового слова
    ├── notes.html        # Страница со списком заметок
    ├── add_note.html     # Страница для добавления новой заметки
    └── error.html        # Страница ошибки при вводе кодового слова
   ```


## Функции

- Регистрация: Пользователи могут зарегистрироваться, создав уникальное имя пользователя и пароль.
- Вход в систему: Пользователи могут войти в систему, введя свой логин и пароль. Для дополнительной безопасности используется кодовое слово.
- Заметки: Пользователи могут добавлять, просматривать и удалять свои заметки.
- Безопасность: Пароли пользователей шифруются с помощью Flask-Bcrypt, а данные о пользователях защищены с использованием Flask-Login. 

## Используемые технологии

- Flask: Микрофреймворк для создания веб-приложений.
- SQLAlchemy: ORM для работы с базой данных.
- Flask-Login: Расширение для управления аутентификацией пользователей.
- Flask-Bcrypt: Для безопасного хеширования паролей.
- SQLite: Легковесная база данных для хранения данных приложения.


## Развертывание на сервере
- Для развертывания приложения на сервере:

1. Настройте сервер с Python и установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Используйте команду для запуска приложения на сервере:

   ```bash
   python app.py
   ```

# Возможные улучшения проекта

Хотя проект NoteKeeper уже функционален, есть несколько областей, где его можно улучшить. В данном разделе мы рассмотрим возможные улучшения и дополнения, которые могут улучшить производительность, безопасность и функциональность приложения.

## 1. Улучшение безопасности

### Защита от атак CSRF (Cross-Site Request Forgery)
Для предотвращения атак CSRF можно добавить защиту с помощью Flask-WTF. Это расширение предоставляет функциональность для добавления токенов CSRF в формы, что защитит приложение от злонамеренных запросов.

Рекомендуемое решение:
- Установить Flask-WTF и добавить форму с CSRF защитой.

### Ограничение по количеству попыток входа
Для улучшения безопасности приложения, можно реализовать ограничение количества попыток входа (rate-limiting), чтобы предотвратить атаки методом подбора пароля.

Рекомендуемое решение:
- Использовать Flask-Limiter для ограничения числа попыток входа с одного IP-адреса.

## 2. Реализация восстановления пароля

На данный момент приложение не поддерживает функциональность восстановления пароля. Добавление этой функции поможет улучшить пользовательский опыт и повысить безопасность.

Рекомендуемое решение:
- Реализовать механизм восстановления пароля через email с помощью Flask-Mail.
- Использовать временные токены для сброса пароля.

## 3. Улучшение пользовательского интерфейса (UI)

### Добавление валидации на стороне клиента
На текущий момент форма регистрации и входа не имеет валидации на стороне клиента. Это можно исправить с помощью JavaScript и HTML5-валидаторов.

Рекомендуемое решение:
- Добавить валидацию на стороне клиента с помощью JavaScript (например, проверка на наличие пробелов в логине или пароле, обязательные поля и т. д.).

### Улучшение дизайна
Хотя проект имеет базовый стиль, интерфейс можно сделать более современным и удобным. Можно использовать библиотеки, такие как Bootstrap или Materialize, для улучшения внешнего вида.

Рекомендуемое решение:
- Перейти на использование Bootstrap или другой CSS-библиотеки для создания более отзывчивого интерфейса.

## 4. Поддержка нескольких пользователей

На данный момент приложение позволяет только одному пользователю работать с заметками. Для улучшения функциональности можно добавить возможность делиться заметками с другими пользователями или создавать групповые заметки.

Рекомендуемое решение:
- Добавить таблицу для совместного использования заметок (например, через связь многие ко многим) между пользователями.
- Реализовать возможность приглашать других пользователей в заметки.

## 5. Миграции базы данных

Использование Alembic для управления миграциями базы данных позволит легче обновлять структуру базы данных при изменении модели.

Рекомендуемое решение:
- Интегрировать Alembic с проектом для управления миграциями.

## 6. Логирование и мониторинг

Хотя в проекте уже есть базовые сообщения в логах, можно добавить более подробное логирование ошибок и мониторинг активности пользователей.

Рекомендуемое решение:
- Использовать Flask-Logging для детализированного логирования.
- Интегрировать проект с системой мониторинга, например, Sentry или Prometheus.

## 7. Тестирование приложения

Для повышения надежности приложения, можно добавить юнит-тесты с использованием Flask-Testing или Pytest. Это поможет избежать ошибок при внесении изменений в код и улучшить поддерживаемость проекта.

Рекомендуемое решение:
- Написать юнит-тесты для различных частей приложения, например, для проверки функционала регистрации, входа и работы с заметками.

## 8. Документация API

Если в будущем приложение будет расширяться и поддерживать API, важно добавить документацию с примерами использования.

Рекомендуемое решение:
- Использовать библиотеки, такие как Flask-RESTful или Flask-OpenAPI, для создания API и документации для внешних разработчиков.

## 9. Использование другой базы данных

Для улучшения производительности и масштабируемости приложения можно перейти на более мощную базу данных, такую как PostgreSQL или MySQL, вместо SQLite.

Рекомендуемое решение:
- Переключиться на PostgreSQL или MySQL, чтобы приложение могло эффективно работать с большим количеством данных.

## 10. Аутентификация через сторонние сервисы

Вместо традиционной регистрации и входа с использованием логина и пароля, можно добавить возможность аутентификации через сторонние сервисы, такие как Google или GitHub.

Рекомендуемое решение:
- Интегрировать OAuth2 для аутентификации через популярные сервисы.

---

Эти улучшения помогут сделать проект более безопасным, удобным и функциональным, а также подготовят его к более широкому использованию в будущем.

