import smtplib


smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)

smtpObj.starttls()

smtpObj.login('remcom4@yandex.ru','wmvdlanbtbdsqvqk')

smtpObj.sendmail('avplustv@yandex.ru','go to bed!')


smtpObj.quit()
