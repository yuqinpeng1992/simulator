#!/bin/python
#coding=utf-8
import logging
import sys
import threading
import time
import common.Util as util
from NetWork.SpiritNetHandler import SpiritNethandler
from common.GetCppTypeStr import GetCppTypeStr
from common.Message import MessageID
from google.protobuf import symbol_database as _symbol_database
from common.MessageAll import *

_sym_db = _symbol_database.Default()
client_str = "输入Dce协议名或者协议ID(exit退出):"

def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(module)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logging.info(
        "Set logging level: %s", logging.getLevelName(logger.getEffectiveLevel()))

#主函数入口
if __name__ == "__main__":
	init_logging()
	#设置未登录
	login_status = 0
	#启动连接服务器 登录流程
	m_nethandler = SpiritNethandler(1)
	netthread = threading.Thread(target=m_nethandler.connectServer)
	netthread.start()

	#校验登录完成
	while m_nethandler.getloginstatus() != 1:
		time.sleep(1)

	#登录完成
	print client_str
	dce_name = sys.stdin.readline().strip('\n')
	while True:
		if dce_name == "exit":
			break
		#协议号转换成协议名
		if dce_name.isdigit():
			dceid = int(dce_name)
			if MessageID.has_key(dceid):
				dce_name = MessageID[dceid]

		if _sym_db._symbols.has_key(dce_name):
			#打印proto文件
			util.PrintProtoFile(dce_name)
			#获取proto对应的类
			request = _sym_db.GetSymbol(dce_name)()
			desc = _sym_db.pool._descriptors[dce_name]
			for field in desc.fields:
				fieldname = field.name
				cpptype = field.cpp_type
				print "请输入字段名:%s - 数据类型:%s" % (fieldname, GetCppTypeStr(cpptype))
				input_str = sys.stdin.readline().strip('\n')
				if hasattr(request, fieldname):
					try:
						if cpptype == 1 or cpptype == 2:
							setattr(request, fieldname, int(input_str))
						elif cpptype == 9:
							setattr(request, fieldname, input_str)
						elif cpptype == 7:
							isTrue = (input_str == "true")
							setattr(request, fieldname, isTrue)
						else:
							pass
					except ValueError:
						print "数据输入错误！！！"
			print "发送协议ID = %d， %s = {" %(MessageID[dce_name], dce_name)
			print request.__str__()
			print "}"
			m_nethandler.sendMsg(MessageID[dce_name],request )
		else:
			print "没有该协议:"
		time.sleep(1)
		print client_str
		dce_name = sys.stdin.readline().strip('\n')
