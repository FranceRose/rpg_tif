# CONFIG RPG TIF

# times "dt" are in minutes (game is 16 hours total)
# energy is on a scale from 1 to 100
# dt and de terms would be a penalty if negative, and a bonus if positive
# probas and chances are between 0 and 1 

#######################
# GLOBAL
######################

end_hour = 19 # 7 pm
start_hour = 8 # 8 am

#########################
# Initial sequence
#########################

# wake-up
snooze_dt                 = 60
nonsnooze_dt              = 10
snooze_de                 = 0
nonsnooze_de              = -10
wakeup_proba              = 0.5

# IBENS arrival
bike_fight_dt             = 15
bike_fight_de             = 5 - 2
non_bike_fight_dt         = 5
non_bike_fight_de         = -2

morning_deadline          = 9

# Daoult encounter
daoult_talk_dt            = 10
daoult_fight_dt           = 10 # about SUVs
daoult_fight_de           = -5
daoult_test_mbti_proba    = 0.7
daoult_test_mbti_dt       = 10

# Swann encounter
swann_beer_dt             = 45

# Sysinfo
pv_convincing_proba       = 0.5
convince_pv_de            = -10
pv_dt                     = 15
after_pv_dt               = 5
phiphuong_dt              = 25
phiphuong_de              = -20
bilel_dt                  = 5

# 6th floor kitchen
auguste_meeting_dt        = 30
auguste_meeting_de        = -20
resistance_talk_dt        = 20
montessori_talk_dt        = 10
montessori_talk_de        = -5
hydroponics_talk_dt       = 30
hydroponics_talk_de       = 20

# arrival in the lab
plants_dt                 = 5
coffee_dt                 = 5
coffee_de                 = 20
poop_dt                   = 5
poop_talk_dt              = 10
poop_constipated_de       = -5
poop_email_dt             = 5
poop_email_de             = -5

# Auguste email
auguste_email_answer_dt   = 5

# 7th floor
floor7_dt                 = 30

# Shifumi
shifumi_between_games_dt  = 5
# pierre, feuille, ciseaux
shifumi_truth_table       = [[-1, 0,  1],
							 [1, -1,  0],
							 [0,  1, -1]] 

# analysis run
analysis_if_coffee_dt     = 30
analysis_if_coffee_de     = 10
promise_mathieu_dt        = 45
non_promise_mathieu_dt    = 60
analysis_de               = 30

# France encounter
france_e                  = 100      
france_dt                 = 20

# Guillauem encoutner
guillaume_dt              = 1 * 60 # 1 hour
guillaume_de              = -20


#############################
# PARALLEL QUESTS
#############################

# menu parameters
diploma_deadline         = 17 # 3pm
lunch_deadline           = 15 # 3pm

# lunch
lunch_dt                 = 60
fungal_de                = 10
tony_lunch_deadline      = 12

# hamac
hamac_quest_dt           = 30
n_people_hamac_vote      = 7
convince_felipe_proba    = 0.7
convince_felipe_dt       = 5
convince_felipe_de       = -5
convince_tony_dt         = 5
convince_tony_de         = -5
convince_tony_proba      = 0.5
convince_lisa_dt         = 10
convince_lisa_de         = -15
convince_lisa_proba      = 0.3
winning_hamac_de         = 30
loosing_hamac_de         = -30

# nap
nap_dt                   = 30
nap_de                   = 30

# admin
admin_deadline           = 17 # 5 pm
admin_lina_deadline      = 14 # 2 pm
if_alexis_lina_dt        = 5
if_alexis_lina_de        = 0
if_alexis_paoletti_dt    = 5
if_alexis_paoletti_de    = 0
if_alexis_auguste_dt     = 5
if_alexis_auguste_de     = 0
if_not_alexis_lina_dt    = 15
if_not_alexis_lina_de    = 5
if_not_alexis_paoletti_dt = 15
if_not_alexis_paoletti_de = 5
if_not_alexis_auguste_dt = 15
if_not_alexis_auguste_de = 2

# babyfoot
if_fungus_de             = -50
baby_dt                  = 2 * 60

# whistleblower
whistleblower_dt         = 2 * 60
if_mbti_daoult_office_de = 20
not_mbti_adoult_office_de = -20
allie_is_evil_de         = -50

# final quest
confrontation_allie_de  = -75
daoult_proposition_de   = -20
trust_daoult_energy_threshold = 20
dont_trust_daoult_energy_threshold = 50
lie_allie_fight_de       = -50
dont_lie_allie_fight_de  = -25
if_covid_convince_daoult_energy_threshold = 80
not_covid_convince_daoult_energy_threshold = 60
