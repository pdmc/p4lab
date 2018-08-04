# -*- encoding: utf-8 -*-
#!/usr/bin/python3

import os
import sys
import math
import time

import numpy as np
from flask import render_template, request, json
import tensorflow as tf
from flask import Flask
from flask import render_template, redirect,url_for
from flask import request

import data_utils
import s2s_model

from flask import Flask

def create_aapp():
    app = Flask(__name__)
    return app

application = create_aapp()

tf.app.flags.DEFINE_float(
    'learning_rate',
    0.0003,
    '学习率'
)
tf.app.flags.DEFINE_float(
    'max_gradient_norm',
    5.0,
    '梯度最大阈值'
)
tf.app.flags.DEFINE_float(
    'dropout',
    1.0,
    '每层输出DROPOUT的大小'
)
tf.app.flags.DEFINE_integer(
    'batch_size',
    64,
    '批量梯度下降的批量大小'
)
tf.app.flags.DEFINE_integer(
    'size',
    1024,
    'LSTM每层神经元数量'
)
tf.app.flags.DEFINE_integer(
    'num_layers',
    2,
    'LSTM的层数'
)
tf.app.flags.DEFINE_integer(
    'num_epoch',
    5,
    '训练几轮'
)
tf.app.flags.DEFINE_integer(
    'num_samples',
    512,
    '分批softmax的样本量'
)
tf.app.flags.DEFINE_integer(
    'num_per_epoch',
    1000000,
    '每轮训练多少随机样本'
)
tf.app.flags.DEFINE_string(
    'buckets_dir',
    './bucket_dbs',
    'sqlite3数据库所在文件夹'
)
tf.app.flags.DEFINE_string(
    'model_dir',
    './model/model1',
    '模型保存的目录'
)
tf.app.flags.DEFINE_string(
    'model_name',
    'model',
    '模型保存的名称'
)
tf.app.flags.DEFINE_boolean(
    'use_fp16',
    False,
    '是否使用16位浮点数（默认32位）'
)

FLAGS = tf.app.flags.FLAGS
buckets = data_utils.buckets

def create_model(session, forward_only):
    """建立模型"""
    dtype = tf.float16 if FLAGS.use_fp16 else tf.float32
    model = s2s_model.S2SModel(
        data_utils.dim,
        data_utils.dim,
        buckets,
        FLAGS.size,
        FLAGS.dropout,
        FLAGS.num_layers,
        FLAGS.max_gradient_norm,
        FLAGS.batch_size,
        FLAGS.learning_rate,
        FLAGS.num_samples,
        forward_only,
        dtype
    )
    return model

sess = tf.Session()
#　构建模型
model = create_model(sess, True)
model.batch_size = 1
# 初始化变量
sess.run(tf.initialize_all_variables())
model.saver.restore(sess, os.path.join(FLAGS.model_dir, FLAGS.model_name))


@application.route('/p4bot', methods=['GET', 'POST'])
def abc(model=model, sess=sess):
    error = None
    if request.method == 'POST':
        #sentence = request.json['sentence']
        sentence = request.form['siri']
        print ("----------siri input words ------" + sentence)
        class TestBucket(object):
            def __init__(self, sentence):
                self.sentence = sentence
            def random(self):
                return sentence, ''
        bucket_id = min([
            b for b in range(len(buckets))
            if buckets[b][0] > len(sentence)
        ])
        data, _ = model.get_batch_data(
            {bucket_id: TestBucket(sentence)},
            bucket_id
        )
        encoder_inputs, decoder_inputs, decoder_weights = model.get_batch(
            {bucket_id: TestBucket(sentence)},
            bucket_id,
            data
        )
        _, _, output_logits = model.step(
            sess,
            encoder_inputs,
            decoder_inputs,
            decoder_weights,
            bucket_id,
            True
        )
        outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
        ret = data_utils.indice_sentence(outputs)
        print ("----------p4bot output words ------" + ret)
        return ret
    return render_template('p4bot.html', error=error)


@application.route('/pk4yoRobot', methods=['GET', 'POST'])
def abcd(model=model, sess=sess):
    sentence = '你好啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'
    class TestBucket(object):
        def __init__(self, sentence):
            self.sentence = sentence
        def random(self):
            return sentence, ''
    #print(time.time())
    bucket_id = min([
        b for b in range(len(buckets))
        if buckets[b][0] > len(sentence)
    ])
    #print(time.time())
    data, _ = model.get_batch_data(
        {bucket_id: TestBucket(sentence)},
        bucket_id
    )
    #print(time.time())
    encoder_inputs, decoder_inputs, decoder_weights = model.get_batch(
        {bucket_id: TestBucket(sentence)},
        bucket_id,
        data
    )
    _, _, output_logits = model.step(
        sess,
        encoder_inputs,
        decoder_inputs,
        decoder_weights,
        bucket_id,
        True
    )
    outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
    ret = data_utils.indice_sentence(outputs)
    return ret


@application.route('/home')
def home():
    return render_template('home.html', siri=request.args.get('siri'))

@application.route('/')
def hello_world():
    return "hello world"

def main(_):
    print ("the tensorflow is run")
    

if __name__ == '__main__':
    application.run()
    #np.random.seed(0)
    #tf.set_random_seed(0)
    #app.debug = True
    #app.run('::', 8082)
    #application.run()


