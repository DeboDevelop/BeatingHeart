import requests
from .models import Website
from .sendmail import sent_mail_up, sent_mail_down

def check_and_mail():
    all_entry = Website.objects.all()
    for entry in all_entry:
        try:
            r = requests.head(entry.url)
            if r.status_code == 200:
                if entry.currently_up == False:
                    entry.currently_up=True
                    entry.save()
                    sent_mail_up(entry.url, entry.email)
                print("Website is up: ", end =" ")
                print(entry.url)
            else:
                if entry.currently_up == True:
                    entry.currently_up=False
                    entry.save()
                    sent_mail_down(entry.url, entry.email)
                print("Website is down: ", end =" ")
                print(entry.url)
        except:
            if entry.currently_up == True:
                entry.currently_up=False
                entry.save()
                sent_mail_down(entry.url, entry.email)
            print("Website is down: ", end =" ")
            print(entry.url)
    return true
