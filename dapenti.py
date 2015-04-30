# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
import codecs
def get_id(page=1):
	url = 'http://www.dapenti.com/blog/blog.asp'
	payload = {
			'name':'xilei',
			'subjectid':'137',
			'page':page
			}
	divPage = requests.get(url, params = payload).text
	id_list = []
	soup = BeautifulSoup(divPage)
	for li in soup.find_all('li'):
		link = li.a['href']
		pattern = re.compile(r'.*?(\d+)')
		match = pattern.search(link)
		id = re.search(r'.*?(\d+)', link).group(1)
		id_list.append(id)
	return id_list

def fun():
	url = 'http://www.dapenti.com/blog/more.asp'
	payload = {'name':'xilei'}
	fp = codecs.open('out.txt', 'w+', 'utf-8')
	for page in range(28, 50):
		id_list = get_id(page)
		url = 'http://www.dapenti.com/blog/more.asp'
		for id in id_list:
			payload['id'] = id
			pentiPage = requests.get(url, params = payload)
			pentiPage.encoding = 'gbk'
			soup = BeautifulSoup(pentiPage.text)
			title = soup.find_all('title')[0].text
			if title.endswith(u'集锦'):
				continue
			title = title[9:]
			print str(page) + ':' + title.encode('gbk', 'ignore')
			content = ''
			for s in soup.find_all('div'):
				if s.has_key('class'): 
					content = s.text
					break
			span = soup.find_all('span')
			date = re.search(r'\d{4}\S*', span[1].text).group()
		
			fp.write('0' + '\t' + date + '\t' + title + '\t'  + content.replace(u'\n', u'') + '\n')
	fp.close()

if __name__ == '__main__':
    fun()
