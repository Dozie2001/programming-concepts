# 0x0F. Python - Object-relational mapping
A repo that shows the linkinking of Databases and Python

# **Tasks**

### **[0.Get all states](0-select_states.py)**
A  a script that lists all states from the database `hbtn_0e_0_usa`:
  * Your script should take 3 arguments: `mysql username`, `mysql password` and database name (no argument validation needed)
  * You must use the module MySQLdb (import MySQLdb)
  * Your script should connect to a MySQL server running on localhost at port `3306`
  * Results must be sorted in ascending order by states.id
  * Results must be displayed as they are in the example below
  * Your code should not be executed when imported
``` bash
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

### **[1. Filter states](1-filter_states.py)**
A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
   * Your script should take 3 arguments: `mysql username`, `mysql password` and database name (no argument validation needed)
   * You must use the module `MYSQLdb` (`import MYSQLdb`)
   * Your script should connect to a MySQL server running on `localhost` at port `3306`
   * Results  must be sorted in ascending order by `states.id`
   * Results  must be displayed as they are in the example below
   * Your code should not be executed when imported
``` bash
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
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

### **[2. Filter states by user input](2-my_filter_states.py)**
A  script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
  * Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
  * Your script should connect to a MySQL server running on localhost at port `3306`
  * You must be sorted in ascending order by states.id
``` bash
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
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
### **[3. SQL Injection...](3-my_safe_filter_states.py)
A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
 * Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
 * You must use the module MySQLdb (import MySQLdb)
 * Your  script should connect to a MySQL server running on localhost at port 3306
 * Results must be sorted in ascending order by states.id
 * Results must be displayed as they are in the example below
 * Your code should not be executed when imported
``` bash
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
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
### **[5. All cities by state](5-filter_cities.py)
A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
  * Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
  * You must use the module MySQLdb (import MySQLdb)
  * Your script should connect to a MySQL server running on localhost at port 3306
  * Results must be sorted in ascending order by cities.id
  * You can use only execute() once
  * The results must be displayed as they are in the example below
  * The results must be displayed as they are in the example below
``` bash 
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_
```
### **[6. First state model](model_state.py)**
![Image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230401%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230401T160029Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ec7b17e561316200125339ba0d5432f488f8b78f08e0e7ecb52e4c19f34edb19)