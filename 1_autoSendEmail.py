#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(to_list,sub,content):
    mail_host = "smtp.126.com"              # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
    mail_user = "**********"                # 用户名
    mail_pass = "********"                  # 密码
    mail_postfix = "126.com"                # 邮箱的后缀，网易就是163.com
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)           # 将收件人列表以‘；’分隔
    try:
        server = SMTP()
        server.connect(mail_host)           # 连接服务器
        server.login(mail_user,mail_pass)   # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False


def auto_sendEmail(to_list, theme, new_file):
    mail_host = "smtp.caixin.com"           # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
    mail_user = "********"                  # 用户名
    mail_pass = "********"                  # 密码
    mail_postfix = "caixin.com"             # 邮箱的后缀，网易就是163.com
    me = "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEMultipart()
    msg['Subject'] = theme
    msg['From'] = me
    msg['To'] = ",".join(to_list)           # 将收件人列表以','分隔
    # 正文
    content = "<html><head><title>我的第一个 HTML 页面</title></head><body><p>body 元素的内容会显示在浏览器中。</p>" \
              "<p>title 元素的内容会显示在浏览器的标题栏中。</p></body></html>"
    signature = "<br><br><br><span id='spnEditorSign'><br>--<br>********<br>********<br>********<br>" \
              "<br>Mail: &nbsp; ********<br>Tel: &nbsp; &nbsp;(+86)********<br>WeChat: ********<br>" \
              "Addr: &nbsp; ********</span>"
    contentpart = MIMEText(content + signature, 'html', 'utf-8')
    msg.attach(contentpart)
    # 附件
    attachpart = MIMEApplication(open(new_file, 'r', encoding='utf-8').read())
    attachpart.add_header('Content-Disposition', 'attachment', filename=new_file)
    msg.attach(attachpart)

    try:
        server = SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False


send_mail('guochang1162@163.com', "电话", "电话是XXX")