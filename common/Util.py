#!/bin/python
#coding=utf-8

def PrintProtoFile(name):
    filename = "./proto/" + name + ".proto"
    protofile = file(filename)
    if protofile:
        '''
        for line in protofile:
            print(line, end='')
        '''
        content = protofile.read(1024 * 8)
        print content
    protofile.close()