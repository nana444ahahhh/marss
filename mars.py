from flask import Flask
from flask import url_for

app = Flask(__name__)

i = 0


@app.route('/')
def slash():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promote():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>девиз марса!</title>
                      </head>
                      <body>
                        <h1>Человечество вырастает из детства.</h1>
                        <h1>Человечеству мала одна планета.</h1>
                        <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                        <h1>И начнем с Марса!</h1>
                        <h1>Присоединяйся!</h1>
                        
                      </body>
                    </html>"""

@app.route('/image_sample')
def image():

    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>марсианский пейзаж</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <
                        
                      </body>
                    </html>
    <img src="{url_for('static', filename='c2c17f31b88d4ea800bfe289258d40b8.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
