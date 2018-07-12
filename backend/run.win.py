# -*- encoding: utf-8 -*-
from app import create_app
from app.modules.home.views import homeRoute
from app.modules.users.views import userRoute
from app.modules.articles.views import articleRoute
from app.modules.aidemos.views import aidemoRoute
from app.lab.chatbot.views import chatbotRoute
from app.lab.text.views import textRoute
from app.lab.image.views import imageRoute
from flask_cors import *

DEFAULT_MODULES = [homeRoute,
                   userRoute,
                   aidemoRoute,
                   chatbotRoute,
				   textRoute,
                   imageRoute,
				   articleRoute]

app = create_app('config.py')
CORS(app, supports_credentials=True)

for module in DEFAULT_MODULES:
    app.register_blueprint(module)


@app.before_request
def before_request():
    """
    这里是全局的方法，在请求开始之前调用。
    其中 flask 有个全局的变量 g，它是和 session 一样的用途，可以使用它来保存当前用户的数据
    Returns:

    """
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
