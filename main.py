from mfd import *
from mfd.saitek.x52pro import *
from mfd.saitek.directoutput import *
from time import (sleep, time)
import re
import os
import logging

def nowmillis():
	millis = int(round(time() * 1000))
	return millis

mfd = None

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

"""
empty route:
		#            --------------
		self.routes[''] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #

"""

"""
routes:
"""

class FortTradeMFD(X52Pro):
	def __init__(self):
		super().__init__(self)
		# NOTE - display is 3 rows of 16 characters
		self.routes = {}
		#            --------------
		self.routes['19 Leonis'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (Con Tech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"Graill Redd",
			"Ray (no pickup)",
			"",
			"-- 5 -----------",
			"19 Leonis",
			"Tshang (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Aasgaa'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"BD-22 3573",
			"Bohm (Gold)",
			"",
			"-- 4 -----------",
			"Leesti",
			"Lucas (Con Tech)",
			"WARNING: pirates",
			"-- 4 -----------",
			"Aasgaa",
			"Steiner (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Alioth *permit'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"HR 5451",
			"Dantec (Beryll.)",
			"",
			"-- 4 -----------",
			"G 224-46",
			"Zebrowski (Silv)",
			"",
			"-- 5 -----------",
			"Alioth",
			"Gotham (ALRs)",
			"WARNING: permit",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Anayol'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 4 -----------",
			"BD+31 2373",
			"Gaultier (Gold)",
			"",
			"-- 4 -----------",
			"Anayol",
			"Andrey (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Ao Kond'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"alt. Prog Cells",
			"-- 3 -----------",
			"MV Virginis",
			"Weitz (Pallad.)",
			"",
			"-- 4 -----------",
			"Ao Kond",
			"Fettman (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Arabh'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"Adeo",
			"Drobrov. (Gold)",
			"",
			"-- 4 -----------",
			"Gilya",
			"Bell (Land Enr.)",
			"",
			"-- 5 -----------",
			"Arabh",
			"Heceta (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Arany'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD-02 4304"
			"Bean (Palladium)",
			"",
			"-- 4 -----------",
			"Chongguls",
			"Filip. (Mar Eqp)",
			"",
			"-- 5 -----------",
			"Arany",
			"Ford (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['BD-22 3573'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"Bd-22 3573",
			"Bohm (Gold)",
			"",
			"-- 4 -----------",
			"Teveri",
			"Wiley (Indite)",
			"",
			"-- 5 -----------",
			"BD-22 3573",
			"Khayyam (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['BD+03 3531A'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD-02 4304",
			"Bean (Palladium)",
			"",
			"-- 4 -----------",
			"Cantjarisni",
			"Cochr. (ResSep)",
			"",
			"-- 5 -----------",
			"BD+03 3531A",
			"Horowitz (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Bielonti'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Bielonti",
			"Ahmed (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Bilfrost'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 4 -----------",
			"BD+31 2373",
			"Gaultier (Gold)",
			"",
			"-- 5 -----------",
			"Bilfrost",
			"Williams (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Bonitou'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Apala",
			"Wilson (ConTech)",
			"",
			"-- 4 -----------",
			"Yoruba",
			"Apt (Marine Eqp)",
			"",
			"-- 5 -----------",
			"Bonitou",
			"Lyakhov (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Boreas'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Boreas",
			"Rice (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Bukurnabal'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Awawar",
			"Cartw. (L. Enr.)",
			"",
			"-- 4 -----------",
			"Bukurnabal",
			"Kneale (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Caraceni'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Holiacan",
			"Fort. (ConsTech)",
			"",
			"-- 4 -----------",
			"LTT 13125",
			"Ross (Gold)",
			"",
			"-- 5 -----------",
			"Caraceni",
			"Kerr (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Cartoq'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"Naitis",
			"Ford (Gallite)",
			"",
			"-- 5 -----------",
			"Cartoq",
			"Avdeyev (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Circios'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"Tellus",
			"Ahern (Land Enr)",
			"",
			"-- 5 -----------",
			"Circios",
			"Mullane (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Contien'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"GQ Virginis",
			"Ray (Prog Cells)",
			"alt. Cons Tech",
			"-- 3 -----------",
			"Anaruwa",
			"Skvort. (Palla.)",
			"",
			"-- 4 -----------",
			"Contien",
			"Eanes (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Cybele'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Supercon)",
			"",
			"-- 5 -----------",
			"Cybele",
			"Fraley (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Daha'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"La Tenha",
			"Rozhd. (ConTech)",
			"",
			"-- 5 -----------",
			"Daha",
			"Burbank (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Dhanhopi'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Supercon)",
			"",
			"-- 5 -----------",
			"Dhanhopi",
			"Plucker (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Helvetitj'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"Acan",
			"Phill. (Mar Eqp)",
			"",
			"-- 5 -----------",
			"Helvetitj",
			"Friend (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['HIP 80242'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD-02 4304",
			"Bean (Palladium)",
			"",
			"-- 4 -----------",
			"Una",
			"Hoard (Res Sep)",
			"",
			"-- 5 -----------",
			"HIP 80242",
			"Csoma (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Holiacan'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Holiacan",
			"Hopi (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Hooriayan'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Hooriayan",
			"Davis (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['HR 8474'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD+65 1846",
			"Thiele (Palladium)",
			"",
			"-- 4 -----------",
			"Apala",
			"Wilson (ConTech)",
			"",
			"-- 5 -----------",
			"HR 8474",
			"Haiseng (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Ining'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"STKM 1-616",
			"Davy (Cons Tech)",
			"",
			"-- 4 -----------",
			"Haritis",
			"Tem (Palladium)",
			"",
			"-- 5 -----------",
			"Ining",
			"Shaara (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Ithaca'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Aulin",
			"Aulin (ConsTech)",
			"",
			"-- 3 -----------",
			"G 203-47",
			"Thorne (Narc.)",
			"",
			"-- 4 -----------",
			"Ithaca",
			"Hume (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Kokoimudji'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 3 -----------",
			"Leesti",
			"Lucas (ConsTech)",
			"WARNING: pirates",
			"-- 4 -----------",
			"Koller",
			"Cummings (Pall.)",
			"",
			"-- 5 -----------",
			"Kokoimudji",
			"Siodmak (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Kons'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 4 -----------",
			"BD+31 2373",
			"Lopez (Gold)",
			"",
			"-- 5 -----------",
			"Kons",
			"Makarov (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Kpaniya'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Aganippe",
			"Vasil. (Res Sep)",
			"",
			"-- 4 -----------",
			"Kpaniya",
			"Tilman (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['La Tenha'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Tantalum)",
			"",
			"-- 5 -----------",
			"La Tenha",
			"Rozhd. (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Leesti'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 3 -----------",
			"Naitis",
			"Ford (Bertrand.)",
			"",
			"-- 4 -----------",
			"Folna",
			"Patsayev (Gold)",
			"",
			"-- 5 -----------",
			"Leesti",
			"Lucas (ALRs)",
			"WARNING: pirates",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LHS 2405'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Apala",
			"Wilson (ConTech)",
			"",
			"-- 4 -----------",
			"LP 27-9",
			"Drebbel (Mar Eq)",
			"",
			"-- 5 -----------",
			"LHS 2405",
			"Godwin (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LHS 2771'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"LHS 2771",
			"Sarafanov (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LHS 2936'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"G 224-46",
			"Zebrow. (Bertr.)",
			"",
			"-- 4 -----------",
			"Andere",
			"Malzberg (Gold)",
			"",
			"-- 5 -----------",
			"LHS 2936 (again)",
			"Fraser (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LHS 3079'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"G 180-18",
			"Hale (Bertr.)",
			"",
			"-- 4 -----------",
			"Parutis",
			"Evans (Gold)",
			"WARNING: Hudson",
			"-- 5 -----------",
			"LHS 3079",
			"Ross (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LHS 3749'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Apala",
			"Wilson (ConTech)",
			"",
			"-- 4 -----------",
			"BD+65 1846",
			"Thiele (Pallad.)",
			"",
			"-- 5 -----------",
			"LHS 3749",
			"Rodden. (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LP 490-68'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"Tellus",
			"Ahern (Res Sep)",
			"",
			"-- 3 -----------",
			"BD+19 2511",
			"Lie (Beryllium)",
			"",
			"-- 4 -----------",
			"LP 490-68",
			"Shaara (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LP 621-11'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 4 -----------",
			"BD-01 2784",
			"Xiaog. (Pallad)",
			"",
			"-- 5 -----------",
			"LP 621-11",
			"Horch (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LTT 14478'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"LTT 14478",
			"Lanier (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['LTT 5964'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 5 -----------",
			"LTT 5964",
			"Witt (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Lugh'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"61 Virginis",
			"Furuk. (Pallad)",
			"alt. Silver",
			"-- 4 -----------",
			"Lu Velorum",
			"Miletus (Beryll)",
			"",
			"-- 5 -----------",
			"Lugh",
			"Balandin (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Manbatz'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"GQ Virginis",
			"Ray (Cons. Tech)",
			"",
			"-- 3 -----------",
			"Parutis",
			"Evans (Gold)",
			"WARNING: Hudson",
			"-- 4 -----------",
			"Manbatz",
			"Bretnor (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Marasing'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD+65 1846",
			"Thiele (Pallad.)",
			"or Gold / Silver",
			"-- 4 -----------",
			"Apala",
			"Wilson (ConTech)",
			"alt. Prog. Cells",
			"-- 5 -----------",
			"Marasing",
			"Landst. (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Meenates'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"G 224-46",
			"Zebrow. (Bertr.)",
			"",
			"-- 4 -----------",
			"Andere",
			"Kummer (Gold)",
			"",
			"-- 5 -----------",
			"Meenates",
			"Burbank (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['MCC 686'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 4 -----------",
			"LP 388-78",
			"Gaspar (Gold)",
			"",
			"-- 5 -----------",
			"MCC 686",
			"Smith (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Mereboga'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Khernidjal",
			"West (Cons Tech)",
			"",
			"-- 4 -----------",
			"BD+46 2014",
			"Simak (Gold)",
			"",
			"-- 5 -----------",
			"Mereboga",
			"Howard (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Mullag'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD+31 2373",
			"Gaultier (Gold)",
			"",
			"-- 4 -----------",
			"LDS 2314",
			"Dobrov. (Mar Eq)",
			"",
			"-- 5 -----------",
			"Mullag",
			"Potagos (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Nagybold'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"MCC 686",
			"Baudin (Beryll.)",
			"",
			"-- 4 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 5 -----------",
			"Nagybold",
			"Gordon (ALRs)",
			"WARNING: Outpost",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Nevermore'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"Tellus",
			"Ahern (ConsTech)",
			"",
			"-- 5 -----------",
			"Nevermore",
			"Pinto (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['NLTT 44958'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"Adeo",
			"Foda (Gold)",
			"",
			"-- 4 -----------",
			"Sivas",
			"Cavalieri (none)",
			"",
			"-- 5 -----------",
			"NLTT 44958",
			"Anderson (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Olwain'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD+31 2373",
			"Gaultier (Gold)",
			"",
			"-- 4 -----------",
			"LHS 2637",
			"Perez (ConsTech)",
			"",
			"-- 5 -----------",
			"Olwain",
			"Cabot (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Partha'] = [
                        # display  width #
                        #----------------#
                        "-- 1 -----------",
                        "Gateway",
                        "Dublin (Min Oil)",
                        "",
                        "-- 2 -----------",
                        "ROSS 1047",
                        "Drew (Beryll.)",
                        "",
                        "-- 3 -----------",
                        "HO HSI",
                        "Hand (BioreLich)",
                        "",
                        "-- 4 -----------",
                        "Partha",
                        "Gresley (ALRs)",
                        "Return to Wicca",
                        "-- repeat ------"]
                        # display  width #
                #            --------------
		self.routes['Opala'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD+31 2373",
			"Gaultier (Gold)",
			"",
			"-- 4 -----------",
			"Chaxiraxi",
			"Gamow (Min Extr)",
			"",
			"-- 5 -----------",
			"Opala",
			"Onizuka's (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Peckollerci'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"Acan",
			"Phill. (Mar Eqp)",
			"",
			"-- 5 -----------",
			"Peckollerci",
			"Minkowski (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Pongo'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Dublin Citadel",
			"Mineral Oil",
			"-- 2 -----------",
			"Inktasa",
			"Oleskiw Station",
			"Superconductors",
			"-- 3 -----------",
			"Ongkampan",
			"Fawcett Gateway",
			"Power Generators",
			"-- 4 -----------",
			"Pongo",
			"Antonelli",
			"ALRs",
                        "Tantalum",
			"-- 5 -----------",
			"Zaragas",
                        "Jenner Hub",
			"Performance Enhancers",
                        "-- 6 -----------",
                        "Gunnovale",
                        "Clauss City",
                        "Tea",
                        "-- 7 -----------",
                        "Epsilon Serpentis",
                        "Kimbrough Orbital",
                        "Superconductors",
                        "-- 8 -----------",
                        "Tau Bootis",
                        "Pascal Orbital",
                        "Marine Equipment",
                        "-- 9 -----------",
                        "Gateway",
                        "Dublin Citadel",
                        "Deliver Forts",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Quan Gurus'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 4 -----------",
			"Quan Gurus",
			"Russell (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Robor'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 3 -----------",
			"Naitis",
			"Ford (Bertrand.)",
			"",
			"-- 4 -----------",
			"Folna",
			"Patsayev (Gold)",
			"",
			"-- 5 -----------",
			"Robor",
			"Hooke (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Ross 94'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Ross 94",
			"Kingsbury (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['San Guan'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"Amahu",
			"Kondr. (Pallad.)",
			"",
			"-- 4 -----------",
			"Cantjarisni",
			"Cochr. (AutoFab)",
			"",
			"-- 5 -----------",
			"San Guan",
			"Alvarado (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['San Tu'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"San Tu",
			"Chomsky (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Siki'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"MCC 686",
			"Baudin (Beryll.)",
			"",
			"-- 3 -----------",
			"Naitis",
			"Ford (Coltan)",
			"",
			"-- 4 -----------",
			"Siki",
			"Lee (ALRs)",
			"WARNING: Outpost",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Tau Bootis'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Tau Bootis",
			"Pascal (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Tricorii'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD-02 4304",
			"Bean (Palladium)",
			"",
			"-- 4 -----------",
			"Tricorii",
			"Hippalus (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Unkuar'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"LP 377-78",
			"Gaspar (Gold)",
			"",
			"-- 4 -----------",
			"MCC 686",
			"Smith (Beryll.)",
			"",
			"-- 5 -----------",
			"Unkuar",
			"Flynn (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['V371 Normae'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 355",
			"Ramelli (ResSep)",
			"",
			"-- 3 -----------",
			"61 Virginis",
			"Furukawa (Pall.)",
			"alt. Silver",
			"-- 4 -----------",
			"GQ Virginis",
			"Ray (Cons Tech)",
			"",
			"-- 5 -----------",
			"V371 Normae",
			"Smith (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Varam'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (Beryll.)",
			"",
			"-- 3 -----------",
			"Holiacan",
			"Fortr. (ConTech)",
			"",
			"-- 4 -----------",
			"HIP 69518",
			"Great (Supercon)",
			"",
			"-- 5 -----------",
			"Varam",
			"Zebrowski (ALRs)",
			"",
			"-- 6 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Woloniugo'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 2 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 3 -----------",
			"BD+26 2184",
			"Wiberg (Mar Eqp)",
			"",
			"-- 4 -----------",
			"Woloniugo",
			"Renenbel. (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #
		#            --------------
		self.routes['Zosi'] = [
			# display  width #
			#----------------#
			"-- 1 -----------",
			"Gateway",
			"Wicca (Gold)",
			"",
			"-- 5 -----------",
			"LHS 2936",
			"Fraser (ConTech)",
			"",
			"-- 5 -----------",
			"LTT 13125",
			"Ross (Gold)",
			"",
			"-- 5 -----------",
			"Ross 113",
			"Tasman (None)",
			"",
			"-- 5 -----------",
			"Zosi",
			"Citi (ALRs)",
			"",
			"-- 5 -----------",
			"Gateway",
			"Wicca (ALRs)",
			"Return to Wicca",
			"-- repeat ------"]
			#----------------#
			# display  width #

		self.cursor = 0
		self.route = 'Manbatz'
		self.mode = 'system'
		self.lastinput = nowmillis()
	def OnSoftButton(self, *args, **kwargs):
		if self.lastinput > nowmillis() - 200:
			return
		self.lastinput = nowmillis()
		select = False
		up = False
		down = False
		if args[0].select:
			select = True
		if args[0].up:
			up = True
		if args[0].down:
			down = True
		if (up):
			if self.mode == 'route':
				self.cursor = (self.cursor - 1) % len(self.routes[self.route])
			else:
				self.cursor = (self.cursor - 1) % len(list(self.routes))
		if (down):
			if self.mode == 'route':
				self.cursor = (self.cursor + 1) % len(self.routes[self.route])
			else:
				self.cursor = (self.cursor + 1) % len(list(self.routes))
		if select:
			if self.mode == 'route':
				# if in route view, switch to system view and focus current system
				lines = list(self.routes)
				lines.sort()
				self.cursor = lines.index(self.route);
				self.mode = 'system'
			else:
				# else if system view, switch to route for selected and jump to line 0
				lines = list(self.routes)
				lines.sort()
				self.route = lines[self.cursor]
				self.mode = 'route'
				self.cursor = 0
		if (select or up or down):
			self.PageShow()
	def OnPage(self, page_id, activated):
		if page_id == 0 and activated:
			self.PageShow()

	def PageShow(self):
		if self.mode == 'route':
			lines = self.routes[self.route]
			cursor = self.cursor
			mfd.display(lines[(cursor + 0) % len(lines)], lines[(cursor + 1) % len(lines)], lines[(cursor + 2) % len(lines)])
			for x in range(-1, 1):
				if re.match(r'^-- \d', lines[(cursor + x) % len(lines)]):
					addToClipBoard(lines[(cursor + x + 1) % len(lines)])
		else:
			lines = list(self.routes)
			lines.sort()
			cursor = self.cursor
			mfd.display(lines[(cursor - 1) % len(lines)], "> " + lines[(cursor + 0) % len(lines)], lines[(cursor + 1) % len(lines)])

#logging.root.setLevel(logging.DEBUG)

doObj = FortTradeMFD()
mfd = X52ProMFD(doObj)
sleep(0.5)

mfd.doObj.PageShow()
#mfd.display("test1", "test2", "1234567890123456")
print("showing fast-track fortification trade routes")
print("press <enter> to exit")
input()
