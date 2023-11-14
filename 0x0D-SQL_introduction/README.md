# 0x0D. SQL - Introduction

0. List databases
	- Write a script that lists all databases of your MySQL server.
	```
	guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	Database                                                                                     
	hbtn_0c_0                                                                                    
	information_schema                                                                           
	mysql                                                                                        
	performance_schema                                                                           
	sys        
	guillaume@ubuntu:~/$ 
	```

1. Create a database
	- Write a script that creates the database `hbtn_0c_0` in your MySQL server.
		- If the database `hbtn_0c_0` already exists, your script should not fail
		- You are not allowed to use the `SELECT` or `SHOW` statements
	```
	guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	Database
	information_schema
	hbtn_0c_0
	mysql
	performance_schema
	guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	guillaume@ubuntu:~/$ 
	```

2. Delete a database
	- Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
		- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
		- You are not allowed to use the `SELECT` or `SHOW` statements
	```
	guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	Database                                                                                     
	hbtn_0c_0                                                                                    
	information_schema                                                                           
	mysql                                                                                        
	performance_schema                                                                           
	sys        
	guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
	Enter password: 
	Database                                                                                                                                                                  
	information_schema                                                                           
	mysql                                                                                        
	performance_schema                                                                           
	sys        
	guillaume@ubuntu:~/$ 
	```

3. List tables
	- Write a script that lists all the tables of a database in your MySQL server.
		- The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)
	```
	guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
	Enter password: 
	Tables_in_mysql                                                                              
	columns_priv                                                                                 
	component                                                                                    
	db                                                                                           
	default_roles                                                                                
	engine_cost                                                                                  
	func                                                                                         
	general_log                                                                                  
	global_grants                                                                                
	gtid_executed                                                                                
	help_category                                                                                
	help_keyword                                                                                 
	help_relation                                                                                
	help_topic                                                                                   
	innodb_index_stats                                                                           
	innodb_table_stats                                                                           
	password_history                                                                             
	plugin                                                                                       
	procs_priv                                                                                   
	proxies_priv                                                                                 
	replication_asynchronous_connection_failover                                                 
	replication_asynchronous_connection_failover_managed                                         
	role_edges                                                                                   
	server_cost                                                                                  
	servers                                                                                      
	slave_master_info                                                                            
	slave_relay_log_info                                                                         
	slave_worker_info                                                                            
	slow_log                                                                                     
	tables_priv                                                                                  
	time_zone                                                                                    
	time_zone_leap_second                                                                        
	time_zone_name                                                                               
	time_zone_transition                                                                         
	time_zone_transition_type                                                                    
	user
	guillaume@ubuntu:~/$ 
	```

4. First table
	- Write a script that creates a table called `first_table` in the current database in your MySQL server.
		- `first_table` description:
			- `id` INT
			- `name` VARCHAR(256)
		- The database name will be passed as an argument of the `mysql` command
		- If the table `first_table` already exists, your script should not fail
		- You are not allowed to use the `SELECT` or `SHOW` statements
	```
	guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	Tables_in_hbtn_0c_0
	first_table
	guillaume@ubuntu:~/$ 
	```

5. Full description
	- Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
		- The database name will be passed as an argument of the `mysql` command
		- You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements
	```
	guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	Table   Create Table                                                                         
	first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
	guillaume@ubuntu:~/$ 
	```

6. List all in table
	- Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
		- All fields should be printed
		- The database name will be passed as an argument of the `mysql` command
	```
	guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	guillaume@ubuntu:~/$ 
	```

7. First add
	- Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
		- New row:
			- `id` = `89`
			- `name` = `Best School`
		- The database name will be passed as an argument of the `mysql` command
	```
	guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	id  name
	89  Best School
	guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	id  name
	89  Best School
	89  Best School
	89  Best School
	guillaume@ubuntu:~/$ 
	```

8. Count 89
	- Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
		- The database name will be passed as an argument of the `mysql` command
	```
	guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
	Enter password: 
	3
	guillaume@ubuntu:~/$ 
	```

9. Full creation
	- Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
		- `second_table` description:
			- `id` INT
			- `name` VARCHAR(256)
			- `score` INT
		- The database name will be passed as an argument to the `mysql` command
		- If the table `second_table` already exists, your script should not fail
		- You are not allowed to use the `SELECT` and `SHOW` statements
		- Your script should create these records:
			- `id` = 1, `name` = “John”, `score` = 10
			- `id` = 2, `name` = “Alex”, `score` = 3
			- `id` = 3, `name` = “Bob”, `score` = 14
			- `id` = 4, `name` = “George”, `score` = 8
	```
	guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
	Enter password: 
	guillaume@ubuntu:~/$ 
	```
