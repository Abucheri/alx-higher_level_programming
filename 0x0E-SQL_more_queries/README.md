# 0x0E. SQL - More queries

0. My privileges!
	- Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).
	```
	guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
	guillaume@ubuntu:~/$ 
	guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
	Enter password: 
	guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
	Enter password: 
	guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	Grants for user_0d_1@localhost                                                                                                
	GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
	GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
	ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
	guillaume@ubuntu:~/$ 
	```
