# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url='https://rate.bot.com.tw/xrt?Lang=zh-TW'

page=requests.get(url) #抓URL的內容

bsObj=BeautifulSoup(page.content,'html.parser') #用html.parser內容解析，

#print(bsObj)


for tr in bsObj.find('table').find('tbody').findAll('tr'): #找網頁的<tr>標籤
    
    #print(tr)
    
    cell=tr.findAll('td')
    
    #print(cell[1])
    
    currency=cell[0].find('div',{'class':'visible-phone'}).contents[0] 
    #找到所有td含有html.parser的第一個標籤
    #print(currency)
    
    currency=currency.replace('\r','')
    currency=currency.replace('\n','')   
    currency=currency.replace(' ','')
    
    #print(currency)
    
    curr_rate=cell[2].contents[0] #把第三欄(幣別值)的值抓出來
    
    print(currency,':',curr_rate)
    
    
    
    
    