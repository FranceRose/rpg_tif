# CONFIG RPG TIF

# times "dt" are in minutes (game is 16 hours total)
# energy is on a scale from 1 to 100
# dt and de terms would be a penalty if negative, and a bonus if positive
# probas and chances are between 0 and 1 

#########################
# Initial sequence
#########################

# wake-up
snooze_dt                 = -60
nonsnooze_dt              = -10
snooze_de                 = 0
nonsnooze_de              = -10

# IBENS arrival
bike_fight_dt             = -15
bike_fight_de             = 5 - 2
non_bike_fight_dt         = -5
non_bike_fight_de         = -2

# Daoult encounter
daoult_talk_dt            = -5
daoult_fight_dt           = -5 # about SUVs
daoult_fight_de           = -5
daoult_test_mbti_proba    = 0.7
daoult_test_mbti_dt       = -10
daoult_test_mbti_dchances = 0.3

# Swann encounter
swann_beer_dt             = -30

# Sysinfo
pv_convincing_proba       = 0.5
pv_dt                     = -15
after_pv_dt               = -1
phiphuong_dt              = -25
phiphuong_de              = -10
bilel_dt                  = -5

# 6th floor kitchen
auguste_meeting_dt        = -20
auguste_meeting_de        = -20
resistance_talk_dt        = -10
montessori_talk_dt        = -5
montessori_talk_de        = -5
hydroponics_talk_dt       = -20
hydroponics_talk_de       = 20

# arrival in the lab
plants_dt                 = -5
coffee_dt                 = -5
coffee_de                 = 20
poop_dt                   = -5
poop_talk_dt              = -5
poop_constipated_de       = -5
poop_email_dt             = -5
poop_email_de             = -5

# Auguste email
auguste_email_answer_dt   = -5

# 7th floor
floor7_dt                 = -10

# Shifumi
shifumi_between_games_de  = -2
# pierre, feuille, ciseaux
shifumi_truth_table       = [[-1, 0,  1],
							 [1, -1,  0],
							 [0,  1, -1]] 

# analysis run
analysis_if_coffee_dt     = -30
analysis_if_coffee_de     = 10
promise_mathieu_dt        = -45
non_promise_mathieu_dt    = -60
analysis_de               = 30

# France encounter
france_e                  = 100      
france_dt                 = -20

# Guillauem encoutner
guillaume_dt              = -1 * 60 # 1 hour
guillaume_de              = -20


#############################
# PARALLEL QUESTS
#############################

# menu parameters
diploma_deadaline        = 15 # 3pm
lunch_deadline           = 15 # 3pm

# lunch
lunch_dt                 = 30
fungal_chances           = 0.1
fungal_de                = 10

# hamac
n_people_hamac_vote      = 7
convince_felipe_proba    = 0.7
convince_felipe_dt       = -5
convince_felipe_de       = -5
convince_tony_dt         = -5
convince_tony_de         = -5
convince_felipe_proba    = 0.5
convince_lisa_dt         = -10
convince_lisa_de         = -15
convince_lisa_proba      = 0.3
winning_hamac_de         = 30
loosing_hamac_de         = -30
