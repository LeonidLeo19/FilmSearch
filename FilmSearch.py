import tkinter as tk
import webbrowser
import requests

api_key = 'YourApiKey'
url = "https://api.themoviedb.org/3/discover/movie"

# 🎨 Цветовая схема
BG_COLOR = "#1e1e2f"
BTN_COLOR = "#3e8e7e"
BTN_TEXT = "#ffffff"
LABEL_COLOR = "#ffffff"
OVERVIEW_BG = "#2a2a3f"
OVERVIEW_TEXT = "#ffffff"

def open_trailer(key):
    webbrowser.open(f'https://www.youtube.com/watch?v={key}')

def Film_page(data):
    n = 0
    films = {}
    film_names = []
    video_id = []

    for movie in data[:10]:
        video_id.append(movie['id'])
        films[movie['title']] = movie['overview']
        film_names.append(movie['title'])

    def prev_movie():
        nonlocal n
        n -= 1
        film_window.title(film_names[n])
        next_button.place(x=320, y=500)
        nameLab.config(text=film_names[n])
        overviewLab.config(text=films[film_names[n]])
        update_trailer()
        if n <= 0:
            prev_button.place_forget()

    def next_movie():
        nonlocal n
        n += 1
        film_window.title(film_names[n])
        nameLab.config(text=film_names[n])
        overviewLab.config(text=films[film_names[n]])
        prev_button.place(x=220, y=500)
        update_trailer()
        if n == 9:
            next_button.place_forget()

    def update_trailer():
        url_trail = f"https://api.themoviedb.org/3/movie/{video_id[n]}/videos?api_key={api_key}"
        response_link = requests.get(url_trail)
        data_link = response_link.json()
        if data_link.get("results"):
            key = data_link["results"][0]["key"]
            ytb_link.config(command=lambda key=key: open_trailer(key))
            ytb_link.config(state="normal", text="Смотреть трейлер")
        else:
            ytb_link.config(state="disabled", text="Трейлер недоступен")

    film_window = tk.Toplevel()
    film_window.title(film_names[n])
    film_window.geometry("620x550")
    film_window.resizable(False, False)
    film_window.configure(bg=BG_COLOR)

    nameLab = tk.Label(film_window, text=film_names[n], font=("Arial", 16, "bold"),
                       bg=BG_COLOR, fg=LABEL_COLOR)
    nameLab.place(x=310, y=30, anchor="n")

    overviewLab = tk.Label(film_window, text=films[film_names[n]], wraplength=580, justify="left",
                           bg=OVERVIEW_BG, fg=OVERVIEW_TEXT, font=("Arial", 12), padx=10, pady=10)
    overviewLab.place(x=10, y=80)

    prev_button = tk.Button(film_window, text='Предыдущий', command=prev_movie,
                            bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 10), relief="flat")
    prev_button.place_forget()

    next_button = tk.Button(film_window, text='Следующий', command=next_movie,
                            bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 10), relief="flat")
    next_button.place(x=320, y=500)

    url_trail = f"https://api.themoviedb.org/3/movie/{video_id[n]}/videos?api_key={api_key}"
    response_link = requests.get(url_trail)
    data_link = response_link.json()

    if data_link.get("results"):
        key = data_link["results"][0]["key"]
        ytb_link = tk.Button(film_window, text="Смотреть трейлер", command=lambda key=key: open_trailer(key),
                             bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 10), relief="flat")
    else:
        ytb_link = tk.Button(film_window, text="Трейлер недоступен", state="disabled",
                             bg=BTN_COLOR, fg=BTN_TEXT, font=("Arial", 10), relief="flat")

    ytb_link.place(x=257, y=450)

def Search(genre: int):
    params = {
        "api_key": api_key,
        "with_genres": genre,
        "sort_by": "popularity.desc",
        "language": "ru",
        "page": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    Film_page(data['results'])

# Главное окно
window = tk.Tk()
window.title("FilmSearch")
window.geometry("620x550")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

Genres = {
    "Боевик": 28, "Приключения": 12, "Мультфильм": 16, "Комедия": 35, "Криминал": 80,
    "Документальный": 99, "Драма": 18, "Семейный": 10751, "Фэнтези": 14, "История": 36,
    "Ужасы": 27, "Музыка": 10402, "Детектив": 9648, "Мелодрама": 10749,
    "Фантастика": 878, "Телевизионный фильм": 10770, "Триллер": 53, "Военный": 10572, "Вестерн": 37,}

buttons = {}
n = 0
for name in Genres:
    gen_code = Genres[name]
    button = tk.Button(text=name, width=17, height=2,
                       bg=BTN_COLOR, fg=BTN_TEXT, relief="flat",
                       font=("Arial", 10),
                       command=lambda gen_code=gen_code: Search(gen_code))
    buttons[n] = button
    n += 1

xo, yo = 10, 50
counter = 0
for el in buttons:
    buttons[el].place(x=xo, y=yo)
    counter += 1
    xo += 150
    if counter >= 4:
        counter = 0
        yo += 100
        xo = 10

window.mainloop()
