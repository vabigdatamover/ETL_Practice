import psycopg2 #import the postgres library

#connect to the database
conn = psycopg2.connect(host='localhost',
                       dbname='database1',
                       user='postgres',
                       password='password',
                        port='5432')  
#create a cursor object 
#cursor object is used to interact with the database
cur = conn.cursor()

#create table with same headers as csv file
cur.execute("CREATE TABLE IF NOT EXISTS test(state text, latitude float, longitude float, code text)")

#open the csv file using python standard file I/O
#copy file into the table just created 
with open('state_cords.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'test', sep=',')
    conn.commit()
    conn.close()

f.close()