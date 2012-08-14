#!/usr/bin/env python
# -*- encoding: utf-8 -*- 
import httplib, urllib
import sys,os
import datetime
import time

try:
    from hashlib import md5
except:
    import md5  
    
    
def writeLog(data):
	logfile = open("log.txt","a")
	tnow = datetime.datetime.now() 
	sys.stdout.write("%s\n%s\n\n"%(tnow.isoformat(),data))
	logfile.write("%s\n%s\n\n"%(tnow.isoformat(),data))
	logfile.close()

def login(conn):
	sendItem="DDDDD="+username+"&upass="+md5password+"&R1=0&R2=1&para=00&0MKKey=123456"
	print sendItem
	conn.request("POST", "", sendItem, headers)
	response = conn.getresponse()	
	data = response.read()
	writeLog(data)
	return data
	
def logout(conn):
	conn.request("GET","/F.htm")
	response = conn.getresponse()
	data=response.read()
	writeLog(data)

headers = {"Content-type": "application/x-www-form-urlencoded",
            "Connection":"keep-alive"}



if(__name__=='__main__'):

	#Please type in your username and password here
	username="XXXXXXXX" #这是用户名
	password="XXXXXXXX" #这是密码
	password="1"+password+"12345678"
	md5=md5()
	md5.update(password)
	md5password=md5.hexdigest()+"123456781"
	conn= httplib.HTTPConnection("gw.bupt.edu.cn") 
	
	
	try:
		login(conn)
		print r'登录成功'
	except:
		print r'网络连接故障'
	'''
	logout(conn)
	'''
	conn.close() 
