from flask import Flask
from flask import url_for
from flask import request

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
    return f'''
    <!doctype html> <img src="{url_for('static', filename='c2c17f31b88d4ea800bfe289258d40b8.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
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

                   '''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <input type="password" class="form-control" id="password" placeholder="Введите адрес почты" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас обраование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>нет</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">почему вы хотите полететь?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                     <label for="form-group form-check">Укажите работу</label>
                                    <div class="form-group form-check">

                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">

                                        <label class="form-check-label" for="acceptRules">врач</label>



                                    </div>
                                     <div class="form-group form-check">

                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">

                                        <label class="form-check-label" for="acceptRules">инженер-исследователь</label>



                                    </div>
                                      <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                     <div class="туц">

                                        <input type="checkbox" class="ready?" id="acceptRules" name="accept">

                                        <label class="form-check-label" for="acceptRules">готовы ли вы остаться на марсе?</label>



                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
