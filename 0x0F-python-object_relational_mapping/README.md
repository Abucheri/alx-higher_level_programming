# 0x0F. Python - Object-relational mapping

# Background Context
<p>In this project, you will link two amazing worlds: Databases and Python!</p>
<p>In the first part, you will use the module <strong>MySQLdb</strong> to connect to a MySQL database and execute your SQL queries.</p>
<p>In the second part, you will use the module <strong>SQLAlchemy</strong> (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).</p>
<p>
The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.</p>

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
<p>Do you see the difference? Cool, right?
The biggest difficulty with ORM is: The syntax!
Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.</p>

# More Info
## Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install `MySQLdb` module version `2.0.x`
For installing `MySQLdb`, you need to have `MySQL` installed: How to install MySQL 8.0 in Ubuntu 20.04 (use the docs)
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

## Install `SQLAlchemy` module version `1.4.x`
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```
You can ignore it.


0. Get all states
	- Write a script that lists all `states` from the database `hbtn_0e_0_usa`:
		- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
		- You must use the module `MySQLdb` (`import MySQLdb`)
		- Your script should connect to a MySQL server running on `localhost` at port `3306`
		- Results must be sorted in ascending order by `states.id`
		- Results must be displayed as they are in the example below
		- Your code should not be executed when imported
	```
	guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
	-- Create states table in hbtn_0e_0_usa with some data
	CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
	USE hbtn_0e_0_usa;
	CREATE TABLE IF NOT EXISTS states ( 
	    id INT NOT NULL AUTO_INCREMENT, 
	    name VARCHAR(256) NOT NULL,
	    PRIMARY KEY (id)
	);
	INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

	guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
	Enter password: 
	guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
	(1, 'California')
	(2, 'Arizona')
	(3, 'Texas')
	(4, 'New York')
	(5, 'Nevada')
	guillaume@ubuntu:~/0x0F$ 
	```
	- ___No test cases needed___
