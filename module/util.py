# -*- coding:utf-8 -*-
import base64
from email import encoders, email
from email.mime.base import MIMEBase
from email.utils import formatdate
import hashlib
import json
import os
import random
import sys
import urllib
import urllib2
from datetime  import datetime


__author__ = 'venkingLiu'

reload(sys)
sys.setdefaultencoding("utf-8")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def fromtimestamp(value, dateformat='%Y-%m-%d %H:%M:%S'):
    dt = datetime.fromtimestamp(int(value))
    return dt.strftime(dateformat)


def setedlist(list):
    return set(list)


def setedlistex(list):
    result = []
    result = [result.append(v) for v in list if v not in result]
    return result


def tomd5(v):
    return hashlib.new('md5', v).hexdigest()


def toSHA1(v):
    return hashlib.sha1(v).hexdigest()


def base64encode(v):
    return base64.b64encode(v)


def base64decode(v):
    return base64.b64decode(v)


def strtounicode(v):
    return unicode(v)


def unicodetostr(v):
    return v.encode('utf-8')





def encrypt(key, s):
    b = bytearray(str(s).encode("utf-8"))
    n = len(b) # 求出 b 的字节数
    c = bytearray(n * 2)
    j = 0
    for i in range(0, n):
        b1 = b[i]
        b2 = b1 ^ key # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16 # b2 = c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码
        c[j] = c1
        c[j + 1] = c2
        j = j + 2
    return c.decode("utf-8")


def decrypt(key, s):
    c = bytearray(str(s).encode("utf-8"))
    n = len(c) # 计算 b 的字节数
    if n % 2 != 0:
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j + 1]
        j = j + 2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2 * 16 + c1
        b1 = b2 ^ key
        b[i] = b1
    try:
        return b.decode("utf-8")
    except:
        return "failed"


def httpfetch(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python'}
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req, timeout=100)
    result = response.read()
    return result


def ip_location(ip):
    longti = 0
    lati = 0
    province = ''
    city = ''
    district = ''
    street = ''
    url = "http://api.map.baidu.com/location/ip?ak=%s&ip=%s&coor=bd09ll"
    ak = "fUUi2wpNqIKyf2Zh7ZE0r1rF"

    jsonStr = httpfetch(url % (ak, ip))
    jsonObj = json.loads(jsonStr)
    if jsonObj['status'] == 0:
        addrJson = jsonObj['content']['address_detail']
        pointJson = jsonObj['content']['point']
        longti = pointJson['x']
        lati = pointJson['y']
        province = addrJson['province']
        city = addrJson['city']
        district = addrJson['district']
        street = addrJson['street'] + addrJson['street_number']
    else:
        pass

    return longti, lati, province, city, district, street


#server['name'], server['user'], server['passwd']
def send_mail(server, fro, to, subject, text, files=[]):
    msg = MIMEMultipart()
    # msg['From'] = fro
    msg['From'] = email.utils.formataddr(('...客服', fro))
    msg['Subject'] = subject
    msg['To'] = to #COMMASPACE==', '
    msg['Date'] = formatdate(localtime=True)

    # part1 = MIMEText(text, 'plain')
    # part2 = MIMEText(html, 'html')

    msg.attach(MIMEText(text, 'html'))

    for file in files:
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data
        part.set_payload(open(file, 'rb'.read()))
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)

    import smtplib

    smtp = smtplib.SMTP(server['name'])
    # smtp.login(server['user'], server['passwd'])
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()




if __name__ == '__main__':
    server = {}
    server['name'] = "mail.xxx.com"
    server['user'] = "xxx@sss.com"
    server['passwd'] = "mailpwd"
    # send_mail(server, server['user'], '986008792@qq.com', "请激活您的帐户", "汉字\n english", [])
    # send_mail(server, 'service', 'zhangxiaodel@live.cn', "请激活您的帐户", "汉字\n english", [])
    # send_mail(server, server['user'], '986008792@qq.com', "请激活您的帐户", "汉字\n english", [])

    # img,code= create_validate_code()
    # img.save("1.jpg")
    # print img
    # print "\n"
    # print code
    print  tomd5('123456')
