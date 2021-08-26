to launch the project locally: 
run the following series of commands:
1) virtualenv venv --python=python3
2) pip3 install psycopg2-binary
3) source venv/bin/activate
4) pip3 install -r requirements.txt
5) change the postgres database username and password to your root user
6) run the SQL script on our postgres DB to import the data
7) python3 manage.py runserver
