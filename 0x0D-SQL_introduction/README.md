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
