# CONFIG RPG TIF

#########################
# Initial sequence
#########################

# wake-up
snooze_dt                 = -120
nonsnooze_dt              = -30
snooze_de                 = 0
nonsnooze_de              = -10

# IBENS arrival
bike_fight_dt             = -30
bike_fight_de             = 5 - 2
non_bike_fight_dt         = -10
non_bike_fight_de         = -2

# Daoult encounter
daoult_talk_dt            = -5
daoult_fight_dt           = -5 # about SUVs
daoult_fight_de           = -5
daoult_test_mbti_proba    = 0.7
daoult_test_mbti_dt       = -10
daoult_test_mbti_dchances = 0.3

# Swann encounter
swann_beer_dt             = -60

# Sysinfo
pv_convincing_proba       = 0.5
pv_dt                     = -20
after_pv_dt               = -1
phiphuong_dt              = -40
phiphuong_de              = -10
bilel_dt                  = -6

# 6th floor kitchen
auguste_meeting_dt        = -60
auguste_meeting_de        = -20
resistance_talk_dt        = -30
montessori_talk_dt        = -5
montessori_talk_de        = -20
hydroponics_talk_dt       = -60
hydroponics_talk_de       = 20

# arrival in the lab
plants_dt                 = -10
coffee_dt                 = -10
coffee_de                 = 20
poop_dt                   = -10
poop_talk_dt              = -10
poop_constipated_de       = -10
poop_email_dt             = -20
poop_email_de             = -5

# Auguste email
auguste_email_answer_dt   = -15

# 7th floor
floor7_dt                 = -20

# Shifumi
shifumi_between_games_dt  = -5
# pierre, feuille, ciseaux
shifumi_truth_table       = [[-1, 0,  1],
							 [1, -1,  0],
							 [0,  1, -1]] 

# analysis run
analysis_if_coffee_dt     = -30
analysis_if_coffee_de     = 10
promise_mathieu_dt        = -60
non_promise_mathieu_dt    = -90
analysis_de               = 30

# France encounter
france_e                  = 100      
france_dt                 = -20

# Guillauem encoutner
guillaume_dt              = -2 * 60 # 2 hours
guillaume_de              = -20


#############################
# PARALLEL QUESTS
#############################

