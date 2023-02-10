import pyautogui as pt
from time import sleep
import random
import string
import pyperclip as pc
import names
import logging
import webbrowser
from win10toast import ToastNotifier


toast = ToastNotifier()
path = r"C:\lovoo_bot\source_code\assets\\"

logging.basicConfig(filename=r'Login_daten.log', encoding='utf-8', level=logging.DEBUG)
random_date = ["1","2","3","4","5","6","7","8","9"]
random_year = ["1999", "2000", "2001", "2002", "2003"]
random_bild = [1,2,3,4,5,6,7,8,9]


pt.PAUSE = 1.5


def open():
    webbrowser.open_new("https://www.phaantm.de/")
    sleep(2)
    pt.hotkey("win", "left")
    pt.click()
    sleep(20)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def create_accout():
    change_account = pt.locateOnScreen(f"{path}change_account.png", confidence=.7)
    pt.click(change_account[0:2] ,duration = .5)
    sleep(5)
    log_in_with_mail = pt.locateOnScreen(f"{path}log_in_with_e-mail.png", confidence=.7)
    pt.click(log_in_with_mail ,duration = .5)
    sleep(1)
    your_email_site = pt.locateOnScreen(f"{path}your_email_site.png", confidence=.7)

    pt.click(your_email_site ,duration = .5)
    sleep(1)
    email_cache = random_char(7)
    pt.write(email_cache)
    sleep(1)
    mail_login = pt.locateOnScreen(f"{path}mail_login.png", confidence=.7)

    pt.click(mail_login ,duration = .5)
    sleep(1)
    new_account = pt.locateOnScreen(f"{path}new_account.png", confidence=.7)

    pt.click(new_account, duration=.5)
    sleep(1)
    your_email = pt.locateOnScreen(f"{path}your_email.png", confidence=.7)

    pt.click(your_email, duration = .5)
    pt.write(email_cache)
    hund = pt.locateOnScreen(f"{path}hund.png", confidence=.7)
    sleep(1)
    pt.click(hund)
    pt.write("phaantm.de")
    your_password = pt.locateOnScreen(f"{path}your_password.png", confidence=.7)
    pt.click(your_password ,duration = .5)
    pt.write("Wasd1234")
    sleep(2)
    logging.info("   Email: "+email_cache+"@phaantm.de"+"  |  "+"Passwort: wasd1234 ")
    continue_1 = pt.locateOnScreen(f"{path}continue.png", confidence=.6)
    pt.click(continue_1 ,duration = .5)
    sleep(2)
    whats_your_name = pt.locateOnScreen(f"{path}whats_your_name.png", confidence=.7)

    pt.click(whats_your_name, duration = .5)
    first_name = names.get_first_name(gender='female')
    pt.write(first_name)
    sleep(1)
    name_weiter = pt.locateOnScreen(f"{path}name_weiter.png", confidence=.8)

    pt.click(name_weiter, duration=.5)
    sleep(2)
    tag = pt.locateOnScreen(f"{path}tag.png", confidence=.8)

    pt.click(tag)
    pt.write(random.choice(random_date))
    monat = pt.locateOnScreen(f"{path}monat.png", confidence=.7)

    pt.click(monat)
    pt.write(random.choice(random_date))
    jahr = pt.locateOnScreen(f"{path}jahr.png", confidence=.8)

    pt.click(jahr)
    pt.write(random.choice(random_year))
    datum_weiter = pt.locateOnScreen(f"{path}datum_weiter.png", confidence=.8)
    pt.click(datum_weiter, duration=.5)
    female = pt.locateOnScreen(f"{path}female.png", confidence=.7)
    pt.click(female, duration=.5)
    sleep(1)
    upload = pt.locateOnScreen(f"{path}upload.png", confidence=.7)

    pt.click(upload)
    sleep(1)
    pt.keyDown("down")
    sleep(random.choice(random_bild))
    pt.keyUp("down")
    pt.click()
    upload_upload = pt.locateOnScreen(f"{path}upload_upload.png", confidence=.7)
    sleep(1)
    pt.click(upload_upload)
    sleep(2)
    upload_weiter = pt.locateOnScreen(f"{path}upload_weiter.png", confidence=.7)

    pt.click(upload_weiter)
    sleep(1)
    int_1 = pt.locateOnScreen(f"{path}int_1.png", confidence=.7)
    pt.click(int_1, duration=.5)
    int_2 = pt.locateOnScreen(f"{path}int_2.png", confidence=.7)
    pt.click(int_2, duration=.5)
    sleep(1)
    int_men = pt.locateOnScreen(f"{path}int_men.png", confidence=.7)

    pt.click(int_men, duration=.5)
    sleep(1)
    weiter_men = pt.locateOnScreen(f"{path}weiter_men.png", confidence=.7)

    pt.click(weiter_men, duration=.5)
    sleep(1)
    skip = pt.locateOnScreen(f"{path}skip.png", confidence=.7)
    pt.click(skip, duration=.5)
    sleep(5)

def reset():
    taskmanager = pt.locateOnScreen(f"{path}taskmanager.png", confidence=.7)
    pt.moveTo(taskmanager)
    pt.move(0,40)
    pt.click()
    sleep(1)
    pt.move(-150,0)
    sleep(1)
    pt.dragTo(1000, 100, button='left')
    sleep(3)
    lovoo_symb = pt.locateOnScreen(f"{path}lovoo_symb.png", confidence=.7)
    pt.click(lovoo_symb, duration=.5)
    sleep(15)
    safety_tips = pt.locateOnScreen(f"{path}safety_tips.png", confidence=.7)
    pt.moveTo(safety_tips, duration=.5)
    pt.move(0,300)
    sleep(1)
    pt.dragTo(1000, 100, button='left')
    got_it = pt.locateOnScreen(f"{path}got_it.png", confidence=.7)
    pt.click(got_it, duration=.5)

def use_and_logout():
    continue_2 = pt.locateOnScreen(f"{path}continue_2.png", confidence=.7)
    if continue_2 != None:
        pt.click(continue_2, duration=.5)
        sleep(5)
    awsm = pt.locateOnScreen(f"{path}awsm.png", confidence=.7)
    if awsm != None:
        pt.click(awsm, duration=.5)
        sleep(8)
    account_slide = pt.locateOnScreen(f"{path}account_slide.png", confidence=.7)
    pt.click(account_slide, duration=.5)
    sleep(2)
    settings = pt.locateOnScreen(f"{path}settings.png", confidence=.7)
    pt.click(settings, duration=.5)
    sleep(1)
    my_account = pt.locateOnScreen(f"{path}my_account.png", confidence=.7)
    pt.click(my_account, duration=.5)
    sleep(1)
    pt.dragTo(1000, 200, button='left')
    delete_account_det = pt.locateOnScreen(f"{path}del_account_det.png", confidence=.7) 
    pt.moveTo(delete_account_det)
    pt.move(0,40)
    pt.click()
    sleep(1)
    skip_del = pt.locateOnScreen(f"{path}skip_del.png", confidence=.7)
    pt.click(skip_del, duration=.5)
    sleep(1)
    delete_account = pt.locateOnScreen(f"{path}delete_account.png", confidence=.7)
    pt.click(delete_account, duration=.5)
    sleep(1)
    ok = pt.locateOnScreen(f"{path}ok.png", confidence=.7)
    pt.click(ok, duration=.5)
    sleep(1)
    back = pt.locateOnScreen(f"{path}back.png", confidence=.7)
    pt.click(back, duration=.5)
    sleep(1)
    x = pt.locateOnScreen(f"{path}x.png", confidence=.7)
    pt.click(x, duration=.5)
    sleep(1)
    pt.click(back, duration=.5)
    sleep(1)
    posteingang = pt.locateOnScreen(f"{path}posteingang.png", confidence=.7)
    pt.click(posteingang, duration=.5)
    sleep(1)
    your_account_delete = pt.locateOnScreen(f"{path}your_account_del.png", confidence=.7)
    pt.click(your_account_delete, duration=.5)
    sleep(3)
    code_platz = pt.locateOnScreen(f"{path}code_platz.png", confidence=.7)
    pt.moveTo(code_platz)
    pt.move(-100,0)
    pt.tripleClick()
    pt.hotkey("ctrl", "c")
    rabatt_code = pc.paste().replace(" ", "")
    redem_code = pt.locateOnScreen(f"{path}redem_code.png", confidence=.7)
    pt.click(redem_code, duration=.5)
    sleep(1.5)
    enter_code = pt.locateOnScreen(f"{path}enter_code.png", confidence=.7)
    pt.click(enter_code, duration=.5)
    sleep(1) 
    pt.write(rabatt_code)
    sleep(1)
    use = pt.locateOnScreen(f"{path}use.png", confidence=.7)
    pt.click(use, duration=.5)
    sleep(1)
    log_out = pt.locateOnScreen(f"{path}log_out.png", confidence=.7)
    pt.click(log_out, duration=.5)
    sleep(2)
    yes_logout = pt.locateOnScreen(f"{path}yes_logout.png", confidence=.7)
    pt.click(yes_logout, duration=.5)
    sleep(2)
    posteingang_2 = pt.locateOnScreen(f"{path}posteingang_2.png", confidence=.7)
    pt.moveTo(posteingang_2, duration=.5)
    pt.move(0,50)
    pt.click()
    sleep(2)
    abmelden_email = pt.locateOnScreen(f"{path}abmelden_email.png", confidence=.7)
    pt.click(abmelden_email, duration=.5)
    sleep(1)


toast.show_toast(
    "Bot wurde gestartet",
    "Bitte nicht unterbrechen, Bot Repariert sich von selbst",
    duration = 10,
    threaded = True,
)

open()
lovoo_symb = pt.locateOnScreen(f"{path}lovoo_symb.png", confidence=.7)
pt.click(lovoo_symb, duration=.5)
sleep(30)
while True:
    create_accout()
    sleep(3)
    reset()
    sleep(3)
    use_and_logout()