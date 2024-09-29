from flask import render_template
from app import create_app


app = create_app()

@app.route('/home')
def home():
    return render_template('home.html',title="下载页面")


@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')
if __name__ == '__main__':
    app.run(debug=True,port=6677)