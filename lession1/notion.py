# !/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from pytion import Notion
from pytion.models import LinkTo
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from tabulate import tabulate
from dominate import document
from dominate.tags import table, tr, td, th, style

# 第三方 SMTP 服务
mail_host = "smtp.sina.com"  # 设置服务器
mail_user = "kuiqwang@sina.com"  # 用户名
mail_pass = "74120020f1207ea0"  # 口令
sender = 'kuiqwang@sina.com'
receivers = '125323997@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


# 邮件主题，邮件内容
def send_mail(title, message):
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(message, 'html', 'utf-8')
    message['From'] = Header(sender)  # 发送者
    message['To'] = Header(receivers)  # 接收者
    message['Subject'] = Header(title, 'utf-8')

    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())


def getNotionDBStatusInfo(dbid, status):
    SOME_TOKEN = 'secret_zfm2jh7s9oLGLGPDaZikI3SkN1xxV9TtHVbp1trM4nj'
    no = Notion(token=SOME_TOKEN)
    pdb = no.databases.get(dbid)
    pages = pdb.db_filter(property_name="Status", property_type="select", value=status)
    res = []
    for p in pages.obj:
        res.append(p.title)
    return res


def catchStatusInfo(dbid):
    baby_dbid = "2d40c8ba7dee4df58d40daebc3d97073"  # 这是孕期Timeline
    # status="Not started"
    babyList = ["In progress", "Not started", "Completed"]
    mailDict = {}
    for status in babyList:
        mailDict.__setitem__(status, getNotionDBStatusInfo(baby_dbid, status))
    ##功能设计1、获取各种状态的TODO DBID 2、整理各DB的Status信息 3、封状 status对应的dict 4、邮件功能，发送相关信息

    return mailDict


def tableCreate(data):
    # 创建文档
    doc = document()

    # 添加CSS样式，用于美化表格
    with doc.head:
        style("""
            table {
                width: 50%;
                border-collapse: collapse;
                margin: 20px;
            }
            th, td {
                padding: 10px;
                text-align: center;
                border: 1px solid black;
            }
            th {
                background-color: #ccc;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:nth-child(odd) {
                background-color: #fff;
            }
        """)

    # 创建表格
    with doc.add(table()):
        # 表头
        with tr():
            th("任务名称")
            th("进展状态")

        # 表格内容
        for status in data.keys():
           for t in data[status]:
               with tr():
                   td(t.simple)
                   td(status)
    return doc


def runJob(title,dbid):
    infos = catchStatusInfo(dbid)
    doc=tableCreate(infos)
    send_mail(title,doc.render())

if __name__ == '__main__':
    runJob("孕期TODO清单","")

