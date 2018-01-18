#!/usr/bin/env python
# coding: utf-8



import Queue
import os
import threading
import urllib2
import re
import requests
from time import ctime

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup

url = 'http://www.ishuhui.net/ReadComicBooks/4765.html'


def title(url):
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	titlename = soup.find('span').string
	path = os.getcwd()
	new_path = os.path.join(path, titlename)
	if not os.path.isdir(new_path):
		os.mkdir(new_path)
	return titlename


#
# def find_img(url):
# 	html = requests.get(url)
# 	soup = BeautifulSoup(html.text)
# 	my_page = soup.find_all('a')
# 	pic_url = []
# 	for item in my_page:
# 		pic_url.append(item.get('href'))
# 	# print item.string
# 	# print pic_url
# 	return pic_url
# pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)

def find_img_2(url):
	html = requests.get(url)
	soup = BeautifulSoup(html.text)
	my_page = soup.find_all('img')
	pic_url = []
	for item in my_page:
		pic_url.append(item.get('data-original'))
		pic_url.append(item.get('src'))
	# print pic_url
	return pic_url


# find_img_2(url)

# def head_url(url1):
# 	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# 	headers = {'User-Agent': user_agent}
# 	request = urllib2.Request(url1, headers=headers)
# 	response = urllib2.urlopen(request)
# 	return response
#
#
def filter_url(url):
	if url is not None:
		if re.match(".*\d+\.jpg$", url):
			return url


def find_pic_title(url_2):
	html = requests.get(url_2)
	soup = BeautifulSoup(html.text)
	my_title = soup.title.string
	print my_title
	return my_title


def get_full_url_2(url):
	result1 = filter(filter_url, find_img_2(url))
	title = find_pic_title(url)
	# for item in result1:
	# 	result = base_url + item
	return result1, title


# return result


def get_picture(url_ex, title_name):
	url_big, pic_title = get_full_url_2(url_ex)
	# url_pic = base_url + url_big[-1]
	print url_big, pic_title
	path = os.getcwd()
	new_path_pic = os.path.join(path, title_name)
	print new_path_pic
	new_path_pic_2 = os.path.join(new_path_pic, pic_title)
	if not os.path.isdir(new_path_pic_2):
		os.mkdir(new_path_pic_2)


get_picture(url, '【漫画】亚人')

########################################

# class Mythread(threading.Thread):
# 	def __init__(self, target, args, titlename):
# 		super(Mythread, self).__init__()
# 		self.target = target
# 		self.args = args
# 		self.titlename = titlename
#
# 	def run(self):
# 		self.target(self.args, self.titlename)
#
#
# def get_picture(url, title_name):
# 	url_big = find_img_2(url)
# 	url_pic = base_url + url_big[-1]
# 	print url_pic
#
# 	contents = head_url(url_pic).read()
# 	with open(title_name + '/' + url_pic[-10:], 'wb') as f:
# 		f.write(contents)
#
#
# def main():
# 	print 'begin'
# 	full_url_dic = get_full_url()
# 	thread = []
# 	title_name = title(url)
# 	q = Queue.Queue(0)
# 	for item in full_url_dic:
# 		q.put(item)
# 	print "job qsize:", q.qsize()
# 	queue_size = range(q.qsize())
# 	for i in queue_size:
# 		my_thread = Mythread(get_picture, q.get(), title_name)
# 		thread.append(my_thread)
# 	for i in queue_size:
# 		thread[i].start()
# 	for i in queue_size:
# 		thread[i].join()
# 	print 'all done at:', ctime()
#
#
# if __name__ == '__main__':
# 	main()
