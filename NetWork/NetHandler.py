#coding=utf-8
import logging
from common.Config import servername
__client_status__ = ['None', 'Connected', 'Online', 'Offline']

class NetHandler(object):
    def __init__(self, id):
        self._id = id
        #self._host = ""
        #self._port = 0
        self._servername = ""
        self._status = __client_status__[0]
        self._netHandler = None

    def connect(self):
        self._netHandler.connect(self._servername)

    def connectServer(self):
        #self._host = host
        #self._port = port
        self._servername = servername
        self.connect()

    def shutdown(self):
        self._netHandler.shutdown()

    def sendData(self, data):
        self._netHandler.sendData(data)

    def connect_cb(self):
        self._status = __client_status__[1]
        logging.info("Nethandler %d connect success...", self._id)

    def shutdown_cb(self):
        self._status = __client_status__[3]
        logging.info("Nethandler %d shutdown...", self._id)

    def receive_cb(self, data):
        pass

