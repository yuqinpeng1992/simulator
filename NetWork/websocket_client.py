#coding=utf-8
import logging
import websocket
import common.Config
class  WebSocketClient(object):
    def __init__(self, connect_cb = None, shutdown_cb = None, receive_cb = None):
        self._wsInstance = None
        self._recvbuff = ""
        self._cbConnect = connect_cb
        self._cbShutdown = shutdown_cb
        self._cbReceive = receive_cb

    def connect(self, servername):
        websocket.enableTrace(True)
        wsaddr = common.Config.loginurl[servername]
        self._wsInstance = websocket.WebSocketApp(wsaddr,
                                                 on_message=self._onMessage,
                                                 on_error=self._onError,
                                                 on_close=self._onClose)
        self._wsInstance.on_open = self._onOpen
        self._wsInstance.run_forever()
        logging.info("Connect to websocket %s", wsaddr)

    def shutdown(self):
        self._wsInstance.close()
        self._cbShutdown()

    def sendData(self, data):
        self._wsInstance.send(data)

    def _onOpen(self, ws):
        logging.info("websocket connected...")
        self._cbConnect()

    def _onClose(self, ws):
        self._cbShutdown()

    def _onMessage(self, ws, message):
        self._cbReceive(message)

    def _onError(self, ws, error):
        print error
