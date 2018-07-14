# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import sys
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if p not in sys.path:
    sys.path.append(p)
import tensorflow as tf
from tensorflow.contrib import learn
import numpy as np
import aiml
import json
import requests

reload(sys)
sys.setdefaultencoding('utf-8')
