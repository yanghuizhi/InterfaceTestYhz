# !/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from config import conf as cf


class SendEmail:

    def __init__(self):
        pass

    def send_mail(self, content):
        msg = MIMEText(content, "plain", "utf-8")
        msg['Subject'] = "接口测试报告邮件"
        msg['From'] = cf.SEND_USERNAME
        msg['To'] = ";".join(cf.RECE_NAME)
        print(";".join(cf.RECE_NAME))
        try:
            server = smtplib.SMTP()
            server.connect(cf.SEND_HOST,25)
            server.login(cf.SEND_USERNAME, cf.PASS_WORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.close()
            print("  PASS  ")
        except smtplib.SMTPException:
            print("发送失败")

    def send_main(self, pass_list, fail_list):

        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)

        content = f"此次一共运行接口个数为{count_num}," \
                  f"通过个数为{pass_num}，" \
                  f"失败个数为{fail_num}," \
                  f"通过率为{pass_result}," \
                  f"失败率为{fail_result}"
        self.send_mail(content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1, 2, 3,4,5], [2, 6, 8])
