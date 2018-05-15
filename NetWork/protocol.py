#coding=utf-8
import socket
import struct
import binascii


class Protocol(object):
    def __init__(self):
        self._headsize = 4
        self._size = 0
        self._type = 0
        self._value = 0
        self._data = ""

    def packagebuff(self, data):
        self._size = len(data)
        s = struct.Struct('!h' + str(self._size) + 's')
        self._data = data
        v = (self._size, self._data)
        return s.pack(*v)

    def package(self, type, data):
        self._size = len(data) + 2 + 4
        self._type = type
        self._value = 1
        self._data = data

        s = struct.Struct('!hhi' + str(len(data)) + 's')
        v = (self._size, self._type, self._value, self._data)
        return s.pack(*v)

    def unpackage(self, data):
        # get header
        if len(data) < self._headsize:
            return False
        self._size, = struct.unpack('!i', data[0:self._headsize])
        #self._size = socket.ntohl(self._size)
        # get body
        if len(data) < self._size + self._headsize:
            return False
        try:
            self._type, self._data, = struct.unpack('!H' + str(self._size - 2) + 's', data[self._headsize:self._headsize+self._size])
            return True
        except Exception as e:
            return False

    def type(self):
        return self._type

    def size(self):
        return self._size

    def data(self):
        return self._data

    def headsize(self):
        return self._headsize
