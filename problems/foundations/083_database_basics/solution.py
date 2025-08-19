"""
Solution for Database Basics with SQLite
Problem ID: F083
"""

import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="test.db"):
        # TODO: Implement your solution here
        pass
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.connection.row_factory = sqlite3.Row
            return True
        except sqlite3.Error:
            return False
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def create_table(self, table_name, columns):
        if not self.connection:
            return False
        
        try:
            column_defs = []
            for col_name, col_type in columns.items():
                column_defs.append(f"{col_name} {col_type}")
            
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
            self.connection.execute(query)
            self.connection.commit()
            return True
        except sqlite3.Error:
            return False
    
    def insert_record(self, table_name, data):
        if not self.connection:
            return False
        
        try:
            columns = list(data.keys())
            placeholders = ['?' for _ in columns]
            values = list(data.values())
            
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
            self.connection.execute(query, values)
            self.connection.commit()
            return True
        except sqlite3.Error:
            return False
    
    def select_records(self, table_name, where_clause=None):
        if not self.connection:
            return []
        
        try:
            query = f"SELECT * FROM {table_name}"
            if where_clause:
                query += f" WHERE {where_clause}"
            
            cursor = self.connection.execute(query)
            return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error:
            return []
    
    def update_record(self, table_name, data, where_clause):
        if not self.connection:
            return False
        
        try:
            set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            self.connection.execute(query, list(data.values()))
            self.connection.commit()
            return True
        except sqlite3.Error:
            return False
    
    def delete_record(self, table_name, where_clause):
        if not self.connection:
            return False
        
        try:
            query = f"DELETE FROM {table_name} WHERE {where_clause}"
            self.connection.execute(query)
            self.connection.commit()
            return True
        except sqlite3.Error:
            return False

def main():
    print("Database Basics Examples:")
    
    # Create database manager
    db = DatabaseManager("example.db")
    
    # Connect and create table
    if db.connect():
        print("Connected to database")
        
        # Create users table
        columns = {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT NOT NULL",
            "email": "TEXT UNIQUE",
            "age": "INTEGER"
        }
        
        if db.create_table("users", columns):
            print("Table created successfully")
            
            # Insert sample data
            user_data = {"name": "John Doe", "email": "john@example.com", "age": 30}
            if db.insert_record("users", user_data):
                print("Record inserted successfully")
                
                # Select records
                records = db.select_records("users")
                print(f"Selected records: {records}")
        
        db.disconnect()
        
        # Cleanup test database
        if os.path.exists("example.db"):
            os.remove("example.db")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")
