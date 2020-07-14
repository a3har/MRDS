service mysql start
echo "Initializing database .."
mysql -e "create database rajagirihospital1;use rajagirihospital1;create table report (Patient_ID varchar(50),Test_Parameter varchar(100),Value varchar(50),Unit varchar(50),Date varchar(50),Time varchar(50),Test_Name varchar(100),Original_Range varchar(50),Conditions varchar(50),Remarks varchar(50),path varchar(50));create table details (Patient_ID varchar(50),age varchar(100),sex varchar(50),documents varchar(100));use mysql;UPDATE mysql.user SET Password=PASSWORD('mypass') WHERE User='root';SET PASSWORD FOR 'root'@'localhost' = PASSWORD('mypass');FLUSH PRIVILEGES;"
echo "Running server at 0.0.0.0:8000"
python3 rajagiri/manage.py runserver 0.0.0.0:8000