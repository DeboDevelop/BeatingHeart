# BeatingHeart

BeatingHeart is a django app which check whether a website is up or not and sents email is the website is down. This project is mainly targeted for devOps use case. It uses crontab to schedule task and send mail using django's internal function.

### Requirements

Python 3.6.9 or above

### To Run Locally

1. Clone the Repository

2. Create an environment variable

   `python3 -m venv env`

3. Activate the virtual env

   `source env/bin/activate`

4. Install the Dependencies
   `pip install -r requirements.txt`

   or

   `pip3 install -r requirements.txt`

   If for some reason the command above didn't work, just install the following

   `Django, django-crontab, python-decouple, requests`

5. Create a .env file inside /src folder

   Give the following Information:

   ```DEBUG=True/False
   SECRET_KEY=x2^-!-p-y#^f%+-n*+-r%)pe+#rq#geb%&pp%se!n2$1gl+xop
   LOG_FILE=>> FileLocation of Log file
   EMAIL_HOST_USER=YourEmailId
   EMAIL_HOST=YourHost
   EMAIL_PORT=YourPortNumber
   EMAIL_USE_TLS=True/False
   EMAIL_HOST_PASSWORD=YourPassword
   ```

   If Using Gmail

   ```DEBUG=True/False
   SECRET_KEY=x2^-!-p-y#^f%+-n*+-r%)pe+#rq#geb%&pp%se!n2$1gl+xop
   LOG_FILE=>> FileLocation of Log file
   EMAIL_HOST_USER=YourEmailId
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_PASSWORD=YourPassword
   ```

6. _Optinal_: Turn on Less Secure Apps

   If you are using Gmail, you need to turn on Less Secure Apps.
   Log in your gmail account and go to the following url:

   [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps)

   Turn it on to use it.

7. Create a django superuser

   ```
   python manage.py createsuperuser
   Username: your_username
   Email address: your_email@example.com
   Password: **********
   Password (again): *********
   Superuser created successfully.
   ```

8. Run the server

   `python manage.py runserver`

   or

   `python3 manage.py runserver`

9. Open `localhost:8000` and log in.

   Add the websites that you want to monitor in the database.

10. Add the cronjob

    `python manage.py crontab add`

    or

    `python3 manage.py crontab add`

11. Enjoy

### Author

[Debajyoti Dutta](https://github.com/DeboDevelop)
