from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
    "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
    "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
    "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
    "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
    "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
    "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."
]

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<a href='/random_fact'>Посмотреть случайный факт!</a><br>" \
           "<a href='/coin'>Подбосить монетку!</a><br>" \
           "<a href='/password'>Генератор паролей!</a>"



@app.route("/random_fact")
def fact():
    return f'<p>{random.choice(facts_list)}</p>'


@app.route("/coin")
def coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "<h1>heads!</h1>" \
            "<img src = 'https://www.shutterstock.com/shutterstock/photos/591846749/display_1500/stock-photo-old-one-euro-coin-heads-with-clipping-path-isolated-on-white-background-crusado-on-white-used-591846749.jpg', width = 450, height = 450>"
    else:
        return "<h1>tails!</h1>" \
            "<img src = 'https://c8.alamy.com/comp/MTPWW4/gold-and-silver-one-euro-coin-germany-MTPWW4.jpg', width = 450, height = 450>"


@app.route("/password")
def password():
    symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    length = 15
    password = ""
    for i in range(length):
        password += random.choice(symbols)
    return f'{password}'





app.run(debug=True)
