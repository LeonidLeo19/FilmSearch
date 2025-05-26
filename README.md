# FilmSearch — Приложение для поиска фильмов 🎬

## Описание / Description

FilmSearch — это настольное приложение на Python с графическим интерфейсом Tkinter, которое позволяет искать фильмы по жанрам с использованием API The Movie Database (TMDb).  
Приложение отображает популярные фильмы выбранного жанра, показывает описание и даёт ссылку на трейлер. Пример работы в папке "Images"

FilmSearch is a Python desktop application with a Tkinter GUI that enables searching movies by genre using The Movie Database (TMDb) API.  
The app displays popular movies for a selected genre, shows their overview, and provides a link to the trailer. Example output in the "Images" folder

---
## Используемые технологии

- Python — основной язык программирования проекта.  
- Tkinter — библиотека для создания графического интерфейса (GUI).  
- Requests — библиотека для выполнения HTTP-запросов к API.  
- The Movie Database (TMDb) API — внешний API для получения данных о фильмах (жанры, описания, трейлеры).  
- Webbrowser (стандартный модуль Python) — для открытия ссылок на трейлеры в браузере.
## Technologies
- Python — main programming language of the project.  
- Tkinter — library for creating the graphical user interface (GUI).  
- Requests — library for making HTTP requests to APIs.  
- The Movie Database (TMDb) API — external API for movie data (genres, descriptions, trailers).  
- Webbrowser (standard Python module) — to open trailer links in the browser.

---

## Особенности

- Выбор жанра фильма  
- Просмотр популярных фильмов выбранного жанра  
- Отображение описания фильма  
- Возможность открыть трейлер на YouTube
## Features
- Select movie genre  
- Browse popular movies by genre  
- View movie overview  
- Watch trailer on YouTube

---

## Установка / Installation

1. Клонируйте репозиторий:
   git clone https://github.com/yourusername/FilmSearch.git
   cd FilmSearch
   
---
Установите зависимости (если используете виртуальное окружение):
pip install requests

---
Получите API-ключ на TMDb и замените в файле main.py строку:
api_key = 'YourApiKey'
на ваш ключ.

