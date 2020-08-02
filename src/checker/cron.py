import requests
from .models import Website

def check_and_mail():
    all_entry = Website.objects.all()
    for entry in all_entry:
        try:
            r = requests.head(entry.url)
            if r.status_code == 200:
                print("Website is up: ")
                print(entry.url)
            else:
                print("Website is down")
                print(entry.url)
        except:
            print("Website is down")
            print(entry.url)
    return true