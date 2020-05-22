# MAIN SCRIPT RPG TIF
import sys
import rpg_config as config
from rpg_functools import *
import random

DEBUG = True

# global variables
time = 16 * 60 # 16 hours
energy = 100
final_quest_chances = 0 # percentage in [0,1]

badge = False
hamac_votes = ['ouardia', 'tiphaine', 'alexis']
covid = False
resistance = False
daoult_password = False
gpu = False
mbti = False
coffee = False

# quests
analysis = False
diploma = False
hamac = False

# Allies
alexis = True
mathieu = True



# INITIAL SEQUENCE

if DEBUG:
	print('INIT')
	print(f'time = {time}; energy={energy}\n')

# wake-up
snooze = input('Snooze ? [T/F]')
if snooze == 'T':
	time += config.snooze_dt
	energy += config.snooze_de
else:
	time += config.nonsnooze_dt
	energy += config.nonsnooze_de

if DEBUG:
	print('WAKEUP')
	print(f'time = {time}; energy={energy}\n')

# bike
bike_fight = input('A velo, se fighter avec un automobiliste ? [T/F]')
if bike_fight == 'T':
	time += config.bike_fight_dt
	energy += config.bike_fight_de
else:
	time += config.non_bike_fight_dt
	energy += config.non_bike_fight_de

if DEBUG:
	print('BIKE')
	print(f'time = {time}; energy={energy}\n')


# arrival
if time > 14 * 60: # before 10am
	# meeting with Daoult
	time += config.daoult_talk_dt
	raoult_bike_talk = input("Raconter a Daoult ce c****** d'automobiliste ? [T/F]")
	if raoult_bike_talk == 'T':
		time += config.daoult_fight_dt
		energy += config.daoult_fight_de
	else:
		# ask daoult to take the MBTI test
		rd = random.random()
		if rd <= config.daoult_test_mbti_proba:
			# daoult does take the test
			final_quest_chances += config.daoult_test_mbti_dchances
			time += config.daoult_test_mbti_dt
			mbti = True

else: # after 10am
	time += config.swann_beer_dt
	mbti = True

if DEBUG:
	print('IBENS ARRIVAL')
	print(f'time = {time}; energy={energy}\n')

# sysinfo
convince_pv = input('Convaincre PV ? [T/F]')
wait_sysinfo = False
if convince_pv == 'T':
	rd = random.random()
	if rd <= config.pv_convincing_proba:
		# pv is convinced!
		time += config.pv_dt
		badge = True
	else:
		# local var
		wait_sysinfo = True
if convince_pv == 'F' or wait_sysinfo:
	#wait
	time += config.after_pv_dt
	phiphuong = input('Deal with Phi-Phuong? [T/F]')
	if phiphuong == 'T':
		time += config.phiphuong_dt
		energy += config.phiphuong_de
		badge = True
	else:
		time += config.bilel_dt
		badge = True

if DEBUG:
	print('SYSINFO')
	print(f'badge = {badge}')
	print(f'time = {time}; energy={energy}\n')

# 6th floor
meeting_auguste = input('Go for the meeting with Auguste? [T/F]')
if meeting_auguste == 'T':
	time += config.auguste_meeting_dt
	energy += config.auguste_meeting_de
	covid = True
else:
	# stay with Pierre and Jerome
	listen_pj = input('Ecoute Pierre et Jerome? [T/F]')
	resistance = True #TODO: not sure it is useful
	if listen_pj == 'T':
		time += config.resistance_talk_dt
		daoult_password = True
	else:
		rd = random.random()
		if rd < 0.5:
			# montessori talk
			time += config.montessori_talk_dt
			energy += config.montessori_talk_de
		else:
			# hydroponics talk
			time += config.hydroponics_talk_dt
			energy += config.hydroponics_talk_de

if DEBUG:
	print('6th FLOOR')
	print(f'covid = {covid}, resistance = {resistance}, daoult_password = {daoult_password}')
	print(f'time = {time}; energy={energy}\n')

# in the lab
lab_choice = input('Plantes / Cafe / Caca ? [0/1/2]')
#local variable
toilets = False
if lab_choice == '0':
	# plants
	time += config.plants_dt
elif lab_choice == '1':
	coffee = True
	energy += config.coffee_de
	time += config.coffee_dt
	lab_choice = input('Caca ? [Oui:2/Non:0]')

if lab_choice == '2':
	toilets = True
	rd = random.random()
	if rd < 0.5:
		# discuss her poop
		time += config.poop_talk_dt
	else:
		energy += config.poop_constipated_de
	time += config.poop_dt

	poop_email = input("Envoyez un e-mail a tout l'institut a propos des cookies aux toilettes ? [T/F]")
	if poop_email == 'T':
		time += config.poop_email_dt
		energy += config.poop_email_de

if not toilets:
	# Tif asphyxiates Alexis, he is not her allie anymore
	alexis = False
	hamac_votes.remove('alexis')


answer_email_auguste = input("Repondre au mail d'Auguste de facon enervee ? [T/F]")
if answer_email_auguste == 'T':
	time += config.auguste_email_answer_dt
	covid = True


if DEBUG:
	print('LAB')
	print(f'covid = {covid}, coffee = {coffee}, toilets = {toilets}, alexis = {alexis}')
	print(f'time = {time}; energy={energy}\n')


# 7th FLOOR
time += config.floor7_dt


# Analysis
shifumi_output = shifumi()
while not shifumi_output:
	time += config.shifumi_between_games_dt
	shifumi_output = shifumi()

gpu = True


if DEBUG:
	print('SHIFUMI')
	print(f'gpu = {gpu}')
	print(f'time = {time}; energy={energy}\n')


# Analysis
if coffee:
	time += config.analysis_if_coffee_dt
	energy += config.analysis_if_coffee_de
else:
	promise_mathieu = input("Promets-tu a Mathieu de ne plus l'emmerder avec tes problemes de config pycharm? [T/F]")
	if promise_mathieu == 'T':
		time += config.promise_mathieu_dt
		hamac_votes.append('mathieu')
	else:
		time += config.non_promise_mathieu_dt
		# mathieu is no more an allie
		mathieu = False

analysis = True
energy += config.analysis_de


if DEBUG:
	print('ANALYSIS')
	print(f'analysis = {analysis}, coffee = {coffee}')
	print(f'time = {time}; energy={energy}\n')


# France & Guillaume encounters
discuss_france = input('Tu veux discuter de tes problemes avec France? [T/F]')
if discuss_france == 'T':
	time += config.france_dt
	energy = config.france_e
	hamac_votes.append('france')


discuss_guillaume = input('Tu veux discuter de tes problemes avec Guillaume? [T/F]')
if discuss_guillaume == 'T':
	time += config.guillaume_dt
	energy = config.guillaume_de
	hamac_votes.append('guillaume')


if DEBUG:
	print('F&G ENCOUNTERS')
	print(f'hamac_votes = {hamac_votes}')
	print(f'time = {time}; energy={energy}\n')
	print(f'HOUR = {get_time_in_hours(time)}')


assert time > 10 * 60 # before 2pm
assert energy > 0
assert badge
assert analysis
assert gpu











