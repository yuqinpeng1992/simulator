#coding=utf-8
import logging

import protocol
from NetWork.NetHandler import NetHandler
from NetWork.websocket_client import WebSocketClient
from common.Message import MessageID
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import text_format
from common.Config import *

_sym_db = _symbol_database.Default()

__client_status__ = ['None', 'Connected', 'Online', 'Offline']


class SpiritNethandler(NetHandler):
    def __init__(self, id):
        super(SpiritNethandler, self).__init__(id)
        self._netHandler = WebSocketClient(self.connect_cb, self.shutdown_cb, self.receive_cb)
        self._recvbuff = ""
        self._loginstatus = 0

    def connect_cb(self):
        super(SpiritNethandler, self).connect_cb()
        self.requestLogin()

    def shutdown_cb(self):
        super(SpiritNethandler, self).shutdown_cb()

    def receive_cb(self, data):
        #logging.debug('receive data: %s', data);
        totallen = len(data)
        self._recvbuff += data
        while True:
            proto = protocol.Protocol()
            if proto.unpackage(self._recvbuff) == False:
                break
            self.handleMessage(proto)
            if totallen > proto.size() + proto.headsize():
                self._recvbuff = self._recvbuff[proto.size() + proto.headsize()]
            else:
                self._recvbuff = ""
                break;

    def handleMessage(self, pack):
        type = pack.type()
        if MessageID.has_key(type):
            response_name = MessageID[type]
            if _sym_db._symbols.has_key(response_name):
                response = _sym_db.GetSymbol(response_name)()
                response.ParseFromString(pack.data())
                print "收到数据协议:%s" % (response_name)
                #import common.Util as util
                #util.PrintProtoFile(response_name)
                print "data: {"
                print response.__str__()
                print "}"
                if response_name == 'DseMainScreenReady':
                    self._loginstatus = 1
        pass

    def sendString(self, data):
        message = protocol.Protocol()
        buffer = message.packagebuff(data)
        self.sendData(buffer)
        logging.debug("Send string size %d: {%s}", len(buffer), data)

    def sendMsg(self, type, proto):
        message = protocol.Protocol()
        buffer = message.package(type, proto.SerializeToString())
        self.sendData(buffer)
        logging.debug("Send message %d size %d: {%s}", type, len(buffer),
                      text_format.MessageToString(proto, True, True))

    def test_login(self):
        self.shutdown();
        self.connect();

    def requestLogin(self):
        data = "gl," + loginaccount + "_" + str(region) + ",861107584555586"
        self.sendString(data)

    def getloginstatus(self):
        return self._loginstatus
