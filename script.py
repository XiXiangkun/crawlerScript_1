import requests
import urllib
from bs4 import BeautifulSoup
import re
import configparser

#导入config数据
config = configparser.ConfigParser()
config.read('config.cfg',encoding='utf-8-sig')
Data = config['Data']
#定义header，可以从chrme浏览器查询header，eval实现str转dict
header = eval(Data['header'])
#url输入
url = Data['url']
#data表单，eval实现str转dict
data = eval(Data['data'])
#编码方式要从chrome查询修改
data_code = urllib.parse.urlencode(data,encoding='GBK')
url_total = url + data_code
#发送请求
response = requests.get(url_total,headers=header)
#修改encoding方式，将乱码转为正常码字
response.encoding=response.apparent_encoding
#调用beautiful库文件，创建解析器
bs = BeautifulSoup(response.text,'html.parser')


##########################################################
#选取类名为tdc2的标签，也是最后需要具体修改的地方
string_get=bs.select('.tdc2 ')[1].text
num_get = re.findall(r"\d+\.?\d*",string_get)[0]
##########################################################


print(data['area']+"的邮编是："+num_get)

#只是简单的一个例子，后面需要用到网页操作可以批量爬取，不用自己操作
