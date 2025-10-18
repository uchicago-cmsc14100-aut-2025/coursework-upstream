"""
CMSC 14100
Updated Autumn 2025

Test code for Homework #4
"""

import hw4
from hw4_texts import load_text
import json
import os

import sys
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw4"


@pytest.mark.parametrize("password1, expected1",
                            [
                                ("", ""),
                                ("HannaH", "HannaH"),
                                ("I", "I"),
                                ("Password123", "321drowssaP"),
                                ("Correct Horse Battery Staple!", "!elpatS yrettaB esroH tcerroC"),
                            ])
def test_reverse_password(password1, expected1):
    """ Test code for reverse_password """
    steps = [f"actual = hw4.reverse_password('{password1}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.reverse_password(password1)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected1)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("password2, purge2, expected2",
                            [
                                ("chennai123", "a", "chenni123"),
                                ("YOTEQUIERO", "a", "YOTEQUIERO"),
                                ("bangladesh09", "9", "bangladesh0"),
                                ("jeanpierre123", "e", "janpirr123"),
                                ("jeanpierre123", "E", "jeanpierre123"),
                                ("Correct Horse Battery Staple!", "o", "Crrect Hrse Battery Staple!"),
                            ])
def test_purge(password2, purge2, expected2):
    """ Test code for purge """
    steps = [f"actual = hw4.purge('{password2}', '{purge2}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.purge(password2, purge2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected2)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("password3, old3, new3, expected3",
                            [
                                ("chennai123", "a", "@", "chenn@i123"),
                                ("YOTEQUIERO", "O", "A", "YATEQUIERA"),
                                ("iriscarolina24", "i", "1", "1r1scarol1na24"),
                                ("jeanpierre123", "e", "E", "jEanpiErrE123"),
                                ("PALMTREES", "a", "z", "PALMTREES"),
                                ("Correct Horse Battery Staple!", "o", "a", "Carrect Harse Battery Staple!"),
                            ])
def test_substitute(password3, old3, new3, expected3):
    """ Test code for substitute """
    steps = [f"actual = hw4.substitute('{password3}', '{old3}', '{new3}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.substitute(password3, old3, new3)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected3)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("password4, expected4",
                            [
                                ("chennai123", "chennai"),
                                ("12345678", ""),
                                ("iriscarolina24", "iriscarolina"),
                                ("7sisters", "sisters"),
                                ("PALMTREES", "PALMTREES"),
                                ("Pa55w0rd", "Pawrd"),
                                ("Correct Horse Battery Staple!", "CorrectHorseBatteryStaple"),
                            ])
def test_alpha_only(password4, expected4):
    """ Test code for alpha_only """
    steps = [f"actual = hw4.alpha_only('{password4}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.alpha_only(password4)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected4)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("password5, expected5",
                            [
                                ("shopping123", "SHOPPING123"),
                                ("r3yn0ldc", "R3YN0LDC"),
                                ("nOtGuIlTy7", "NoTgUiLtY7"),
                                ("Fishboat1", "fISHBOAT1"),
                                ("MATT65", "matt65"),
                                ("Gabriela01", "gABRIELA01"),
                                ("Nnamdi03", "nNAMDI03"),
                                ("Correct Horse Battery Staple!", "cORRECT hORSE bATTERY sTAPLE!"),
                            ])
def test_toggle_case(password5, expected5):
    """ Test code for toggle_case """
    steps = [f"actual = hw4.toggle_case('{password5}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.toggle_case(password5)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected5)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("password6, shift6, expected6",
                            [
                                ("shopping123", 1, "shopping234"),
                                ("r3yn0ldc", 5, "r8yn5ldc"),
                                ("r3yn0ldc", 0, "r3yn0ldc"),
                                ("Gabriela01", 1, "Gabriela12"),
                                ("nOtGuIlTy7", 4, "nOtGuIlTy1"),
                                ("nOtGuIlTy7", -6, "nOtGuIlTy1"),
                                ("102030", -2, "980818"),
                                ("MATT65", 8, "MATT43"),
                                ("Nnamdi03", 8, "Nnamdi81"),
                                ("Correct Horse Battery Staple!", 3, "Correct Horse Battery Staple!"),
                            ])
def test_shift_numbers(password6, shift6, expected6):
    """ Test code for shift_numbers """
    steps = [f"actual = hw4.shift_numbers('{password6}', {shift6})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.shift_numbers(password6, shift6)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected6)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("credentials7, expected7",
                            [
                                (["blase1@uchicago.edu:section4", "blase2@uchicago.edu:section5", "ams@cs.uchicago.edu:BillEvansFan8"], [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0]),
                                (["*************@yahoo.co.uk:munchie", "***********@freenet.de:august", "***********@yahoo.com:donkey10", "**************@hotmail.com:major88", "************@gmail.com:pasvord"], [0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
                                (["****@smc.smces.es:inicio", "*********@hotmail.com:marina2122", "********@att.net:pepper", "**********@hotmail.com:linkedin", "***************@btinternet.com:twickers100", "*****@yahoo.co.uk:appleby1", "********@my.devry.edu:minime16", "*************@yahoo.co.uk:munchie", "***********@freenet.de:august", "*******@terra.com.br:sheila2", "*****************@yahoo.com:brownie22", "***********@gmail.com:pierrelagardere", "***********@yahoo.com:pakistan", "***********@yahoo.com:donkey10", "**************@hotmail.com:major88", "*******@bt.com:sdfghj", "************@gmail.com:pasvord"], [0, 0, 0, 0, 0, 0, 4, 4, 5, 1, 1, 1, 0, 0, 0, 1, 0]),
                                (["****@smc.smces.es:", "*********@hotmail.com:marina2122", "********@att.net:pepper", "************@gmail.com:pasvord"], [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]),
                                (["****@smc.smces.es:ifiwerearichmanladeedee", "*********@hotmail.com:CORRECT HORSE BATTERY STAPLE!", "********@att.net:1234567887654321", "************@gmail.com:pasvord"], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3]),
                                ([], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                (load_text(), [0, 8, 0, 1, 2, 0, 2732, 1777, 3181, 1211, 569, 242, 150, 63, 32, 21, 11]),
                            ])
def test_length_distribution(credentials7, expected7):
    """ Test code for length_distribution """
    steps = [f"actual = hw4.length_distribution({credentials7})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.length_distribution(credentials7)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected7)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("credentials8, expected8",
                            [
                                (["****@smc.smces.es:", "*********@hotmail.com:marina2122", "********@att.net:pepper", "************@gmail.com:pasvord", "*************@gmail.com:catch22", "******@hotmail.com:12341234"], [0, 3, 7, 2, 2, 0, 0, 0, 0, 0]),
                                (["blase1@uchicago.edu:section4", "blase2@uchicago.edu:section5", "ams@cs.uchicago.edu:BillEvansFan888"], [0, 0, 0, 0, 1, 1, 0, 0, 3, 0]),
                                (["*************@yahoo.co.uk:munchie", "***********@freenet.de:august", "***********@yahoo.com:donkey10", "**************@hotmail.com:major88", "************@gmail.com:pasvord"], [1, 1, 0, 0, 0, 0, 0, 0, 2, 0]),
                                (["****@smc.smces.es:inicio", "*********@hotmail.com:marina2122", "********@att.net:pepper", "**********@hotmail.com:linkedin", "***************@btinternet.com:twickers100", "*****@yahoo.co.uk:appleby1", "********@my.devry.edu:minime16", "*************@yahoo.co.uk:munchie", "***********@freenet.de:august", "*******@terra.com.br:sheila2", "*****************@yahoo.com:brownie22", "***********@gmail.com:pierrelagardere", "***********@yahoo.com:pakistan", "***********@yahoo.com:donkey10", "**************@hotmail.com:major88", "*******@bt.com:sdfghj", "************@gmail.com:pasvord"], [3, 5, 6, 0, 0, 0, 1, 0, 2, 0]),
                                (["****@smc.smces.es:ifiwerearichmanladeedee", "*********@hotmail.com:CORRECT HORSE BATTERY STAPLE!", "********@att.net:ekonomist", "************@gmail.com:pasvord"], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                ([], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                (load_text(), [2779, 4467, 2943, 1883, 1495, 1553, 1495, 1431, 1471, 1639]),
                            ])
def test_digit_distribution(credentials8, expected8):
    """ Test code for digit_distribution """
    steps = [f"actual = hw4.digit_distribution({credentials8})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.digit_distribution(credentials8)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected8)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("credentials9, expected9",
                            [
                                (["test1@gmail.com:1monkeyjumpingonthebed", "test2@gmail.com:w3lostthesea", "test3@uchicago.edu:disasterkid3", "test4@cs.uchicago.edu:cs141student", "test5@gmail.com:1qaz1qaz"], [0, 1, 0, 2, 0, 0, 0, 0, 0, 0]),
                                (["test1@gmail.com:123456", "test2@gmail.com:welostthesea", "test3@uchicago.edu:disasterkid99", "test4@cs.uchicago.edu:cs141student", "test5@gmail.com:1qaz2wsx"], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                (["*****@gbpinc.com:matilda", "***********@flextronics.com:simon5", "******@hotmail.com:47182006", "***********@yahoo.com:faizaa", "********@yahoo.com:dontcare", "********@terra.com.br:leonel58", "*********@hotmail.com:pelonchas", "*************@hotmail.com:Rlinn5", "*****@miconstruct.com.au:uss091", "***************@yahoo.co.in:25111981", "************@yahoo.com:telephone", "***********@gmail.com:mojo2029", "************@us.army.mil:sunshine20", "**********@yahoo.se:saidpiran", "***************@hotmail.co.uk:sebastian", "**********@hotmail.com:pppppp", "*************@vetcoaibel.com:qwertyui1", "********@yahoo.com:iluvdana", "***********@gmail.com:gbio2011", "********@hotmail.com:reticulos", "*****@optonline.net:dance1", "******@libero.it:vialarda", "********@aol.com:sterling", "******@gmail.com:gudtjr99", "*************@hotmail.com:Latjms88", "***********@hotmail.com:SweetDreams", "**************@gmail.com:grkvkays", "**********@yahoo.com:ead123", "********@videotron.ca:2919page", "**********@live.com:luces99", "************@gmail.com:UKEDUCATION", "***********@gmail.com:26540000", "*******@jwrc.or.jp:palila", "*****************@hotmail.com:mari2406", "**************@yahoo.ci.in:love123", "*********@hotmail.com:rizwan", "*****************@gmail.com:daddyo12345", "*********@leapforward.biz:guerrero", "**********@carstigemotors.com:packers04", "***************@gmail.com:pebbles", "***@HFFUND.COM.CN:855653", "******@cameronschools.org:dukeone", "***************@fidal.fr:mozart"], [0, 2, 0, 0, 0, 2, 0, 0, 0, 0]),
                                (load_text(), [25, 603, 122, 61, 65, 36, 27, 47, 37, 28]),
                            ])
def test_solitary_digits(credentials9, expected9):
    """ Test code for solitary_digits """
    steps = [f"actual = hw4.solitary_digits({credentials9})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.solitary_digits(credentials9)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected9)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("credentials10, search10, expected10",
                            [
                                (["test1@gmail.com:1monkeyjumpingonthebed", "test2@gmail.com:monkey", "test3@uchicago.edu:disasterkid3", "test4@cs.uchicago.edu:cs141student", "test5@gmail.com:monkey"], "monkey", 3),
                                (["redacted1@yahoo.co.uk:monkey369", "redacted2@gmail.com:Monkey#1", "redacted@monkey.com:monkeydo", "redacted3@yahoo.com:monkey123", "monkeyredacted21@yahoo.com:2loudog2", "redacted4@gmail.com:Monkey1", "redacted5@gmail.com:MONKEY77", "redacted6@gmail.com:Monkeys44", "redacted7@yahoo.com:greenmonkeys", "theredactedmonkey@hotmail.com:slipknot13", "redacted8@aol.com:seamonkeys", "redacted9@kohls.com:monkey11", "redacted10@gmail.com:evilmonkey13", "redacted11@gmail.com:12monkeys", "redacted12@yahoo.com:monkey1*"], "monkey", 13),
                                (["redacted1@yahoo.co.uk:monkey369", "redacted2@gmail.com:Monkey#1", "redacted@monkey.com:monkeydo", "redacted3@yahoo.com:monkey123", "monkeyredacted21@yahoo.com:2loudog2", "redacted4@gmail.com:Monkey1", "redacted5@gmail.com:MONKEY77", "redacted6@gmail.com:Monkeys44", "redacted7@yahoo.com:greenmonkeys", "theredactedmonkey@hotmail.com:slipknot13", "redacted8@aol.com:seamonkeys", "redacted9@kohls.com:monkey11", "redacted10@gmail.com:evilmonkey13", "redacted11@gmail.com:12monkeys", "redacted12@yahoo.com:monkey1*"], "mOnKeY", 13),
                                (["redacted1@yahoo.co.uk:monkey369", "redacted2@gmail.com:Monkey#1", "redacted@monkey.com:monkeydo", "redacted3@yahoo.com:monkey123", "monkeyredacted21@yahoo.com:2loudog2", "redacted4@gmail.com:Monkey1", "redacted5@gmail.com:MONKEY77", "redacted6@gmail.com:Monkeys44", "redacted7@yahoo.com:greenmonkeys", "theredactedmonkey@hotmail.com:slipknot13", "redacted8@aol.com:seamonkeys", "redacted9@kohls.com:monkey11", "redacted10@gmail.com:evilmonkey13", "redacted11@gmail.com:12monkeys", "redacted12@yahoo.com:monkey1*"], "password", 0),
                                (["redacted1@yahoo.co.uk:monkey369", "redacted2@gmail.com:Monkey#1", "redacted@monkey.com:monkeydo", "redacted3@yahoo.com:monkey123", "monkeyredacted21@yahoo.com:2loudog2", "redacted4@gmail.com:Monkey1", "redacted5@gmail.com:MONKEY77", "redacted6@gmail.com:Monkeys44", "redacted7@yahoo.com:greenmonkeys", "theredactedmonkey@hotmail.com:slipknot13", "redacted8@aol.com:seamonkeys", "redacted9@kohls.com:monkey11", "redacted10@gmail.com:evilmonkey13", "redacted11@gmail.com:12monkeys", "redacted12@yahoo.com:monkey1*"], "LouDog", 1),
                                (load_text(), "Password", 24),
                                (load_text(), "123456", 140),
                                (load_text(), "!", 22),
                                (load_text(), "chicago", 1),
                                (load_text(), "LinkedIn", 44),
                            ])
def test_matching_passwords(credentials10, search10, expected10):
    """ Test code for matching_passwords """
    steps = [f"actual = hw4.matching_passwords({credentials10}, '{search10}')"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.matching_passwords(credentials10, search10)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected10)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("credentials11, expected11",
                            [
                                (["test1@gmail.com:1monkeyjumpingonthebed", "test2@gmail.com:MOnkeY", "test3@uchicago.edu:diSASterkid3", "test4@cs.uchicago.edu:cs141student", "test5@gmail.com:monkey"], ['test1@gmail.com:1m0nk3yjump1ng0nth3b3d', 'test2@gmail.com:M0nk3Y', 'test3@uchicago.edu:d1S@St3rk1d3', 'test4@cs.uchicago.edu:cs141stud3nt', 'test5@gmail.com:m0nk3y']),
                                (["*************@mac.com:No1stunner", "**********************@hotmail.com:221501", "**********@aol.com:zygote1", "**************@ymail.com:taz420", "************@kpmg.com:rain4est", "********@hotmail.com:caitlin", "******@rediffmail.com:archy1102", "**********@pec-cares.org:nannie", "************@yahoo.com:matthew007", "********@adacto.it:monster1", "*********@hotmail.com:Tucker123", "**********@whitehead-monckton.co.uk:madjock"], ['*************@mac.com:N01stunn3r', '**********@aol.com:zyg0t31', '**************@ymail.com:t@z420', '************@kpmg.com:r@1n43st', '********@hotmail.com:c@1tl1n', '******@rediffmail.com:@rchy1102', '**********@pec-cares.org:n@nn13', '************@yahoo.com:m@tth3w007', '********@adacto.it:m0nst3r1', '*********@hotmail.com:Tuck3r123', '**********@whitehead-monckton.co.uk:m@dj0ck']),
                                (["**********@rogers.com:daisychain", "*********@qq.com:240691956", "**************@bellsouth.net:lacey01", "********@sbcglobal.net:03grace11", "********@disney.com:xing61", "*********@yahoo.com:berries", "*******@pctrainingonline.co.za:kavita", "********@gmail.com:avenger74", "******@tx.rr.com:linkedin6245", "**********@yahoo.com:brain62", "***********@banamex.com:oscarleal", "**************@gmail.com:420420", "**********@hotmail.com:somerset", "********@hotmail.com:luvluv", "******@prakashchemicals.com:chirag", "*******@comcast.net:steelers1", "**************@surreycc.gov.uk:antoinette", "********@pacbell.net:pigeon", "********@yahoo.com:howdy4u2", "**********@hotmail.com:charlt0n"], ['**********@rogers.com:d@1sych@1n', '**************@bellsouth.net:l@c3y01', '********@sbcglobal.net:03gr@c311', '********@disney.com:x1ng61', '*********@yahoo.com:b3rr13s', '*******@pctrainingonline.co.za:k@v1t@', '********@gmail.com:@v3ng3r74', '******@tx.rr.com:l1nk3d1n6245', '**********@yahoo.com:br@1n62', '***********@banamex.com:0sc@rl3@l', '**********@hotmail.com:s0m3rs3t', '******@prakashchemicals.com:ch1r@g', '*******@comcast.net:st33l3rs1', '**************@surreycc.gov.uk:@nt01n3tt3', '********@pacbell.net:p1g30n', '********@yahoo.com:h0wdy4u2', '**********@hotmail.com:ch@rlt0n']),
                                (["************@oxfordhealth.nhs.uk:chocolate", "*************@hotmail.com:CALIFORNIA", "****@bartowford.com:barnes", "*******@fortsmithschools.org:athena15", "*****@ford.com:sommer30", "************@yahoo.com.mx:california", "***********@virgin.net:forest", "******@seventeenevents.co.uk:madforit", "********@gmail.com:forest3", "*********@yahoo.com:traford", "*******************@windowslive.com:playforever", "******@telfort.nl:123456", "********@stanford.edu:dena4444", "****@theartcentre.org:artforyou", "*****@bedfordstmartins.com:campout", "************@hotmail.com:forever", "**********@hotmail.com:fordodge", "*********@gmail.com:Formus1", "******@staffordmanpower.com:arnold", "*******@ford.com:lakers", "********@hotmail.com:fordfalcon", "**********@ntlworld.com:bradford", "*******@forlandlighting.com:19811010", "**********@aol.com:forkids", "*******@ath.forthnet.gr:1qa2ws", "******@ssinformatica.com:713499", "***********@gmail.com:informatica", "****@helfmanford.com:wings1", "********@usfamily.net:crawford", "*************@CityofOrlando.net:129569abc", "*************@att.net:foreverdone", "*********@yahoo.com:forever11", "**********@oxford.k12.ms.us:jdavenport", "***********@yahoo.com:friendsforever", "************@fastwebmail.it:fornaci", "*******@yahoo.com:forest", "*****@oxfordcentre.eu:clara01", "*********@leapforward.biz:guerrero", "********@yahyoo.com:crawford", "*******@cloverinformatica.com:clover07", "*****@sbcglobal.net:ford12345", "***************@foresthills.edu:bruno91", "*****@theforbescompany.com:temby145", "************@amerisourcebergen.com:murford", "*******@feliciaforte.com:yippie28", "*******@gmail.com:fordikon", "******@gmail.com:kuforu35"], ['************@oxfordhealth.nhs.uk:ch0c0l@t3', '*************@hotmail.com:C@L14N1@', '****@bartowford.com:b@rn3s', '*******@fortsmithschools.org:@th3n@15', '*****@ford.com:s0mm3r30', '************@yahoo.com.mx:c@l14n1@', '***********@virgin.net:43st', '******@seventeenevents.co.uk:m@d41t', '********@gmail.com:43st3', '*********@yahoo.com:tr@4d', '*******************@windowslive.com:pl@y43v3r', '********@stanford.edu:d3n@4444', '****@theartcentre.org:@rt4y0u', '*****@bedfordstmartins.com:c@mp0ut', '************@hotmail.com:43v3r', '**********@hotmail.com:4d0dg3', '*********@gmail.com:4mus1', '******@staffordmanpower.com:@rn0ld', '*******@ford.com:l@k3rs', '********@hotmail.com:4df@lc0n', '**********@ntlworld.com:br@d4d', '**********@aol.com:4k1ds', '*******@ath.forthnet.gr:1q@2ws', '***********@gmail.com:1n4m@t1c@', '****@helfmanford.com:w1ngs1', '********@usfamily.net:cr@w4d', '*************@CityofOrlando.net:129569@bc', '*************@att.net:43v3rd0n3', '*********@yahoo.com:43v3r11', '**********@oxford.k12.ms.us:jd@v3np0rt', '***********@yahoo.com:fr13nds43v3r', '************@fastwebmail.it:4n@c1', '*******@yahoo.com:43st', '*****@oxfordcentre.eu:cl@r@01', '*********@leapforward.biz:gu3rr3r0', '********@yahyoo.com:cr@w4d', '*******@cloverinformatica.com:cl0v3r07', '*****@sbcglobal.net:4d12345', '***************@foresthills.edu:brun091', '*****@theforbescompany.com:t3mby145', '************@amerisourcebergen.com:mur4d', '*******@feliciaforte.com:y1pp1328', '*******@gmail.com:4d1k0n', '******@gmail.com:ku4u35']),
                                (["test@uchicago.edu:forever", "test@uchicago.edu:EvelynForever", "test@uchicago.edu:EvelynfOrever", "test@uchicago.edu:EvelynfoRever", "test@uchicago.edu:FOREVERandfOReverANDFoReverandFOrever"], ['test@uchicago.edu:43v3r', 'test@uchicago.edu:3v3lyn43v3r', 'test@uchicago.edu:3v3lyn43v3r', 'test@uchicago.edu:3v3lyn43v3r', 'test@uchicago.edu:43V3R@nd43v3r@ND43v3r@nd43v3r'])
                            ])
def test_l33tify(credentials11, expected11):
    """ Test code for l33tify """
    steps = [f"actual = hw4.l33tify({credentials11})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.l33tify(credentials11)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected11)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("credentials12, expected12",
                            [
                                (["blase1@uchicago.edu:section4", "blase2@uchicago.edu:section5", "ams@cs.uchicago.edu:BillEvansFan8", "ams2@cs.uchicago.edu:00BillEvansFan"], 3),
                                (["blase1@uchicago.edu:section444", "blase2@uchicago.edu:section55", "ams@cs.uchicago.edu:B0000000000000000", "ams2@cs.uchicago.edu:xx00BillEvansFan00xx"], 3),
                                (["blase1@uchicago.edu:section", "blase2@uchicago.edu:section55", "ams@cs.uchicago.edu:password123456", "ams2@cs.uchicago.edu:1234567"], 2),
                                (["**************@ymail.com:taz420", "************@kpmg.com:rain4est", "********@hotmail.com:caitlin", "******@rediffmail.com:archy1102", "**********@pec-cares.org:nannie", "************@yahoo.com:matthew007", "********@adacto.it:monster1", "*********@hotmail.com:Tucker123", "**********@whitehead-monckton.co.uk:madjock", "***************@gmail.com:seetha", "********************@gmail.com:!QAZzaq1", "*********@msn.com:krystle2", "*********@gmail.com:Hckykid8", "*******************@hotmail.com:pepita85", "*********@juno.com:mackj91", "*********@tin.it:talco2599", "************@aol.com:standard63"], 11),
                                (load_text(), 3603),
                            ])
def test_letters_digits(credentials12, expected12):
    """ Test code for length_distribution """
    steps = [f"actual = hw4.letters_digits({credentials12})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.letters_digits(credentials12)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected12)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
