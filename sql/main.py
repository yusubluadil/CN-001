"""

SQL - Structed Query Language (PostgreSQL, MSSQL, MySQL, Sqlite, MongoDB, Cassandra, Redis, etc)


Relational, NoRelational

Relational - PostgreSQL, MSSQL, MySQL, Sqlite

NoRelational - MongoDB, Cassandra, Redis

Database - Məlumatların saxlandığı yer

Data - Məlumat

"""


import psycopg2


conn = psycopg2.connect(
    dbname="Employee",
    user="postgres",
    password="azerbaycan444",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS employees (
id SERIAL PRIMARY KEY,
name VARCHAR(100),
age INTEGER,
department VARCHAR(50)
);
"""

# try:
cursor.execute(query)
conn.commit()
# except:
#     print('employees adlı table mövcuddur.')


#== CRUD - Create, Read, Update, Delete ==#

# create_query = """
# INSERT INTO employees (name, age, department) VALUES ('Izzet', 20, 'IT')
# """
# cursor.execute(create_query)
# conn.commit()


create_query = """
SELECT * FROM employees
"""

name = input('Adı daxil edin: ')
age = input('Yaşı daxil edin: ')
department = input('Departamenti daxil edin: ')

datas = (name, age, department)

cursor.execute(create_query, datas)
datas = cursor.fetchall()
conn.commit()
