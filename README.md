Developed a CRM website using Python, Django, MySQL, HTML/CSS, Bootstrap <br/>

Quick Guide: <br/>
•	Dcrm (directory) – drcm, virt (environment) – dcrm(project) wesbsite(app)<br/>
•	Change directory to folder: cd /c/dcrm<br/>
•	Created virtual env virt: python -m venv virt<br/>
•	Activate virtual env: source virt/Scripts/activate<br/>
•	In the directory install django<br/>
•	Project name is dcrm; create project: django-admin startproject dcrm<br/>
•	Create app website: python manage.py startapp website<br/>
•	Open drcm environment in VScode<br/>
•	Change settings.py(db) in dcrm project <br/>
•	Connect to db using mydb.py <br/>
o	Create file: touch mydb.py<br/>
•	Migration <br/>
o	Python manage.py makemigrations<br/>
o	Python manage.py migrate<br/>
o	Python managepy runserver<br/>
•	Create model, register model in admin.py<br/>
•	Create superuser: python manage.py createsuperuser<br/>
<br/>



References: John_Elder@Codemy Django <br/>
