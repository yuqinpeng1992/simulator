#!/bin/python
#coding=utf-8

messagefile = file('MessageDef.h', 'r')
c2sstart = 0
c2sstart_posoff = 0
s2cstart = 0
s2cstart_posoff = 0
print "MessageID = {"
for line in messagefile:
    try:
        if line.find("S2C_EVENT_BASE") > 0:
            array = line.split(' ')
            s2cstart = int(array[-1][:-2].strip())
            s2cstart_posoff += 1
        if line.find("S2C_Dse") > 0 :
            dsekey = line.split(",")[0].strip().split("_")[1]
            print "\"%s\" : %d," % (dsekey, s2cstart + s2cstart_posoff)
            print "%d : \"%s\"," %(s2cstart + s2cstart_posoff, dsekey)
            s2cstart_posoff += 1

        if line.find("C2S_EVENT_BASE") > 0:
            array = line.split(' ')
            c2sstart = int(array[-1][:-2].strip())
            c2sstart_posoff += 1
        if line.find("C2S_Dce") > 0 :
            dcekey = line.split(",")[0].strip().split("_")[1]
            print "\"%s\" : %d," % (dcekey, c2sstart + c2sstart_posoff)
            print "%d : \"%s\"," % (c2sstart + c2sstart_posoff, dcekey)
            c2sstart_posoff += 1

    except ValueError:
        continue
print "}"
messagefile.close()
