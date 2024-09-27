from flask import render_template
from app import create_app


app = create_app()
@app.doc()
@app.route('/')
def home():
    return render_template('index.html',title="下载页面")


@app.route('/download')
def download():
    return render_template('download.html')



if __name__ == '__main__':
    app.run(debug=True,port=6677)