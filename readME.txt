This is a Django/Python Project
1. When you run the server you'll be taken to the index.html page where you will be shown a button to get all doctors. I manually created doctors within the shell, so please refer to the models.py file to be able to appropriately create the doctor object prior to hitting the button. This will be your conventional GET request and list out all the doctors using an HttpResponse while being in json format.

2. Get a list of all appointments for a particular doctor on a particular day. This is your typical GET request, and I created the appoinments within the shell. Please refer to the models.py file to be able to do that correctly. Once created, I was able to return the HttpResponse of aall the appoinments using json format.

3. Deleting an appoinment is a POST request. Passing the correct appointment (created appoinments in the shell), I was able to then delete. I initially ran this block without the IF statement on line 30 while passing the necessary information through the URL. This might work better by removing that line since we dont have a front end, however, I thought to include it for back end purposes.

4. For the last question, I included an additional html page with some basic text fields to fill out for the form. I didnt worry too much about the drop down to increment the time every 15 minutes because thats a front end task, however, I put in an IF statement check for that using the modulus operator. The did the necessary checks to ensure the remaining instructions per the project were met as well (i.e., no more than 3 appoiments per doctor at a particular time).

**Slightly challenging to build without a front end however this was a ton of fun!

Installations have been listed below:

aiohttp==3.6.2
astroid==2.4.2
async-timeout==3.0.1
attrs==20.2.0
bcrypt==3.1.7
cachetools==4.1.1
certifi==2020.6.20
cffi==1.14.1
chardet==3.0.4
Django==2.2
django-easy-timezones==0.8.0
google-api-core==1.22.2
google-api-python-client==1.12.2
google-auth==1.22.0
google-auth-httplib2==0.0.4
googleapis-common-protos==1.52.0
haversine==2.3.0
httplib2==0.18.1
idna==2.10
ipaddress==1.0.16
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
multidict==4.7.6
Pillow==7.2.0
protobuf==3.13.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
pygeoip==0.3.2
pylint==2.5.3
pytz==2016.6
requests==2.24.0
rsa==4.6
six==1.15.0
sqlparse==0.3.1
toml==0.10.1
uritemplate==3.0.1
urllib3==1.25.10
wrapt==1.12.1
yarl==1.6.0