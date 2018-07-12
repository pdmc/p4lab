# -*- encoding: utf-8 -*-

import json
import requests
import time
import os

# AI模块
import jieba
import pytesseract
from PIL import Image
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# 用户登录模块
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
#from config import basedir
from tenacity import retry


#import zutil
import p4utils
# generateP4ID()

# 日志模块
import logging

# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s:%(lineno)d:%(funcName)s %(process)d:%(thread)d %(levelname)s %(message)s',
                filename='log.log',
                filemode='a')
#    datefmt='%a %Y-%m-%d %H:%M:%S',
                
logging.debug('This is debug message')


app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def index():
    # 主页面
    return render_template("main.html")

#@retry
@app.route('/inp4bot', methods=['POST', 'GET'])
def p4bot_api_in():
    print "enter /inp4bot: p4bot_api_in() "
    fd=open('log.log','a')
    if request.method == 'GET':
        #print request.args
        #return '{"code": 1003, "text": "%s" }' % ("请求方法错误")
        try:
            sentence = request.args['siri']
        except KeyError :
            end = '{"code": 1001, "text": "%s" }' % ("错误的请求KEY")
            return "successCallback"+"("+json.loads(json.dumps(end))+")"	# 为了响应jsonp，加壳
        print("------用户输入------", sentence)
        if sentence.strip() =='':
            end = '{"code": 1002, "text": "%s" }' % ("请求的VALUE为空")
            return "successCallback"+"("+json.loads(json.dumps(end))+")"
        else:
            user_info = {'key': "b186cf11be824847bd4cd59e61cc91e9", 'info': sentence, 'userid': 'wangjipeng121'}
            headers = {'content-type': 'application/json'}
            r = requests.post("http://www.tuling123.com/openapi/api", data=json.dumps(user_info), headers=headers)
            r_json = r.json()
            if r_json["code"]==100000:
                end = '{"code": 1000, "text": "%s" }' %(r_json["text"])
                fd.write("logloglog")
                fd.close()
                return "successCallback"+"("+json.loads(json.dumps(end))+")"
                    #end
            else:
                new_str = str(r_json["text"]).replace('已帮你找到', '小p4bot给您推荐的').replace('价格信息','').replace('亲', '主人')
                end = '{"code": 1000, "text": "%s" }' % (new_str + " 👉👉👉"+r_json["url"])
                return "successCallback"+"("+json.loads(json.dumps(end))+")"
                # return new_str + " 👉👉👉"+r_json["url"]
    end = '{"code": 1003, "text": "%s" }' % ("请求方法错误")
    return "successCallback"+"("+json.loads(json.dumps(end))+")" 	#"


@app.route('/partciple', methods=['POST', 'GET'])
def p4bot_fenci():
    print('fenci -=-=-=-=-=-=-=-=')
    error = None
    if request.method == 'POST':
        sentence = request.form['siri'].strip()
        if sentence =='':
            return '空白输入'
        else:
            seg_list = jieba.cut(sentence, cut_all=False)
            end_str = "/ ".join(seg_list)
            return end_str
    return render_template('index.html', error=error)	# '


@app.route('/inpartciple', methods=['POST', 'GET'])
def p4bot_fenci_in():
    print('fenci -=-=-=-=-=-=-=-=')
    if request.method == 'POST':
        try:
            sentence = request.json['sentence']
        except KeyError :
            end = '{"code": 1001, "text": "%s" }' % ("错误的请求KEY")
            return json.loads(json.dumps(end))
        if sentence.strip() =='':
            end = '{"code": 1002, "text": "%s" }' % ("请求的VALUE为空")
            return json.loads(json.dumps(end))
        else:
            seg_list = jieba.cut(sentence, cut_all=False)
            end_str = "/ ".join(seg_list)
            end = '{"code": 1000, "text": "%s" }' % (end_str)
            return json.loads(json.dumps(end))
    end = '{"code": 1003, "text": "%s" }' % ("请求方法错误")
    return json.loads(json.dumps(end))		# "


@app.route('/ocr', methods=['POST', 'GET'])
def p4bot_load():
    print('opopopopopopopopopopopopop')
    error = None
    if request.method == 'POST':
        pic_time = time.time()
        upload_file = request.files.get("file")
        if upload_file and allowed_file(upload_file.filename):
            save_filename = "./picture/" + str(pic_time).replace('.', '') + secure_filename(upload_file.filename)
            upload_file.save(save_filename)
            image = Image.open(save_filename)
            image.load()
            vcode = pytesseract.image_to_string(image,  lang='chi_sim+eng')
            return (vcode)
        # file.save('/Users/wangjipeng/PycharmProjects/mobile/templates/'+str(pic_time)+file.filename)
        else:
            end = '{"code": 1004, "text": "%s" }' % ("请求的VALUE格式错误")
            return end
    return render_template('index.html', error=error)	# 格式补偿"


@app.route('/inocr', methods=['POST', 'GET'])
def p4bot_load_in():
    if request.method == 'POST':
        pic_time = time.time()
        try:
            upload_file =  request.files['picture']
        except KeyError:
            end = '{"code": 1001, "text": "%s" }' % ("错误的请求KEY")
            return json.loads(json.dumps(end))
        if upload_file and allowed_file(upload_file.filename):
            save_filename = "/opt/software/P4LIB/picture/" + str(pic_time).replace('.', '') + secure_filename(upload_file.filename)
            upload_file.save(save_filename)
            image = Image.open(save_filename)
            image.load()
            vcode = pytesseract.image_to_string(image,  lang='chi_sim+eng')
            end = '{"code": 1000, "text": "%s" }' % (vcode)
            return json.loads(json.dumps(end))
        else:
            end = '{"code": 1004, "text": "%s" }' % ("请求的VALUE格式错误")
            return json.loads(json.dumps(end))
    end = '{"code": 1003, "text": "%s" }' % ("请求方法错误")
    return json.loads(json.dump(end))



if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=8080)
