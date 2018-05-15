#coding=utf-8
def GetCppTypeStr(cpptype):
	return {
			1 : 'int',
			2 : 'int64',
			3 : 'uint32',
			4 : 'uint64',
			5 : 'double',
			6 : 'float',
			7 : 'bool',
			8 : 'enum',
			9 : 'string',
			10 : 'message',
	}.get(cpptype, 'error')