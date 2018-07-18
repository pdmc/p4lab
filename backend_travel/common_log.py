# -*- encoding: utf-8 -*- 编码

# 日志模块
import logging

# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s\t%(levelname)s\t%(filename)s\t%(funcName)s\t%(lineno)d\t%(message)s',
                filename='logs/travel.log',
                filemode='a')
#    datefmt='%a %Y-%m-%d %H:%M:%S',

# 创建一个logger
logger = logging.getLogger()

logger.debug('module log __init__')