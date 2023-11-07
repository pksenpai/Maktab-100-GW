from configparser import ConfigParser
import psycopg2


def config(filename=None, section=None):
    parser = ConfigParser()
    parser.read(filename)

    db_config = dict()
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception(f'section {section} not found')

    return db_config


def connect(conn, cur):
    if conn and cur:
        conn, cur, local_connection = conn, cur, False
    else:
        try:
            params = config('database.ini', 'hospitaldb')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            local_connection = True
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
            conn, cur, local_connection = None, None, None
    return conn, cur, local_connection


