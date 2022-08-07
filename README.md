##Learning Management System
An all in one learning management system where you can see video lectures, ask doubts and more.
The LMS has been designed by keeping the students as well as teachers in mind.

###Steps to access LMS
##Local Environment
You need to clone the repo in your local environment and run 
> pip install -r requirements.txt
 ---this will install all the dependencies in your local machine. Then run :
>python manage.py make migrations.

>python manage.py migrate.

##Access From Anywhere:

Visit: https://emraanadil.pythonanywhere.com
In the navbar you first need to go to register yourself. Login with same credentials and you will be able to access the LMS. If you aren't logged in you will be redirected to login page. In LMS page you will have different years of study. After clicking on a particular year you will have cards of courses in that particular year.From courses you can view different lectures where you will be able to acces the video lecture, post comments and replies in the lecture page.

###Note: 
As a student you will be able to only view the contents. But if you are given a staff status by the admin you can add courses , lectures and more.
##For teachers:
After grating staff access the teachers can add new courses, edit present courses and course contents, give replies to questions and update lecture details.


For any bugs please mailto:emraanadil07@gmail.com
