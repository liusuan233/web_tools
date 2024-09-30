from os.path import exists

from flask import render_template, Blueprint
from app import create_app


app = create_app()
# 主页路由
@app.route('/home')
def home():
    return render_template('home.html')
# 下载页面路由
@app.route('/download')
def download():
    return render_template('download.html')
# 安装过程可能会遇到的问题
@app.route('/faq')
def faq():
    return render_template('faq.html')

# 应用安装指南路由
@app.route('/AppGuide/<string:guide_name>')
def Guide(guide_name):
    if not exists("./templates/AppGuide/"+guide_name+'.html'):
        return render_template('404.html')
    return render_template('AppGuide/'+guide_name+'.html')



if __name__ == '__main__':
    app.run(debug=True,port=6677)