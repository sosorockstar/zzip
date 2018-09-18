# coding: utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
import os
import smtplib


class ZMail:
    def __init__(self, mail_conf):
        self.host = mail_conf['host']
        self.port = mail_conf['port']
        self.sender = mail_conf['sender']
        self.receiver = mail_conf['receiver']
        self.timeout = mail_conf.get('timeout', 60)
        self.msg = MIMEMultipart()
        self.msg['From'] = self.format_addr(self.sender)
        self.msg['To'] = self.format_addr(self.receiver)
        self.attach_id = 0

    def format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((
            Header(name, 'utf-8').encode(),
            addr.encode('utf-8') if isinstance(addr, unicode) else addr
        ))

    def set_subject(self, subject):
        self.msg['Subject'] = Header(subject, 'utf-8').encode()

    def set_text(self, text):
        self.msg.attach(MIMEText(text, 'plain', 'utf-8'))

    def set_html(self, html):
        self.msg.attach(MIMEText(html, 'html', 'utf-8'))

    def attach_csv(self, csv_path, csv_name=None):
        if not csv_name:
            csv_name = os.path.basename(csv_path)
        with open(csv_path, 'r') as f:
            mime = MIMEBase('application', 'octet-stream')
            mime.add_header('Content-Disposition', 'attachment', filename=csv_name)
            mime.add_header('Content-ID', '<'+str(self.attach_id)+'>')
            mime.add_header('X-Attachment-Id', str(self.attach_id))
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            self.msg.attach(mime)
            self.attach_id += 1

    def attach_png(self, png_path, png_name=None):
        if not png_name:
            png_name = os.path.basename(png_path)
        with open(png_path, 'rb') as f:
            mime = MIMEBase('image', 'png', filename=png_name)
            mime.add_header('Content-ID', '<'+str(self.attach_id)+'>')
            mime.add_header('X-Attachment-Id', str(self.attach_id))
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            self.msg.attach(mime)
            self.attach_id += 1

    def send_mail(self):
        server = smtplib.SMTP(self.host, self.port, timeout=self.timeout)
        # server.set_debuglevel(1)
        server.sendmail(self.sender, self.receiver, self.msg.as_string())
        server.quit()


def test_zmail():
    mail_conf = {
        "host": "smtp.xxxxxx.com",
        "port": 25,
        "sender": "test@xxxxxx.com",
        "receiver": [
            "xxx@xxxxxx.com",
        ],
        "timeout": 60
    }
    mail = ZMail(mail_conf)
    mail.set_subject('测试邮件')
    mail.set_text('这是测试邮件\n请勿回复')
    mail.attach_csv('dp.csv')
    mail.attach_png('cloud.png')
    mail.send_mail()


if __name__ == '__main__':
    test_zmail()