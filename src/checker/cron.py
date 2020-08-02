import requests
import datetime
from .models import Website
from .sendmail import sent_mail_up, sent_mail_down

def check_and_mail():
    """
    Function to check whether the website is up or not and call teh sentmail functions appropriately.
    Returns:
        bool: True
    """
    #Extract all the website data
    all_entry = Website.objects.all()
    for entry in all_entry:
        try:
            #Senting the request to check whether the website is up or not
            r = requests.head(entry.url)
            #Printing Data and Time For Logging Purpose
            print(datetime.datetime.now()) 
            #If the website is up
            if r.status_code == 200:
                #And the website should be down according to database
                if entry.currently_up == False:
                    #Update the database
                    entry.currently_up=True
                    entry.save()
                    #Send Mail
                    sent_mail_up(entry.url, entry.email)
                #Logging the information to file
                print("Website is up: ", end =" ")
                print(entry.url)
            #if the website is not up
            else:
                #And is should be down according to dabase
                if entry.currently_up == True:
                    #Update the database
                    entry.currently_up=False
                    entry.save()
                    #Send Mail
                    sent_mail_down(entry.url, entry.email)
                #Logging the information to file
                print("Website is down: ", end =" ")
                print(entry.url)
        #If the request fail then the website id down
        except:
            #And is should be down according to dabase
            if entry.currently_up == True:
                #Update the database
                entry.currently_up=False
                entry.save()
                #Send Mail
                sent_mail_down(entry.url, entry.email)
            #Logging the information to file
            print("Website is down: ", end =" ")
            print(entry.url)
    return true
