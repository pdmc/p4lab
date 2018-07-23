# -*- coding:utf-8 -*-
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 时间
# input_time_dir = '/Users/wangjipeng/Desktop/tour_corpus/时间'
# output_time_dir = '/Users/wangjipeng/Git_stu/machine_learning/data/sohu_news_segment_data/时间/'
# jieba.add_word('什么时候', 200)
# jieba.add_word('开始营业', 200)
# jieba.add_word('开到', 200)
# jieba.add_word('最晚', 200)
# jieba.add_word('24小时', 200)
# jieba.add_word('几点开门', 200)
# jieba.add_word('几点关门', 200)
# jieba.add_word('什么时候关门', 200)
#
# with open(input_time_dir, 'r') as reader:
#     int = 1800
#     for line in reader.readlines():
#         one_line = line.replace('\n', '')
#         jieba_line = jieba.cut(one_line)
#         write_line =  ' '.join(jieba_line)
#         # print (write_line)
#         new_output = output_time_dir + str(int) + '.txt'
#         with open(new_output, 'a+') as write:
#             write.write(write_line)
#         int +=1




#   票价的分词，文件保存
# input_time_dir = '/Users/wangjipeng/Desktop/票价'
# output_time_dir = '/Users/wangjipeng/Git_stu/machine_learning/data/sohu_news_segment_data/票价/'
# jieba.add_word('多少钱', 200)
# jieba.add_word('是多少', 200)
# jieba.add_word('成人票', 200)
# jieba.add_word('什么价格', 200)
# jieba.add_word('上班日', 200)
# jieba.add_word('季度票', 200)
# jieba.add_word('怎么卖', 200)
# jieba.add_word('小孩票', 200)
# jieba.add_word('大人票', 200)
# jieba.add_word('毛爷爷', 200)
#
# with open(input_time_dir, 'r') as reader:
#     int = 900
#     for line in reader.readlines():
#         one_line = line.replace('\n', '')
#         jieba_line = jieba.cut(one_line)
#         write_line =  ' '.join(jieba_line)
#         new_output = output_time_dir + str(int) + '.txt'
#         with open(new_output, 'a+') as write:
#             write.write(write_line)
#         int +=1



# 小卖店
# input_time_dir = '/Users/wangjipeng/Desktop/小卖店'
# output_time_dir = '/Users/wangjipeng/Git_stu/machine_learning/data/sohu_news_segment_data/小卖店/'
# jieba.add_word('怎么走', 200)
# jieba.add_word('小卖店在哪里', 200)
# jieba.add_word('小卖店怎么走', 200)
# jieba.add_word('商店在哪里', 200)
# jieba.add_word('商店怎么走', 200)
# jieba.add_word('买点吃的', 200)
# jieba.add_word('我渴了', 200)
# jieba.add_word('我饿了', 200)
# jieba.add_word('想买', 200)
# jieba.add_word('想吃', 200)
# jieba.add_word('想喝', 200)
# jieba.add_word('自拍杆', 200)
# jieba.add_word('小卖店', 200)
# jieba.add_word('小卖铺', 200)
# jieba.add_word('好吃的', 200)
# jieba.add_word('想吃点东西', 200)
# jieba.add_word('小卖店在什么地方', 200)
# jieba.add_word('在哪里能买到', 200)
#
# with open(input_time_dir, 'r') as reader:
#     int =1000
#     for line in reader.readlines():
#         one_line = line.replace('\n', '')
#         jieba_line = jieba.cut(one_line)
#         write_line =  ' '.join(jieba_line)
#         # print (write_line)
#         new_output = output_time_dir + str(int) + '.txt'
#         with open(new_output, 'a+') as write:
#             write.write(write_line)
#         int +=1



# 卫生间
# input_time_dir = '/Users/wangjipeng/Desktop/tour_corpus/卫生间'
# output_time_dir = '/Users/wangjipeng/Git_stu/machine_learning/data/sohu_news_segment_data/卫生间/'
# jieba.add_word('厕所在什么地方', 200)
# jieba.add_word('女厕所在什么地方', 200)
# jieba.add_word('男厕所在什么地方', 200)
# jieba.add_word('卫生间怎么走', 200)
# jieba.add_word('卫生间在哪', 200)
# jieba.add_word('厕所在哪', 200)
# jieba.add_word('洗手间在哪', 200)
# jieba.add_word('卫生间在哪里', 200)
# jieba.add_word('厕所在哪里', 200)
# jieba.add_word('洗手间在哪里', 200)
# jieba.add_word('我想去厕所', 200)
#
#
# with open(input_time_dir, 'r') as reader:
#     int = 1600
#     for line in reader.readlines():
#         one_line = line.replace('\n', '')
#         jieba_line = jieba.cut(one_line)
#         write_line =  ' '.join(jieba_line)
#         # print (write_line)
#         new_output = output_time_dir + str(int) + '.txt'
#         with open(new_output, 'a+') as write:
#             write.write(write_line)
#         int +=1



# 闲聊
# input_time_dir = '/Users/wangjipeng/Desktop/tour_corpus/闲聊'
# output_time_dir = '/Users/wangjipeng/Git_stu/machine_learning/data/sohu_news_segment_data/闲聊/'
# jieba.add_word('陪我聊天吧', 200)
# jieba.add_word('你从哪里来', 200)
# jieba.add_word('天气怎么样', 200)
# jieba.add_word('温度怎么样', 200)
#
# with open(input_time_dir, 'r') as reader:
#     int = 1800
#     for line in reader.readlines():
#         one_line = line.replace('\n', '')
#         jieba_line = jieba.cut(one_line)
#         write_line =  ' '.join(jieba_line)
#         # print (write_line)
#         new_output = output_time_dir + str(int) + '.txt'
#         with open(new_output, 'a+') as write:
#             write.write(write_line)
#         int +=1