from configparser import ConfigParser
import psycopg2

class Database:
    def __init__(self, filename='database.ini', section='hospitaldb'):
        parser = ConfigParser()
        parser.read(filename)

        db_config = dict()
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db_config[param[0]] = param[1]
        else:
            raise Exception(f'section {section} not found')

        self.db_config = db_config
        self.conn = None
        self.cur = None
        self.local_connection = None
    
    def __enter__(self):
        if conn and cur:
            conn, cur, local_connection = conn, cur, False
        else:
            try:
                params = self.db_config
                self.conn = psycopg2.connect(**params)
                self.cur = conn.cursor()
                self.local_connection = True
            
            except (Exception, psycopg2.DatabaseError) as e:
                print(e)
                
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
    
