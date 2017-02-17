#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:16:29 2017

@author: vlad
"""

import mysql.connector
from mysql.connector import errorcode


class DatabaseUtility:
    def __init__(self, database, tableOne):
        self.db = database
        self.tableName = tableOne
        
        self.cnx = mysql.connector.connect(user='root', password='admin', host='127.0.0.1')
        self.cursor = self.cnx.cursor()
        
        self.ConnectToDatabase()
        self.CreateTable()
        
    
    
    def ConnectToDatabase(self):
        try:
            self.cnx.database = self.db #attempts to connect to database
                                        #if it fails - creates that database
                                        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_ER_ERROR:
                self.CreateDatabase()
                self.cnx.database = self.db   
            else:
                print (err.msg)
                
	
    def CreateDatabase(self):
        try:
            self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            
    def CreateTable(self):
        cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
            " `ID` int(5) NOT NULL AUTO_INCREMENT,"
            " 'DATE' datetime NOT NULL,"
            " 'FLOW_RATE' DECIMAL(3,2) NOT NULL,"
            " 'WAVE_LENGTH' smallint(3) NOT NULL, "
            " 'ELECTROLYTE' char(50) NOT NULL, "
            " 'VOLUME' DECIMAL(3,2) NOT NULL, "
            " 'TEMPERATURE' smallint(3) NOT NULL, "
            " 'ADSORBER' char(15) NOT NULL, "
            " PRIMARY KEY('ID') "
            " ) ENGINE=InnoDB;"               )
        self.RunCommand(cmd)
        
    def GetTable(self):
        self.CreateTable()
        return self.RunCommand("SELECT * FROM %s;" % self.tableName)

    def GetColumns(self):
        return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)
    
    def RunCommand(self, cmd):
        print ("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print ('ERROR MESSAGE: ' + str(err.msg))
            print ('WITH ' + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg
    
    def AddEntryToTable(self, DATE, FLOW_RATE, WAVE_LENGTH, ELECTROLYTE, VOLUME, TEMPERATURE, ADSORBER):
        
        cmd = " INSERT INTO " + self.tableName + "DATE, FLOW_RATE, WAVE_LENGTH, ELECTROLYTE, VOLUME, TEMPERATURE, ADSORBER"
        cmd += " VALUES  ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" %(DATE, FLOW_RATE, WAVE_LENGTH, ELECTROLYTE, VOLUME, TEMPERATURE, ADSORBER)
        self.RunCommand(cmd)
        
    def __del__(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
##===============================================
##===============================================


if __name__ == '__main__':
	db = 'chrombook'
	tableName = 'tableOne'

	dbu = DatabaseUtility(db, tableName)      
        