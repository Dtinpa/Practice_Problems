#!/usr/bin/env python

class chainLink:
	__val = ""
	__read = ""

	def __init__(self, value, read):
		self.__val = value
		self.__read = read

	def value(self):
		return self.__val

	def read(self):
		return self.__read

	def setRead(self, rd):
		self.__read = rd
