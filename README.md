Hospital Appointment System – Django
  - A full-stack hospital appointment booking system built using Django, featuring:
  - Patient login & dashboard
  - Doctor login & dashboard
  - Admin login & management
  - Appointment booking with timeslots

STEPS TO RUN THIS PROJECT LOCALLY IN YOUR MACHINE :

1) Clone the repository
    -git clone https://github.com/premklp16/ams.git
    -cd ams
2) Create environment variable
    - python -m venv venv
    - To activate, venv/scripts/activate
3) Install dependencies
    - pip install -r requirements.txt
4) Install PostgreSQL and pgAdmin4
    - Download PostgreSQL from https://www.postgresql.org/download/
    - Download pgAdmin4 from https://www.pgadmin.org/download/
    - Open pgAdmin4, CREATE DATABASE hospital_db
    - Update setting.py in folder ams
        - DATABASES = {
                'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'hospital_db',
                'USER': 'postgres',
                'PASSWORD': 'your_password',
                'HOST': 'localhost',
                'PORT': '5432',
                            }
                      }
6) Run migrations
    - python manage.py makemigrations
    - python manage.py migrate
7) Create super user
    - python manage.py createsuperuser
8) Run the server
    - python manage.py runserver
    - Open in browser, 127.0.0.1:8000/

Getting into the project:
1) Home page:
    It comes with Hospital details and login for admin, doctor and patient.
   <img width="1891" height="882" alt="Screenshot 2025-12-05 143824" src="https://github.com/user-attachments/assets/aaaec837-d65e-4a27-907c-3f92e2a02368" />
   <img width="1884" height="869" alt="Screenshot 2025-12-05 143849" src="https://github.com/user-attachments/assets/9229ff56-4aa6-45ff-a8fd-2cacef5940fe" />
   
2) Patient dashboard:
   Patient can book appointment.
   <img width="1814" height="833" alt="Screenshot 2025-12-05 144045" src="https://github.com/user-attachments/assets/11baf513-60f4-4071-99e0-19454cc339c2" />
   
3) Doctor dashboard:
   Doctor can view his appointments for today and upcoming days and also can view his profile.
   <img width="1879" height="868" alt="Screenshot 2025-12-05 144133" src="https://github.com/user-attachments/assets/28f1fba1-49af-4a89-aa85-efac895000b2" />
   
4) Admin dashboard:
   Admin can view number of doctors working, registered patient, appointments today.
   <img width="1896" height="863" alt="Screenshot 2025-12-05 144207" src="https://github.com/user-attachments/assets/65cc890e-2f4c-484c-8dbb-cfa9e132245b" />

   And also admin can view, add and deactivate doctors and patient
   <img width="1866" height="819" alt="image" src="https://github.com/user-attachments/assets/16ea54ea-fb04-4a58-9b2b-5e93f3c40ed5" />

 
 



   
