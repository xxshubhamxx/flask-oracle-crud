# flask-oracle-crud

Basic CRUD Application using Flask and Oracle DB.

This app performs all 4 CRUD (Create, Reas, Update, Delete) Operations.

To use the project on your local system, you'll have to download the oracle database XE 10g (any version will work fine)

while installing oracle database on your system, it will ask you to create a password (which can be changed later), so either setup the password/change the password to ```system``` or change the 8th line of app.py in this format:
```connection=cx_Oracle.connect("system/<your_password>@localhost:1521/XE")```
replace <your_password> with your password that you set up while installing the database

Now, you need to download oracle instant client from oracle website, I have downloaded file named "instantclient-basic-windows.x64-19.12.0.0.0dbru" but anything should work.
After extracting the file, you need to add the path ```path\to\instantclient-basic-windows.x64-19.12.0.0.0dbru\instantclient_19_12``` to your system's environment variables to make it work

After this, you can start database by manually searching in start button of windows. Once the database starts, you can either choose "Go to Database Homepage" or install Oracle SQL Developer.
I'd just installing the sql developer as it povides a much better interface than the website and its easy to setup. 

Once, you're done with all that, open db.sql file in the root folder of this application. You can either copy paste the commands in your oracle sql interface to create the emp table that has been used in this application or just uncooment line 100 ``` #   createAndInsert()``` of app.py when running for first time to create and insert values in the database, then stop the application, comment out that line and run again

Then just download this repository as a zip file, extract it, open with VSCode, and open terminal at the root directory of this application, and run this command: 
```pip install -r requirements.txt```

and then just run the app.py present in root folder of this application. Then just go to ```http://127.0.0.1:8000/``` in your browser to see the webpage.
