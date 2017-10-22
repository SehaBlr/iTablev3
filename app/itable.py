from flask import Flask, render_template, request, escape


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('index.html',
                           the_title='Выбор языка')

@app.route('/mainmenu')
def menu() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('mainmenu.html',
                           the_title='Меню')


@app.route('/buklet')
def buklet() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('buklet.html',
                           the_title='Буклет')

@app.route('/video')
def video() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('video.html',
                           the_title='Видео')

if __name__ == '__main__':
    app.run(debug=True)