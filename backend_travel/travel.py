# -*- coding: utf-8 -*-

import time
import json

from aip import AipSpeech
from flask import Flask, request, Response, render_template
from werkzeug.utils import secure_filename
from cnn_pre import run  as  cnn
from common_log import  logger


app = Flask(__name__)

# 百度语音
APP_ID = '********'
API_KEY = '**********'
SECRET_KEY = '*******'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 语音
@app.route('/travelv',  methods=['POST', 'GET'])
def travelvoice():
    error = 'post'
    logger.debug("Enter /travelv: travelvoice()")
    if request.method == 'POST':
        upload_file = request.files.get("file")
        flag_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        save_filename = "/opt/software/p4lab/p4lab/backend_travel/voice_data/" + secure_filename(upload_file.filename) + str(flag_time) + '.wav'
        upload_file.save(save_filename)
        logger.debug("Save voice " + str(flag_time) + ".wav  is ok" )
        baidu_result = client.asr(get_file_content(save_filename), 'wav', 16000, {
            'lan': 'zh',
        })
        if baidu_result['err_no'] == 0:
            baidu_re = str(baidu_result['result'][0]).replace('，', '')
            logger.debug("baidu_voice return is " + baidu_re)
            baidu_str = cnn(baidu_re)
            logger.debug("cnn_travel return is " + baidu_str)
            end = '{"code": 1000, "text": "%s"}' % (baidu_str)
            result_json = json.loads(json.dumps(end))
            resp = Response(result_json)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            logger.debug("Out /travelv: travelvoice() is ok")
            return resp
        else:
            baidu_str = '语音解析失败'
            end = '{"code": 1000, "text": "%s"}' % (baidu_str)
            logger.debug("baidu_voice return is bad")
            result_json = json.loads(json.dumps(end))
            resp = Response(result_json)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
    return render_template('index.html', error=error)


# 文字
@app.route('/travels',  methods=['POST', 'GET'])
def travelstr():
    logger.debug("Enter /travels: travelstr()")
    error = 'post'
    if request.method == 'GET':
        voice_uncode = request.args['siri']
        voice_str = str(voice_uncode)
        logger.debug("receive str is " + voice_str)
        cnn_re = cnn(voice_str)
        logger.debug("cnn_travel return is " + cnn_re)
        end = '{"code": 1000, "text": "%s" }' %(cnn_re)
        return "successCallback"+"("+json.loads(json.dumps(end))+")"
    end = '{"code": 1000, "text": "%s" }' %('error')
    return "successCallback"+"("+json.loads(json.dumps(end))+")"


if __name__ == '__main__':
#    app.run(host="192.168.8.100", port=8080)
    app.run(debug=True, ssl_context=(
        "/etc/httpd/****.crt",
        "/etc/httpd/****.key")
    )
