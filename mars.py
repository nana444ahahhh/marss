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


@app.route('/promotion_image')
def promimage():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                       <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Привет, Яндекс!</h1>
                        <div class="alert alert-primary" role="alert">
                         Переезжайте на марс
                        </div>
                        <div class="alert alert-success" role="alert">
                          там лучше чем на земле
                        </div>
                        <div class="alert alert-danger" role="alert">
                          тут весело жить
                        </div>
                        <div class="alert alert-info" role="alert">
                          легче зарабатывать
                        </div>
                        <div class="alert alert-dark" role="alert">
                          ты будешь Богаче!
                        </div>
                      </body>
                    </html>
                    
                    <img src="{url_for('static', filename='c2c17f31b88d4ea800bfe289258d40b8.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
