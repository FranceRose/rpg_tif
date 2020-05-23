# MAIN SCRIPT RPG TIF
import sys
import rpg_config as config
from rpg_functools import *
import random


def game(DEBUG=False):

	# global variables
	time = config.start_hour * 60 # 16 hours
	energy = 100

	# needed for advancement
	badge = False
	gpu = False
	felipe_badge = False

	hamac_votes = ['ouardia', 'tiphaine', 'alexis']
	resistance = False
	daoult_password = False #TODO: check if used
	coffee = False
	eaten = False
	huel = False

	# potential weapons
	selfie = True
	covid = False
	fungus = False
	mbti = False
	hamac_weapon = False

	# quests
	analysis = False
	diploma = False
	hamac_quest = False
	babyfoot = False
	whistleblower = False

	# Allies
	alexis = True
	mathieu = True
	paoletti = False
	holcman = False

	###############################
	# INITIAL SEQUENCE
	###############################
	if DEBUG:
		print('\nINIT')
		print(f'time = {time2hours(time)}; energy={energy}\n')

	# wake-up
	snooze = input('Snooze ? [T/F]')
	if snooze == 'T':
		time += config.snooze_dt
		energy += config.snooze_de
	else:
		time += config.nonsnooze_dt
		energy += config.nonsnooze_de

	if DEBUG:
		print('\nWAKEUP')
		print(f'time = {time2hours(time)}; energy={energy}\n')

	# bike
	bike_fight = input('A velo, se fighter avec un automobiliste ? [T/F]')
	if bike_fight == 'T':
		time += config.bike_fight_dt
		energy += config.bike_fight_de
	else:
		time += config.non_bike_fight_dt
		energy += config.non_bike_fight_de

	if DEBUG:
		print('\nBIKE')
		print(f'time = {time2hours(time)}; energy={energy}\n')


	# arrival
	if time <= config.morning_deadline * 60: # before 9am
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
				time += config.daoult_test_mbti_dt
				mbti = True

	else: # after 10am
		time += config.swann_beer_dt
		mbti = True

	if DEBUG:
		print('\nIBENS ARRIVAL')
		print(f'time = {time2hours(time)}; energy={energy}\n')

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
		print('\nSYSINFO')
		print(f'badge = {badge}')
		print(f'time = {time2hours(time)}; energy={energy}\n')

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
				print(f'montessori talk')
				# montessori talk
				time += config.montessori_talk_dt
				energy += config.montessori_talk_de
			else:
				print(f'hydroponics talk')
				# hydroponics talk
				time += config.hydroponics_talk_dt
				energy += config.hydroponics_talk_de

	if DEBUG:
		print('\n6th FLOOR')
		print(f'covid = {covid}, resistance = {resistance}, daoult_password = {daoult_password}')
		print(f'time = {time2hours(time)}; energy={energy}\n')

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
		print('\nLAB')
		print(f'covid = {covid}, coffee = {coffee}, toilets = {toilets}, alexis = {alexis}')
		print(f'time = {time2hours(time)}; energy={energy}\n')


	# 7th FLOOR
	time += config.floor7_dt

	if DEBUG:
		print('\n7th FLOOR')
		print(f'time = {time2hours(time)}; energy={energy}\n')


	# Analysis
	shifumi_output = shifumi()
	while not shifumi_output:
		energy += config.shifumi_between_games_de
		shifumi_output = shifumi()

	gpu = True


	if DEBUG:
		print('\nSHIFUMI')
		print(f'gpu = {gpu}')
		print(f'time = {time2hours(time)}; energy={energy}\n')


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
		print('\nANALYSIS')
		print(f'analysis = {analysis}, coffee = {coffee}')
		print(f'time = {time2hours(time)}; energy={energy}\n')


	# France & Guillaume encounters
	discuss_france = input('Tu veux discuter de tes problemes avec France? [T/F]')
	if discuss_france == 'T':
		time += config.france_dt
		energy = config.france_e
		huel = True
		hamac_votes.append('france')


	discuss_guillaume = input('Tu veux discuter de tes problemes avec Guillaume? [T/F]')
	if discuss_guillaume == 'T':
		time += config.guillaume_dt
		energy += config.guillaume_de
		hamac_votes.append('guillaume')


	if DEBUG:
		print('\nF&G ENCOUNTERS')
		print(f'hamac_votes = {hamac_votes}')
		print(f'time = {time2hours(time)}; energy={energy}\n')


	assert time <= 14 * 60 # before 2pm
	assert energy > 0
	assert badge
	assert analysis
	assert gpu


	##########################################
	# PARALLEL QUESTS
	##########################################

	while (time < config.end_hour * 60 and energy > 0) and ((not diploma) or (not hamac_quest) or (not babyfoot)): #TODO: check constraints
		
		to_display_menu = display_menu(time, hamac_quest, diploma, babyfoot, eaten)
		menu_choice = input('\n'.join([f'Tape {key} pour {value}' for key, value in to_display_menu.items()]) + '\n')

		# HAMAC
		# 14 people max can vote
		if menu_choice == '0':
			if ('France' in hamac_votes) and not ('Guillaume' in hamac_votes):
				hamac_votes.append('Guillaume')
			
			# TODO: verify hamac_votes has no redundacy
			assert len(hamac_votes) == len(set(hamac_votes))

			print(f'Il y a {len(hamac_votes)} personnes pour le hamac sur 14.')

			# try convince some people
			# TODO: il manque les fioritures la: le sprobas qui changent en fonction de la conversation
			convince_hamac = input("Tu essayes de convaincre Felipe ? [T/F]")
			if convince_hamac == 'T':
				rd = random.random()
				time += config.convince_felipe_dt
				energy += config.convince_felipe_de
				if rd < config.convince_felipe_proba:
					hamac_votes.append('felipe')
					print("Tu as convaincu Felipe.")

			convince_hamac = input("Tu essayes de convaincre Tony ? [T/F]")
			if convince_hamac == 'T':
				rd = random.random()
				time += config.convince_tony_dt
				energy += config.convince_tony_de
				if rd < config.convince_tony_proba:
					hamac_votes.append('tony')
					print("Tu as convaincu Tony.")

			convince_hamac = input("Tu essayes de convaincre Lisa ? [T/F]")
			if convince_hamac == 'T':
				rd = random.random()
				time += config.convince_lisa_dt
				energy += config.convince_lisa_de
				if rd < config.convince_lisa_proba:
					hamac_votes.append('lisa')
					print("Tu as convaincu Lisa.")

			if len(hamac_votes) >= config.n_people_hamac_vote:
				print(f'Quete HAMAC reussie !')
				hamac_weapon = True
				energy += config.winning_hamac_de
			else:
				# couch with auguste
				covid = True
				energy += config.loosing_hamac_de

			time += config.hamac_quest_dt
			hamac_quest = True

			if DEBUG:
				print('\nHAMAC')
				print(f'hamac_votes = {hamac_votes}, hamac = {hamac_weapon}')
				print(f'time = {time2hours(time)}; energy={energy}\n')


		# DIPLOMA
		elif menu_choice == '1':
			if time >= config.admin_deadline * 60:
				# after 6 pm
				time = config.end_hour * 60
				break

			# Lina's signature sequence
			if alexis:
				time += config.if_alexis_lina_dt
			else:
				if time <= config.admin_lina_deadline * 60:
					# before 2 pm
					time = 14 * 60
				time += config.if_not_alexis_lina_dt

			# Paoletti's signature sequence
			if alexis:
				time += config.if_alexis_paoletti_dt
			else:
				time += config.if_not_alexis_paoletti_dt
				resistance = True #TBD

			# Auguste's signature sequence
			if alexis:
				time += config.if_alexis_auguste_dt
			else:
				time += config.if_not_alexis_auguste_dt

			# diploma quest achieved
			diploma = True

			# meet with Felipe
			felipe_badge = True

			if DEBUG:
				print('\nDIPLOMA')
				print(f'diploma = {diploma}, resistance = {resistance}')
				print(f'time = {time2hours(time)}; energy={energy}\n')


		# BABYFOOT
		elif menu_choice == '2':
			if fungus:
				energy += config.if_fungus_de

			# compliment Maxime and Nikita
			hamac_votes.extend(['nikita', 'maxime'])

			if resistance:
				#TBD: verify she has high chances to get resistance: 
				# - from talk with pierre and jerome
				# - from paloetti signature
				daoult_password = True

			time += config.baby_dt

			if resistance: 
				# choose between paoletti and holcman
				paoletti_vs_holcman = input('De Pierre Paloetti et David Holcman, qui choisis-tu comme allie contre Daoult? [0/1]')
				if paoletti_vs_holcman == '0':
					# choose paoletti
					paoletti = True
				else:
					holcman = False

			# babyfoot quest achieved
			babyfoot = True

			if DEBUG:
				print('\nBABYFOOT')
				print(f'babyfoot = {babyfoot}, paoletti = {paoletti}, holcman = {holcman},')
				print(f'daoult_password = {daoult_password}, resistance = {resistance}, fungus = {fungus}')
				print(f'time = {time2hours(time)}; energy = {energy}\n')

		# LUNCH
		elif menu_choice == '3':
			if time <= config.tony_lunch_deadline * 60:
				# lunch with Tony
				selfie = True
			else:
				# eat with Solene and Elise
				hamac_votes.extend(['elise', 'raphael', 'solene'])
				# cure fungal infection?
				fungal_choice = input("Pour ton champignon, tu suis le conseil d'Elise [0] ou de Solene[1] ?") 
				if fungal_choice == '0':
					# elise: the fungal infection grows worse
					fungus = True
				else:
					#solene: the fungal infection is cured
					energy += config.fungal_de

			time += config.lunch_dt
			eaten = True

			if DEBUG:
				print('\nLUNCH')
				print(f'hamac_votes = {hamac_votes}, selfie={selfie}')
				print(f'time = {time2hours(time)}; energy={energy}\n')

		# NAP
		else: #if menu_choice == '4':
			energy += config.nap_de
			time += config.nap_dt

			if DEBUG:
				print('\nNAP')
				print(f'time = {time2hours(time)}; energy={energy}\n')
		

	if time >= config.end_hour * 60 or energy < 0:
		print('GAME OVER ! Recommence !')
		return

	assert babyfoot
	assert hamac_quest
	assert diploma
	assert (covid or fungus or hamac_weapon)


	########################################
	# WHISTLEBLOWER QUEST
	########################################

	office_check = input("Choisis-tu d'aller inspecter le bureau de Daoult [0], de Pierre Paoletti [1], de David Holcman [2] ou aucun [3]?")
	if office_check == '0':
		if mbti:
			print("Tu trouves qqchose chez Daoult")
			energy += config.if_mbti_daoult_office_de
		else:
			print("Tu ne trouves rien chez Daoult")
			energy += config.not_mbti_adoult_office_de

	elif office_check =='1':
		if paoletti:
			print("Ton allie Paoletti est mechant")
			energy += allie_is_evil_de
		else:
			print("Tu ne trouves rien chez Paoletti")
	elif office_check == '2':
		if paoletti:
			print("Tu ne trouves rien chez Holcman")
		else:
			print("Ton allie Holmcan est mechant")
			energy += allie_is_evil_de
	
	if office_check != '3':	
		time += config.whistleblower_dt
		if DEBUG:
			print('\nWHISTLEBLOWER')
			print(f'time = {time2hours(time)}; energy={energy}\n')


	whistleblower_choice = input('Fais tu fuiter dans mediapart le scandale du corona-cola ? [T/F]')
	if whistleblower_choice == 'T':
		whistleblower = True


	##########################################
	# FINAL QUEST
	##########################################

	if time >= config.end_hour * 60 or energy < 0:
		print('GAME OVER ! Recommence !')
		return

	if whistleblower:
		allie_confrontation = input("Confrontes-tu ton allie ? [T/F]")
		if allie_confrontation == 'T':
			energy += config.confrontation_allie_de

		if huel:
			huel_choice = input("Veux-tu un peu de huel? [T/F]")
			if huel_choice == 'T':
				energy = 100

		daoult_proposition =  input("Daoult te propose un poste permanent avec mobilite. Tu acceptes ? [T/F]")
		energy += config.daoult_proposition_de
		if daoult_proposition == 'T':
			if energy >= config.trust_daoult_energy_threshold:
				# epilogue 1
				print("Tu as gagne - Sort of")
				return
			else:
				print("GAME OVER! Recommence !")
				return
		else:
			if energy >= config.dont_trust_daoult_energy_threshold:
				daoult_weapon_choice = input(daoult_attack(covid, hamac_weapon, fungus))
				if daoult_weapon_choice == '0':
					print("Tu tues Daoult avec le covid")
					# epilogue 2
				elif daoult_weapon_choice == '1':
					print("Tu emprisonnes Daoult avec le piege hamac")
					# epilogue 3
				elif daoult_weapon_choice == '2':
					print("Tu contamines Daoult avec ton champignon")
					# epilogue 4

					allie_choice = input("Choisis-tu de changer ton choix pour le prochain directeur d'institut ? [T/F]")
					if allie_choice == 'T':
						# exchange
						paloetti = not paloetti
						holcman = not holcman

					print("Tu as gagne - Sort of")
					return

			else:
				print("GAME OVER! Recommence !")
				return

	else:
		# not whistleblower

		# fight with allie
		lie_or_not = input("Tu n'as pas fait fuiter les infos. Ments tu a ton allie ? [T/F]")
		if lie_or_not == 'T':
			# need to fight
			energy += config.lie_allie_fight_de
			# loose allie
			paoletti = False
			holcman = False
		else:
			energy += config.dont_lie_allie_fight_de

		if energy < 0:
			print("GAME OVER! Recommence !")
			return	

		if huel:
			huel_choice = input("Veux-tu un peu de huel? [T/F]")
			if huel_choice == 'T':
				energy = 100

		if paoletti or holcman:
			# she still has an allie
			fight_daoult_or_both = input("Choisis-tu d'attaquer Daoult [0] ou les deux [1] ?")
			if fight_daoult_or_both == '0':
				# epilogue 4
				print("Tu as gagne - Sort of")
				return
			elif fight_daoult_or_both == '1':
				# fight both
				# not enough energy!
				print("GAME OVER! Recommence !")
				return	

		else:
			# no more allie
			if (covid and energy >= config.if_covid_convince_daoult_energy_threshold):
				# epilogue 6
				print("Tu as gagne - Sort of")
				return
			elif (not covid and energy >= config.not_covid_convince_daoult_energy_threshold):
				# epilogue 7
				print("Tu as gagne - Sort of")
				return
			else:
				# not enough energy!
				print("GAME OVER! Recommence !")
				return

	if DEBUG:
		print("/!\\ No return - Pb")


if __name__ == '__main__':
	game(DEBUG=True)


