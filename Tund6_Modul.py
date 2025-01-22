from math import *
from random import *
from datetime import *

def summa3(arv1:int, arv2:int, arv3:int)->int:
	"""Tagastab kolme täisarvu summa

	:param int arv1: Esimene number
	:param int arv2: Teine number
	:param int arv3: Kolmas number
	:rtype: int

	"""
	summa=arv1+arv2+arv3
	return summa
	

def arithmetic(x1:float, x2:float, x3:str)->any:
	"""Lihtne kalkulaator
	+ - liitmine
	- - lahutamine
	* - korrutamine
	/ - jagamine
	:param int x1: Esimene argument
	:param int x2: Teine argument
	:param str x3: Arithmeetiline operatsioon
	:rtype: var Määramata tüüp(float or str)
	"""
	if x3=="+":
		vastus=x1+x2
	elif x3=="-":
		vastus=x1-x2
	elif x3=="*":
		vastus=x1*x2
	elif x3=="/":
		vastus=x1/x2
	else:
		vastus="Неизвестная операция"

	return vastus


def is_year_leap(a:int)->bool:     #bool - булевый тип, для хранения логических значений, которые могут быть либо истинными, либо ложными.
	"""Liigaasta leidmine
	Tagastab True, kui liigaasta ja False kui on tavaline aasta.
	:param int a: aasta number
	:rtype: bool tagastab loogilises formaadis tulemus
	"""
	if a%4==0:
		vastus=True
	else:
		vastus=False

	return vastus


def square(a:float)->any:
	"""Ruut
	Tagastab ruudu ümbermõõt, ruudu pindala ja ruudu diagonaal
	:param float a: ruudu külg
	:rtype: float P, S, d
	"""
	S=round(a**2,2)
	P=round(a*4,2)
	d=round(a*sqrt(2),2)

	vastus=f"S={S}, P={P}, d={d}"   # return S, P, d - если нужно в будующем обратиться отдельно к данным переменным

	return vastus


def season(nr:int)->str:
	"""Aasta hooajade leidmine
	:param int nr: kuu number (1 kuni 12)
	:rtype: str Talv, Kevad, Suvi, Sügis
	"""

	if nr in [12,1,2]:
		vastus="Talv"
	elif nr in [3,4,5]:
		vastus="Kevad"
	elif nr in [6,7,8]:
		vastus="Suvi"
	elif nr in [9,10,11]:
		vastus="Sügis"
	else:
		vastus="Arv peab olema 1 kuni 12"

	return vastus


def bank(a:float,years:int)->float:
	"""Pangadeposiit
	:param float a:
	:param int years:
	:rtype: float
	"""
	#A=a*(1+protsent)^years - формула сложных процентов
	protsent=0.10
	summa=round(a*((1+protsent)**years),2)

	# for i in range(years)
	# a*=1.1
	# return a
	return summa


def is_prime(a=randint(0,1000))->bool:    # перемостреть дома!
	"""Algarvud
	Tagastab True, kui algarv ja False kui mite algarv
	:param int a: arv 0 kuni 1000
	:rtype: bool tagastab loogilises formaadis tulemus
	"""
	print(a)
	vastus=True
	for i in range(2,a):
		if a%i==0:
			vastus=False

	return vastus


def date(paev,kuu,aasta)->bool:
	"""Õige kuupäev
	"""
	try:
		datetime(aasta,kuu,paev)
	except:
		vastus=True
	vastus=False

	return vastus



