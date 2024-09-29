from flask import render_template
from app import create_app


app = create_app()
# 主页路由
@app.route('/home')
def home():
    return render_template('home.html',title="下载页面")
# 下载页面路由
@app.route('/download')
def download():
    return render_template('download.html')
# 安装过程可能会遇到的问题
@app.route('/faq')
def faq():
    return render_template('faq.html')
# python的使用指南路由
@app.route('/PythonGuide')
def PythonGuide():
    return render_template('AppGuide/PythonGuide.html')

if __name__ == '__main__':
    app.run(debug=True,port=6677)