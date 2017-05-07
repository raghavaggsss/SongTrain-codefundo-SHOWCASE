#!/usr/bin/env python
import smtplib

def send_email(mail_id,song_name):
	to = mail_id
	gmail_user = 'songtraincfd@gmail.com'
	gmail_pwd = 'Microsoft123!'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)

	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Your Karaoke is ready! Please upload recording. \n'
	msg = header + '\n We have generated the karaoke for your audio file named - %s. Please login using the link ( https://songtraincfd.southindia.cloudapp.azure.com/Project/ ) to view your profile and proceed. \n\n'%song_name
	smtpserver.sendmail(gmail_user, to, msg)
	smtpserver.close()
