#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


msg = MIMEText('你好，内容已发你，确定请回复.', 'plain', 'utf-8')


from_ = 'zgcmc126@126.com'
pwd = 'zgcm0518c28'

to_ = '316513623@qq.com'

msg['From'] = Header('Python <{0}>'.format(from_), 'utf-8')
msg['To'] = Header('myfriend <{0}>'.format(to_), 'utf-8')
msg['Subject'] = Header('一份问候', 'utf-8')
# print(msg)
# exit(-1)

smtp_server = 'smtp.126.com'

try:
    srv = smtplib.SMTP_SSL(smtp_server.encode(), 465)
    srv.set_debuglevel(1)
    srv.login(from_, pwd)

    srv.sendmail(from_, [to_], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)
