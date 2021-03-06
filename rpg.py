# MAIN SCRIPT RPG TIF
import sys
import rpg_config as config
from rpg_functools import *
import random

from os import system, name

def credits():
    clear_screen()
    print(p_color("narration/credits.txt"))
    input()
    clear_screen()
    return


def launch_video():
    open_file('./narration/rise_of_champetier.mp4')
    clear_screen()


def menu_principal(**kwargs):
    while (True):
        menu_choice = check_input(p_color('narration/menu_principal.txt'),
                                  ['1', '2', '3', '4'])
        if menu_choice == "1":
            launch_video()
        if menu_choice == "2":
            clear_screen()
            game(**kwargs)
        if menu_choice == "3":
            credits()
        if menu_choice == "4":
            sys.exit(0)
        clear_screen()


def die():
    clear_screen()
    print(p_color(
        "[RED]CATASTROPHE ! \n[GREEN]Tiphaine[DEFAULT] a [RED]crevé[DEFAULT].\n"
        "Elle a visiblement fait de très [RED]mauvais[DEFAULT] choix... Il faut recommencer"),
          file=False)
    input()
    clear_screen()
    menu_principal()


def game(DEBUG=False, **kwargs):
    # global variables
    time = config.start_hour * 60 # starts at 8 am
    energy = Energy(100)

    # needed for advancement
    badge = False
    gpu = False
    felipe_badge = False

    hamac_votes = ['ouardia', 'tiphaine', 'alexis']
    daoult_password = False  # TODO: check if used
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
    paoletti = False
    holcman = False

    ###############################
    # PROLOGUE
    ###############################
    # Star Wars Init
    input(p_color("narration/intro.txt"))
    clear_screen()
    # TBD: remove if video

    # Retour
    input(p_color("narration/retour.txt"))
    clear_screen()

    # Tutoriel
    input(p_color("narration/tutoriel.txt"))
    clear_screen()

    ###############################
    # INITIAL SEQUENCE
    ###############################
    print_INFO(time, energy)


    # wake-up
    snooze = check_input(p_color("narration/matin/matin.txt"), ['T', 'F'])
    if snooze == 'T':
        time += config.snooze_dt
        energy += config.snooze_de

        print_result_action(config.snooze_dt, config.snooze_de)
        print(p_color("narration/matin/matin_snooze.txt"))

    else:
        rd = random.random()
        if rd <= config.wakeup_proba:
            # Tif manages to wakeup
            time += config.nonsnooze_dt
            energy += config.nonsnooze_de

            print_result_action(config.nonsnooze_dt, config.nonsnooze_de)
            print(p_color("narration/matin/matin_lever_success.txt"))

        else:
            # fail
            time += config.snooze_dt
            energy += config.nonsnooze_de

            print_result_action(config.snooze_dt, config.nonsnooze_de)

            print(p_color("narration/matin/matin_lever_fail.txt"))
    print_INFO(time, energy)
    input()
    clear_screen()

    # bike
    bike_fight = check_input(p_color("narration/bike/bike.txt"), ['T', 'F'])
    if bike_fight == 'T':
        time += config.bike_fight_dt
        energy += config.bike_fight_de

        print_result_action(config.bike_fight_dt, config.bike_fight_de)
        print(p_color("narration/bike/bike_fight.txt"))
    else:
        time += config.non_bike_fight_dt
        energy += config.non_bike_fight_de

        print(p_color("narration/bike/bike_no_fight.txt"))
        print_result_action(config.non_bike_fight_dt, config.non_bike_fight_de)

    print_INFO(time, energy)
    input()
    clear_screen()
    # arrival
    if time <= config.morning_deadline * 60:  # before 9am
        # meeting with Daoult
        time += config.daoult_talk_dt
        print(p_color("narration/arrivee_ibens/daoult/daoult.txt"))
        print_result_action(config.daoult_talk_dt, 0)
        input()

        if bike_fight == 'T':
            time += config.daoult_fight_dt
            energy += config.daoult_fight_de

            print(p_color(
                "narration/arrivee_ibens/daoult/daoult2_si_agression.txt"))
            print_result_action(config.daoult_fight_dt, config.daoult_fight_de)
        else:
            # daoult does take the MBTI test
            time += config.daoult_test_mbti_dt
            mbti = True

            print(p_color(
                "narration/arrivee_ibens/daoult/daoult2_si_mbti.txt"))
            print_result_action(config.daoult_test_mbti_dt, 0)

    else:  # after 10am
        time += config.swann_beer_dt
        mbti = True

        print(p_color(
            "narration/arrivee_ibens/swann/swann.txt"))
        print_result_action(config.swann_beer_dt, 0)

    print_INFO(time, energy)
    input()
    clear_screen()

    # sysinfo
    convince_pv = check_input(p_color("narration/sysinfo/pv.txt"), ["T", "F"])
    wait_sysinfo = False
    if convince_pv == 'T':
        rd = random.random()
        energy += config.convince_pv_de
        time += config.pv_dt
        if rd <= config.pv_convincing_proba:
            # pv is convinced!
            badge = True

            print(p_color("narration/sysinfo/pv_after.txt"))
        else:
            # local var
            wait_sysinfo = True
            print(p_color("narration/sysinfo/pv_not_convinced.txt"))
        print_result_action(config.pv_dt, config.convince_pv_de)

    if convince_pv == 'F' or wait_sysinfo:
        # wait
        time += config.after_pv_dt
        print_result_action(config.after_pv_dt, 0)
        input()

        phiphuong = check_input(
            p_color("narration/sysinfo/deal_w_phiphuong.txt"),
            ['T', 'F'])
        if phiphuong == 'T':
            time += config.phiphuong_dt
            energy += config.phiphuong_de
            badge = True

            print(p_color("narration/sysinfo/phiphuong_after.txt"))
            print_result_action(config.phiphuong_dt,
                                config.phiphuong_de)
        else:
            time += config.bilel_dt
            badge = True

            print(p_color("narration/sysinfo/bilel.txt"))
            print_result_action(config.bilel_dt, 0)

    print_INFO(time, energy)
    input()
    clear_screen()

    # 6th floor
    meeting_auguste = check_input(
        p_color("narration/sixth_floor_kitchen/arrival.txt"), ['T', 'F'])
    if meeting_auguste == 'T':
        time += config.auguste_meeting_dt
        energy += config.auguste_meeting_de
        covid = True

        print(p_color("narration/sixth_floor_kitchen/meeting_auguste.txt"))
        print_result_action(config.auguste_meeting_dt,
                            config.auguste_meeting_de)

    else:
        # stay with Pierre and Jerome
        listen_pj = check_input(
            p_color("narration/sixth_floor_kitchen/choice_pierrejerome.txt"),
            ['T', 'F'])
        if listen_pj == 'T':
            time += config.resistance_talk_dt
            daoult_password = True

            print(
                p_color(
                    "narration/sixth_floor_kitchen/listen_pierrejerome.txt"))
            print_result_action(config.resistance_talk_dt, 0)
        else:
            rd = random.random()
            if rd < 0.5:
                # montessori talk
                time += config.montessori_talk_dt
                energy += config.montessori_talk_de

                print(p_color(
                    "narration/sixth_floor_kitchen/montessori.txt"))
                print_result_action(config.montessori_talk_dt,
                                    config.montessori_talk_de)

            else:
                # hydroponics talk
                time += config.hydroponics_talk_dt
                energy += config.hydroponics_talk_de

                print(p_color(
                    "narration/sixth_floor_kitchen/hydroponics.txt"))
                print_result_action(config.hydroponics_talk_dt,
                                    config.hydroponics_talk_de)

    print_INFO(time, energy)
    input()
    clear_screen()

    # in the lab
    lab_choice = check_input(p_color("narration/bureau/bureau.txt"),
                             ['1', '2', '3'])
    # local variable toilets
    toilets = False
    if lab_choice == '3':
        # plants
        time += config.plants_dt
        print(p_color("narration/bureau/plantes.txt"))
        print_result_action(config.plants_dt, 0)

    elif lab_choice == '1':
        coffee = True
        energy += config.coffee_de
        time += config.coffee_dt

        print_result_action(config.coffee_dt,
                            config.coffee_de)  # TODO: check if order is ok between the 2 prints
        lab_choice = check_input(p_color("narration/bureau/cafe.txt"),
                                 ['1', '2'])

    if lab_choice == '2':
        # caca
        toilets = True
        rd = random.random()
        if rd < 0.5:
            # discuss her poop
            time += config.poop_talk_dt

            poop_email = check_input(
                p_color("narration/bureau/caca_explication.txt"),
                ['T', 'F'])
            print_result_action(config.poop_talk_dt + config.poop_dt, 0)
        else:
            energy += config.poop_constipated_de

            poop_email = check_input(
                p_color("narration/bureau/caca_constipee.txt"),
                ['T', 'F'])
            print_result_action(config.poop_dt, config.poop_constipated_de)

        time += config.poop_dt

        if poop_email == 'T':
            time += config.poop_email_dt
            energy += config.poop_email_de

            print_result_action(config.poop_dt, config.poop_constipated_de)
            check_input(p_color("narration/bureau/reponse_mail.txt"), ['1'])
        else:
            check_input(
                p_color("narration/bureau/toilettes_degueues_passer_outre.txt"),
                ['1'])

    if not toilets:
        # Tif asphyxiates Alexis, he is not her allie anymore
        print(p_color("narration/bureau/asphyxier_alexis.txt"))
        alexis = False
        hamac_votes.remove('alexis')

    if DEBUG:
        print("\nIN THE LAB\n")
        print(f"alexis = {alexis}, hamac_votes = {hamac_votes}")

    print_INFO(time, energy)
    input()
    clear_screen()

    # email auguste
    ignore_email_auguste = check_input(
        p_color("narration/bureau/mail_auguste.txt"),
        ['T', 'F'])

    if ignore_email_auguste == 'T':
        time += config.auguste_email_answer_dt
        print(p_color("narration/bureau/ignorer_auguste.txt"))

    else:
        covid = True

        print(p_color("narration/bureau/engueuler_auguste.txt"))
        print_result_action(config.auguste_email_answer_dt, 0)

    if DEBUG:
        print('\nLAB')
        print(
            f'covid = {covid}, coffee = {coffee}, toilets = {toilets}, alexis = {alexis}')

    print_INFO(time, energy)
    input()
    clear_screen()

    # 7th FLOOR
    time += config.floor7_dt
    print(p_color("narration/seventh_floor/seventh_floor_data.txt"))
    print_result_action(config.floor7_dt, 0)

    print_INFO(time, energy)
    input()
    clear_screen()

    # Analysis
    print(p_color("narration/gpu/gpu.txt"))
    shifumi_output = shifumi()
    while not shifumi_output:
        time += config.shifumi_between_games_dt
        print_result_action(config.shifumi_between_games_dt, 0)
        shifumi_output = shifumi()

    gpu = True

    if DEBUG:
        print('\nSHIFUMI')
        print(f'gpu = {gpu}')

    print_INFO(time, energy)
    input()
    clear_screen()

    # Analysis
    check_input(p_color("narration/analyse/question_troll.txt"),
                ['1', '2', '3', '4'])

    if coffee:
        time += config.analysis_if_coffee_dt
        energy -= config.analysis_if_coffee_de

        print(p_color("narration/analyse/avec_cafe.txt"))
        print_result_action(config.analysis_if_coffee_dt,
                            config.analysis_if_coffee_de)
    else:
        promise_mathieu = check_input(
            p_color("narration/analyse/sans_cafe.txt"),
            ['T', 'F'])

        if promise_mathieu == 'T':
            time += config.promise_mathieu_dt
            energy -= config.analysis_de
            # mathieu is an allie
            hamac_votes.append('mathieu')
            print(p_color("narration/analyse/gentille_avec_mathieu.txt"))
            print_result_action(config.promise_mathieu_dt,
                                config.analysis_de)
        else:
            time += config.non_promise_mathieu_dt
            energy -= config.analysis_de
            print(p_color("narration/analyse/pasgentille_avec_mathieu.txt"))
            print_result_action(config.promise_mathieu_dt, config.analysis_de)

    analysis = True

    if DEBUG:
        print('\nANALYSIS')
        print(f'analysis = {analysis}, coffee = {coffee}')

    print_INFO(time, energy)
    input()
    clear_screen()

    # Discussion with Alexis about admin problems
    print(p_color("narration/convaincre_le_monde/interlude.txt"))
    if alexis:
        print(
            p_color("narration/convaincre_le_monde/answer_alexis_if_caca.txt"))
    else:
        print(p_color(
            "narration/convaincre_le_monde/answer_alexis_if_not_caca.txt"))
    input()

    # France & Guillaume encounters
    discuss_france = check_input(p_color(
        "narration/convaincre_le_monde/discussion_france_beginning.txt"),
                                 ['T', 'F'])
    if discuss_france == 'T':
        print(p_color(
            "narration/convaincre_le_monde/discussion_france_follow.txt"))
        print_result_action(config.france_dt, config.france_e - energy.e)

        time += config.france_dt
        energy = Energy(config.france_e)
        huel = True
        hamac_votes.append('france')

    print_INFO(time, energy)
    input()
    clear_screen()

    discuss_guillaume = check_input(p_color(
        "narration/convaincre_le_monde/choice_discussion_guillaume.txt"),
                                    ['T', 'F'])
    if discuss_guillaume == 'T':
        time += config.guillaume_dt
        energy += config.guillaume_de
        hamac_votes.append('guillaume')

        print(p_color("narration/convaincre_le_monde/discussion_guillaume.txt"))
        print_result_action(config.guillaume_dt, config.guillaume_de)

    if DEBUG:
        print('\nF&G ENCOUNTERS')
        print(f'hamac_votes = {hamac_votes}')

    print_INFO(time, energy)
    input()

    if not all([time <= 14 * 60, energy.e > 0, badge, analysis, gpu]):
        clear_screen()
        print(p_color("narration/fail_checkpoint.txt"))
        input()
        clear_screen()
        return False

    ##########################################
    # PARALLEL QUESTS
    ##########################################

    while (time < config.end_hour * 60 and energy > 0) and (
            (not diploma) or (not hamac_quest) or (
    not babyfoot)):  # TODO: check constraints
        clear_screen()

        print('\n\n')
        print_INFO(time, energy)
        print('\n\nQue faire ?\n\n')

        if DEBUG:
            print(
                f"diplome = {diploma}, hamac_quest = {hamac_quest}, babyfoot = {babyfoot}")

        to_display_menu = display_menu(time, hamac_quest, diploma, babyfoot,
                                       eaten)
        menu_choice = check_input('\n'.join(
            [f'- {value} [{key}]' for key, value in
             to_display_menu.items()]) + '\n',
                                  [str(k) for k in to_display_menu.keys()])

        # HAMAC
        # 14 people max can vote
        if menu_choice == '0':
            ### HAMAC_QUEST
            clear_screen()

            print(p_color("narration/quetes_paralleles/hamac/HAMAC.txt"))

            if ('France' in hamac_votes) and not ('Guillaume' in hamac_votes):
                hamac_votes.append('Guillaume')

            # TODO: verify hamac_votes has no redundacy
            assert len(hamac_votes) == len(set(hamac_votes))

            print(f'Il y a {len(hamac_votes)} personnes pour le hamac sur 14.')

            # try convince some people
            # TODO: il manque les fioritures la: les probas qui changent en fonction de la conversation
            print(p_color("narration/quetes_paralleles/hamac/FELIPE.txt"))
            convince_hamac = check_input("", ["T", "F"])
            if convince_hamac == 'T':
                rd = random.random()
                time += config.convince_felipe_dt
                energy += config.convince_felipe_de

                if rd < config.convince_felipe_proba:
                    hamac_votes.append('felipe')
                    print(p_color("narration/quetes_paralleles/hamac/FELIPE_success_convaincre.txt"))
                else:
                    print(p_color("narration/quetes_paralleles/hamac/FELIPE_fail_convaincre.txt"))

                print_result_action(config.convince_felipe_dt, config.convince_felipe_de)
                print_INFO(time, energy)

            else:
                print(p_color("narration/quetes_paralleles/hamac/FELIPE_ignorer.txt"))
            input("")

            clear_screen()
            print(p_color("narration/quetes_paralleles/hamac/TONI.txt"))
            convince_hamac = check_input("", ["T", "F"])
            if convince_hamac == 'T':
                rd = random.random()
                time += config.convince_tony_dt
                energy += config.convince_tony_de
                if rd < config.convince_tony_proba:
                    hamac_votes.append('tony')
                    print(p_color("narration/quetes_paralleles/hamac/TONI_success_convaincre.txt"))
                else:
                    print(p_color("narration/quetes_paralleles/hamac/TONI_fail_convaincre.txt"))

                print_result_action(config.convince_tony_dt, config.convince_tony_de)
                print_INFO(time, energy)

            else:
                print(p_color("narration/quetes_paralleles/hamac/TONI_ignorer.txt"))
            input("")

            clear_screen()
            print(p_color("narration/quetes_paralleles/hamac/LISA.txt"))
            convince_hamac = check_input("", ["T", "F"])
            if convince_hamac == 'T':
                rd = random.random()
                time += config.convince_lisa_dt
                energy += config.convince_lisa_de

                if rd < config.convince_lisa_proba:
                    hamac_votes.append('lisa')
                    print(p_color("narration/quetes_paralleles/hamac/LISA_success_convaincre.txt"))
                else:
                    print(p_color("narration/quetes_paralleles/hamac/LISA_fail_convaincre.txt"))

                print_result_action(config.convince_lisa_dt, config.convince_lisa_de)

            else:
                print(p_color("narration/quetes_paralleles/hamac/LISA_ignorer.txt"))
            input("")

            clear_screen()

            print(p_color("narration/quetes_paralleles/hamac/vote.txt"))
            input("")

            if len(hamac_votes) >= config.n_people_hamac_vote:
                print(p_color("narration/quetes_paralleles/hamac/final_success.txt"))
                hamac_weapon = True
                energy += config.winning_hamac_de
                time += config.hamac_quest_dt
                print_result_action(config.hamac_quest_dt, config.winning_hamac_de)
            else:
                print(p_color("narration/quetes_paralleles/hamac/final_failed.txt"))
                # couch with auguste
                covid = True
                energy += config.loosing_hamac_de
                time += config.hamac_quest_dt
                print_result_action(config.hamac_quest_dt, config.loosing_hamac_de)

            hamac_quest = True

            if DEBUG:
                print('\nHAMAC')
                print(f'hamac_votes = {hamac_votes}, hamac = {hamac_weapon}')

            print_INFO(time, energy)
            input('')
            clear_screen()

        # DIPLOMA
        elif menu_choice == '1':
            diploma_dir = "narration/diploma/"

            if DEBUG:
                print(f"time = {time}, {config.diploma_deadline * 60}, alexis = {alexis}")
            if time >= config.diploma_deadline * 60:
                # after 5 pm
                print(p_color(diploma_dir + "vigile.txt"))
                input()
                clear_screen()
                return False

            # Lina's signature sequence
            if alexis:
                time += config.if_alexis_lina_dt
                energy += config.if_alexis_lina_de
                print(p_color(diploma_dir + "lina_with_alexis.txt"))
                print_result_action(config.if_alexis_lina_dt, config.if_alexis_lina_de)
            else:
                if time <= config.admin_lina_deadline * 60:
                    # before 2 pm
                    print(p_color(diploma_dir + "wait_for_lina.txt"))
                    print_result_action(config.admin_lina_deadline * 60 - time, 0)
                    time = config.admin_lina_deadline * 60

                time += config.if_not_alexis_lina_dt
                energy += config.if_not_alexis_lina_de
                print(p_color(diploma_dir + "lina_wo_alexis.txt"))
                print_result_action(config.if_not_alexis_lina_dt, config.if_not_alexis_lina_de)

            print_INFO(time, energy)
            input()
            clear_screen()


            # Auguste's signature sequence
            if alexis:
                time += config.if_alexis_auguste_dt
                energy += config.if_alexis_auguste_de
                print(p_color(diploma_dir + "auguste_with_alexis.txt"))
                print_result_action(config.if_alexis_auguste_dt, config.if_alexis_auguste_de)
            else:
                time += config.if_not_alexis_auguste_dt
                energy += config.if_not_alexis_auguste_de
                print(p_color(diploma_dir + "auguste_wo_alexis.txt"))
                print_result_action(config.if_not_alexis_auguste_dt, config.if_not_alexis_auguste_de)

            print_INFO(time, energy)
            input()
            clear_screen()

            # Paoletti's signature sequence
            if alexis:
                time += config.if_alexis_paoletti_dt
                energy += config.if_alexis_paoletti_de
                print(p_color(diploma_dir + "paoletti_with_alexis.txt"))
                print_result_action(config.if_alexis_paoletti_dt, config.if_alexis_paoletti_de)
            else:
                time += config.if_not_alexis_paoletti_dt
                energy += config.if_not_alexis_paoletti_de
                print(p_color(diploma_dir + "paoletti_wo_alexis.txt"))
                print_result_action(config.if_not_alexis_paoletti_dt, config.if_not_alexis_paoletti_de)

            print_INFO(time, energy)
            input()
            clear_screen()

            # diploma quest achieved
            diploma = True

            print(p_color(diploma_dir + "rencontre_felipe.txt"))
            # meet with Felipe
            felipe_badge = True

            input()
            clear_screen()


        # BABYFOOT
        elif menu_choice == '2':
            print(p_color("narration/quetes_paralleles/babyfoot/babyfoot_tournament.txt"))

            if fungus:
                print(p_color("narration/quetes_paralleles/babyfoot/fungus_handicap.txt"))
                energy += config.if_fungus_de
                print_result_action(0, config.if_fungus_de)
            else:
                print(p_color("narration/quetes_paralleles/babyfoot/fungus_no_handicap.txt"))

            # compliment Maxime and Nikita


            hamac_votes.extend(['nikita', 'maxime'])
            print(p_color("narration/quetes_paralleles/babyfoot/maxime_nikita.txt"))

            daoult_password = True

            time += config.baby_dt

            print(p_color("narration/quetes_paralleles/babyfoot/amira_ouardia.txt"))

            print_result_action(config.baby_dt, 0)
            print_INFO(time, energy)
            input('')
            clear_screen()

            print(p_color("narration/quetes_paralleles/babyfoot/question_troll.txt"))
            input('')
            clear_screen()

            clear_screen()
            print(p_color("narration/quetes_paralleles/babyfoot/holcman_paoletti.txt"))


            # choose between paoletti and holcman
            paoletti_vs_holcman = check_input(
                'De Pierre Paloetti [0] et David Holcman [1], qui choisis-tu comme allie contre Daoult? [0/1]\n\n',
                ["0", "1"])
            if paoletti_vs_holcman == '0':
                # choose paoletti
                paoletti = True
                print(p_color("narration/quetes_paralleles/babyfoot/paoletti_only.txt"))

            else:
                print(p_color("narration/quetes_paralleles/babyfoot/holcman_only.txt"))
                holcman = False

            # babyfoot quest achieved
            babyfoot = True
            print_INFO(time, energy)
            input('')
            clear_screen()

            if DEBUG:
                print('\nBABYFOOT')
                print(
                    f'babyfoot = {babyfoot}, paoletti = {paoletti}, holcman = {holcman},')
                print(f'daoult_password = {daoult_password}, fungus = {fungus}')
                print(f'time = {time2hours(time)}; energy = {energy}\n')

        # LUNCH
        elif menu_choice == '3':
            clear_screen()
            if time <= config.tony_lunch_deadline * 60:
                # lunch with Tony
                print(p_color("narration/quetes_paralleles/manger/toni/toni.txt"))
                selfie = True
            else:
                # eat with Solene and Elise
                hamac_votes.extend(['elise', 'raphael', 'solene'])
                # cure fungal infection?
                fungal_choice = check_input(p_color("narration/quetes_paralleles/manger/elise_solene/elise_solene.txt"),
                                            ["0", "1"])
                if fungal_choice == '0':
                    # elise: the fungal infection grows worse
                    print(p_color("narration/quetes_paralleles/manger/elise_solene/elise.txt"))
                    fungus = True
                    time += config.lunch_dt
                    print_result_action(config.lunch_dt, 0)
                else:
                    # solene: the fungal infection is cured
                    print(p_color("narration/quetes_paralleles/manger/elise_solene/solene.txt"))
                    energy += config.fungal_de
                    time += config.lunch_dt
                    print_result_action(config.lunch_dt, config.fungal_de)

            print_INFO(time, energy)
            eaten = True
            input('')
            clear_screen()

            if DEBUG:
                print('\nLUNCH')
                print(f'hamac_votes = {hamac_votes}, selfie={selfie}')

        # NAP
        else:  # if menu_choice == '4':
            energy += config.nap_de
            time += config.nap_dt

            print_result_action(config.nap_dt, config.nap_de)

    if time >= config.end_hour * 60 or energy < 0:
        clear_screen()
        print(p_color("narration/fail_checkpoint.txt"))
        input()
        clear_screen()
        return False

    if not all([babyfoot, hamac_quest, diploma,
                (covid or fungus or hamac_weapon)]):
        clear_screen()
        print(p_color("narration/fail_checkpoint_2.txt"))
        input()
        clear_screen()
        return False

    ########################################
    # WHISTLEBLOWER QUEST
    ########################################

    assert daoult_password # hamac_quest
    assert felipe_badge # diploma quest

    if paoletti:
        office_check = check_input(
            p_color("narration/whistleblower_quest/whistleblower_allie_paoletti.txt"),
            [str(i) for i in range(4)])
    else:
        office_check = check_input(
            p_color(
                "narration/whistleblower_quest/whistleblower_allie_holcman.txt"),
            [str(i) for i in range(4)])

    if office_check == '0':
        # choose Daoult
        if mbti:
            print(p_color("narration/whistleblower_quest/daoult_si_mbti.txt"))
            energy += config.if_mbti_daoult_office_de
            time += config.whistleblower_dt
            print_result_action(config.whistleblower_dt, config.if_mbti_daoult_office_de)
        else:
            print(p_color("narration/whistleblower_quest/daoult_sans_mbti.txt"))
            energy += config.not_mbti_adoult_office_de
            time += config.whistleblower_dt
            print_result_action(config.whistleblower_dt, config.not_mbti_adoult_office_de)

    elif office_check == '1':
        # choose paoletti
        if paoletti:
            print(p_color("narration/whistleblower_quest/allie_paoletti.txt"))
            energy += config.allie_is_evil_de
            time += config.whistleblower_dt
            print_result_action(config.whistleblower_dt, config.allie_is_evil_de)
        else:
            time += config.whistleblower_dt
            print(p_color("narration/whistleblower_quest/not_allie_paoletti.txt"))
            print_result_action(config.whistleblower_dt, 0)

    elif office_check == '2':
        # choose Holcman
        if paoletti:
            time += config.whistleblower_dt
            print(p_color("narration/whistleblower_quest/not_allie_holcman.txt"))
            print_result_action(config.whistleblower_dt, 0)
        else:
            print(p_color("narration/whistleblower_quest/allie_holcman.txt"))
            print_result_action(config.whistleblower_dt, config.allie_is_evil_de)
            energy += config.allie_is_evil_de
            time += config.whistleblower_dt

    whistleblower_choice = check_input(p_color("narration/whistleblower_quest/whistleblower_end.txt"),
        ["T", "F"])
    if whistleblower_choice == 'T':
        whistleblower = True

    print_INFO(time, energy)
    input('')
    clear_screen()

    ##########################################
    # FINAL QUEST
    ##########################################

    if time >= config.end_hour * 60 or energy < 0:
        clear_screen()
        print(p_color("narration/fail_checkpoint.txt"))
        input()
        clear_screen()
        return False

    # get an appointment with Daoult
    if diploma:
        # appointment OK
        print(p_color("narration/final_quest/appointment_daoult_if_diploma.txt"))
    else:
        # appointment not valid
        print(
            p_color("narration/final_quest/appointment_daoult_if_no_diploma.txt"))
        input()
        clear_screen()
        return False

    print_NRJ(energy)
    input()
    clear_screen()

    if whistleblower:
        if paoletti:
            allie_confrontation = check_input(p_color(
                "narration/final_quest/if_whistleblower"
                "/allie_confrontation_paoletti.txt"),
                                          ["T", "F"])
        else:
            allie_confrontation = check_input(p_color(
                "narration/final_quest/if_whistleblower"
                "/allie_confrontation_holcman.txt"),
                ["T", "F"])

        if allie_confrontation == 'T':
            energy += config.confrontation_allie_de
            if paoletti:
                print(p_color(
                    "narration/final_quest/if_whistlblower"
                    "/confrontation_paoletti.txt"))
            else:
                print(p_color(
                    "narration/final_quest/if_whistlblower"
                    "/confrontation_paoletti.txt"))

        print_NRJ(energy)
        input()
        clear_screen()

        if huel:
            huel_choice = check_input(p_color("narration/final_quest/huel.txt"),
                                      ["T", "F"])
            if huel_choice == 'T':
                energy = 100
                print(p_color("narration/final_quest/huel_yes.txt"))
                print_NRJ(energy)
            else:
                print(p_color("narration/final_quest/huel_no.txt"))

            input()
            clear_screen()

        if selfie:
            daoult_proposition = check_input(
                p_color("narration/final_quest/if_whistleblower"
                        "/proposition_daoult_if_lydia.txt"),
                ["0", "1", "2"])
        else:
            daoult_proposition = check_input(
                p_color("narration/final_quest/if_whistleblower"
                        "/proposition_daoult_no_lydia.txt"),
                ["0", "1"])

        energy += config.daoult_proposition_de
        print_result_action(0, config.daoult_proposition_de)

        if daoult_proposition == '0':
            # accepter
            if energy >= config.trust_daoult_energy_threshold:
                # epilogue 1
                print(p_color("narration/final_quest/if_whistleblower"
                    "/epilogue1_enough_energy.txt"))
                input()
                clear_screen()
                return True
            else:
                clear_screen()
                print(p_color(
                    "narration/final_quest/if_whistleblower"
                    "/epilogue1_not_enough_energy.txt"))
                input()
                clear_screen()
                return False

        elif daoult_proposition == '1':
            # le confronter
            if energy >= config.dont_trust_daoult_energy_threshold:
                possible_keys, txt = attack(covid, hamac_weapon,
                                                     fungus, daoult=True)
                daoult_weapon_choice = check_input(p_color(txt, file=False),
                    possible_keys)

                if daoult_weapon_choice == '0':
                    # epilogue 2
                    if paoletti:
                        if bike_fight:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue2_paoletti_bike.txt"))
                        else:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue2_paoletti_nobike.txt"))
                    else:
                        if bike_fight:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue2_holcman_bike.txt"))
                        else:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue2_paoletti_nobike.txt"))

                elif daoult_weapon_choice == '1':
                    # epilogue 4
                    change_allie = check_input(p_color(
                        "narration/final_quest/if_whistleblower"
                        "/epilogue4_change_allie.txt"), ['T', 'F'])
                    if change_allie == 'T':
                        print(p_color(
                            "narration/final_quest/if_whistleblower/epilogue4_change_allie.txt"))
                    else:
                        print(p_color(
                            "narration/final_quest/if_whistleblower/epilogue4_no_change.txt"))

                else:
                    # champignon
                    # epilogue 3
                    if paoletti:
                        if covid:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue3_if_covid_paoletti.txt"))
                        elif fungus:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue3_no_covid_if_champi_paoletti.txt"))
                        else:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue3_no_covid_no_champi_paoletti.txt"))
                    else:
                        if covid:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue3_if_covid_holcman.txt"))
                        elif fungus:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue3_no_covid_if_champi_holcman.txt"))
                        else:
                            print(p_color(
                                "narration/final_quest/if_whistleblower/epilogue3_no_covid_no_champi_holcman.txt"))
                input()
                clear_screen()
                return True

            else:
                # not enough energy
                clear_screen()
                print(p_color("narration/final_quest/fail_energy.txt"))
                input()
                clear_screen()
                return False
        else:
            # partage des gains avec lydia
            assert selfie
            # epilogue 5
            print(p_color("narration/final_quest/if_whistleblower/epilogue5"
                          ".txt"))
            input()
            clear_screen()
            return True

    else:
        # not whistleblower

        # fight with allie
        if paoletti:
            lie_or_not = check_input(
                p_color("narration/final_quest/no_whistleblower"
                        "/lie_or_not_paoletti"
                        ".txt"),
                ["T", "F"])
        else:
            lie_or_not = check_input(
                p_color("narration/final_quest/no_whistleblower"
                        "/lie_or_not_holcman.txt"),
                ["T", "F"])
        if lie_or_not == 'F':
            # need to fight
            if paoletti:
                print(p_color(
                    "narration/final_quest/no_whistleblower/fight_paoletti"
                    ".txt"))
            else:
                print(p_color(
                    "narration/final_quest/no_whistleblower/fight_holcman.txt"))

            energy += config.lie_allie_fight_de
            # will exit if not enough energy

            possible_keys, txt = attack(covid, hamac_weapon,
                                        fungus, daoult=False)
            check_input(p_color(txt, file=False),
                                               possible_keys)
            # loose allie
            paoletti = False
            holcman = False

            # win fight
            print(p_color("narration/final_quest/no_whistleblower/win_fight"
                          ".txt"))
            print_NRJ(energy)
            input()
            clear_screen()
        else:
            if energy > config.dont_lie_allie_fight_de:
                #enough energy
                print(p_color("narration/final_quest/no_whistleblower/lie_enough_energy.txt"))
                energy += config.dont_lie_allie_fight_de
                print_NRJ(energy)
                input()
                clear_screen()
            else:
                # not enough energy
                # she is a bad liar
                print(p_color(
                    "narration/final_quest/no_whistleblower/lie_not_enough_energy.txt"))
                input()
                clear_screen()
                return False

        if huel:
            huel_choice = check_input(p_color("narration/final_quest/huel.txt"),
                                      ["T", "F"])
            if huel_choice == 'T':
                energy = 100
                print(p_color("narration/final_quest/huel_yes.txt"))
                print_NRJ(energy)
            else:
                print(p_color("narration/final_quest/huel_no.txt"))

            input()
            clear_screen()

        if paoletti or holcman:
            # she still has an allie
            fight_daoult_or_both = check_input(
                p_color(
                    "narration/final_quest/no_whistleblower"
                    "/fight_daoult_or_both.txt"),
                ["T", "F"])
            if fight_daoult_or_both == 'T':
                # fight only daoult
                # epilogue 4
                if paoletti:
                    print(p_color("narration/final_quest/no_whistleblower"
                    "/fight_only_daoult_if_paoletti.txt"))
                else:
                    print(p_color("narration/final_quest/no_whistleblower"
                                  "/fight_only_daoult_if_holcman.txt"))

                input()
                clear_screen()
                return True
            else:
                # fight both
                # not enough energy!
                print(p_color("narration/final_quest/no_whistleblower"
                    "/fight_both.txt"))
                input()
                clear_screen()
                return False

        else:
            # no more allie
            if (covid and energy >= config.if_covid_convince_daoult_energy_threshold):
                # epilogue 6
                print(p_color("narration/final_quest/no_whistleblower/epilogue6.txt"))
                input()
                clear_screen()
                return True
            elif (not covid and energy >= config.not_covid_convince_daoult_energy_threshold):
                # epilogue 7
                print(p_color(
                    "narration/final_quest/no_whistleblower/epilogue7.txt"))
                input()
                clear_screen()
                return True
            else:
                # not enough energy!
                print(p_color(
                    "narration/final_quest/no_whistleblower/fail_energy_daoult"
                    ".txt"))
                input()
                clear_screen()
                return False


if __name__ == '__main__':
    menu_principal(DEBUG=False)
