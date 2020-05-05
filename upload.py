#!/usr/bin/python3

import getpass
import pg8000

class uploader:#this class handles the upload of a csv while iterating through it
    def __init__(self):
        #user = input("Username: ")
        #secret = getpass.getpass()
        user="erickgomez"
        secret="youarewhatyouyeeet"
        self.db=pg8000.connect(user=user, password=secret, host='bartik.mines.edu', database='csci403')
        self.cursor=self.db.cursor()
    def create_table(self, table_name, col_names):
        self.cursor.execute("DROP TABLE IF EXISTS "+table_name)
        query ='CREATE TABLE '+table_name +' (%s)' % ','.join(str(i)+' text' for i in col_names)
        print(query)
        self.cursor.execute(query)
        self.db.commit()
    def insert_row(self, table_name, content):
        query = 'INSERT INTO '+table_name+ ' VALUES (%s) ' %','.join("'"+str(i)+"'" for i in content)
        # print(query)
        try:
            self.cursor.execute(query)
        except(pg8000.core.ProgrammingError):
            query='INSERT INTO '+table_name+ ' VALUES (%s) ' %','.join('"'+str(i)+'"' for i in content)
        # self.db.commit()
    def commit(self):
        self.db.commit()
