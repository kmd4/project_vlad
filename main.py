from dotenv import load_dotenv
from flask import Flask, redirect, render_template
from data import db_session
from data.users import User
from data.messages import News
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user
from mail import send_email


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        s = check_password(form.password.data)
        if s != True:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message=s)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        send_email('mdku2005@gmail.com')
        user = User(
            name=form.name.data,
            about=form.about.data,
            email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            print(1)
            return redirect('/blog')
        print(2)
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)

    return render_template('login.html', title='Авторизация', form=form)


@app.route('/blog', methods=['GET', 'POST'])
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


def check_password(pas):
    if len(pas) < 8: return 'Пароль слишком короткий'
    if pas.isdigit() or pas.isalpha(): return 'Пароль слишком простой. Надежный пароль содержит латинские буквы и цифры'
    return True

if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
