#!/usr/bin/env python
# coding: utf-8


import Queue
import os
import threading
import urllib2
import re
import requests
from time import ctime

from bs4 import BeautifulSoup

url = 'http://www.ishuhui.net/ComicBookInfo/17'
base_url = 'http://www.ishuhui.net'


def title(url):
	'''
	获取漫画的名字 并创建漫画名目录创建目录
	:param url: 基础的url
	:return: 返回的是 标题名字
	'''
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	titlename = soup.find('span').string
	path = os.getcwd()
	new_path = os.path.join(path, titlename)  # 做路径
	if not os.path.isdir(new_path):  # 如果目录不存在创建目录
		os.mkdir(new_path)
	return titlename


def find_img(url):
	'''
	查找每一个章节的url
	:param url: 基础url
	:return:返回章节url
	'''
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	my_page = soup.find_all('a')
	pic_url = []
	for item in my_page:
		pic_url.append(item.get('href'))
	# print item.string
	# print pic_url
	return pic_url


def find_img_2(url_2):
	'''
	查找章节中图片url
	:param url_2: 章节的url
	:return: 返回图片url列表
	'''
	html = requests.get(url_2)
	soup = BeautifulSoup(html.text)
	my_page = soup.find_all('img')
	pic_url = []
	for item in my_page:
		pic_url.append(item.get('data-original'))
		pic_url.append(item.get('src'))
	# print pic_url
	return pic_url


def find_pic_title(url_2):
	'''
	查找章节漫画的名字
	:param url_2: 章节url
	:return: 章节的名字
	'''
	html = requests.get(url_2)
	soup = BeautifulSoup(html.text)
	my_title = soup.title.string
	# print my_title
	return my_title


def head_url(url1):
	'''
	用于请求头
	:param url1:
	:return:返回html
	'''
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}
	request = urllib2.Request(url1, headers=headers)
	response = urllib2.urlopen(request)
	return response


def filter_url(url):
	'''
	对url进行过滤 去除空的 和不需要的url
	:param url: url的列表
	:return: 返回 过滤完的url
	'''
	if url is not None:
		if re.match(".*ReadComicBooks*", url) and re.match(".*\d+\.html$", url):
			return url


def get_full_url():
	'''
	利用filter 对 url列表进行过滤
	:return: 返回过滤后的url再加上 基础url变成章节的完整url
	'''
	result1 = filter(filter_url, find_img(url))
	result = []
	for item in result1:
		result.append(base_url + item)
	# print result
	return result


def filter_url_2(url):
	'''
	对章节取出的url列表进行过滤
	:param url: 章节url列表
	:return: 返回图片url
	'''
	if url is not None:
		if re.match(".*\d+\.jpg$", url):
			return url


def get_full_url_2(url_ex):
	'''
	利用filter 对 图片url列表进行过滤，并取出章节标题
	:param url_ex: 图片url列表
	:return: 返回图片列表和 标题
	'''
	result1 = filter(filter_url_2, find_img_2(url_ex))
	title = find_pic_title(url_ex)
	# print result1
	return result1, title


class Mythread(threading.Thread):
	'''
	线程
	'''

	def __init__(self, target, args, titlename):
		super(Mythread, self).__init__()
		self.target = target
		self.args = args
		self.titlename = titlename

	def run(self):
		self.target(self.args, self.titlename)


def get_picture(url_ex, title_name):
	'''
	下载图片函数
	:param url_ex: 图片列表
	:param title_name: 标题
	:return:
	'''
	url_big, pic_title = get_full_url_2(url_ex)
	# url_pic = base_url + url_big[-1]
	# print url_big
	path = os.getcwd()  # 获取路径
	new_path_pic = os.path.join(path, title_name)
	new_path_pic_2 = os.path.join(new_path_pic, pic_title)
	if not os.path.isdir(new_path_pic_2):
		os.mkdir(new_path_pic_2)
	print new_path_pic_2  # 上面一小段 是创建漫画章节文件夹
	for item in url_big:
		contents = head_url(item).read()
		with open(new_path_pic_2 + '/' + item[-6:], 'wb') as f:
			f.write(contents)  # 图片写入文件


def main():
	print 'begin'
	full_url_dic = get_full_url()
	new_ids = list(set(full_url_dic))
	new_ids.sort(key=full_url_dic.index)
	print new_ids
	thread = []
	title_name = title(url)
	q = Queue.Queue(0)
	for item in new_ids:
		q.put(item)
	print "job qsize:", q.qsize()
	queue_size = range(q.qsize())
	for i in queue_size:
		my_thread = Mythread(get_picture, q.get(), title_name)
		thread.append(my_thread)
	for i in queue_size:
		thread[i].start()
	for i in queue_size:
		thread[i].join()
	print 'all done at:', ctime()


if __name__ == '__main__':
	main()
