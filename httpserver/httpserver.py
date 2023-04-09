from http.server import BaseHTTPRequestHandler, HTTPServer

import psycopg2 as pg2
import os

class Database:
  def __init__(self, db, username, password, dbhost, port):
    self.db = db
    self.username = username
    self.password = password
    self.dbhost = dbhost
    self.port = port
    self.cur = None
    self.conn = None

  def connect(self):
    self.conn = pg2.connect(database=self.db, user=self.username, password=self.password, host=self.dbhost, port=self.port)
    self.cur = self.conn.cursor()

  def execute_query(self, query):
    self.cur.execute(query)
    self.conn.commit()

  def close(self):
    self.cur.close()
    self.conn.close()


class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        db.execute_query("INSERT INTO requests(ipaddress) VALUES(%s)", (str(self.client_address[0])) )
        db.conn.commit()

DB_NAME = os.environ.get("DB_NAME")
DB_LOGIN = os.environ.get("DB_LOGIN")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
DB_HOST = os.environ.get("DB_HOST")

print("testing")
print(DB_HOST)
print(DB_NAME)

db = Database(DB_NAME, DB_LOGIN, DB_PASSWORD, DB_HOST, DB_PORT)
db.connect()


host = ''
port = 80
HTTPServer((host, port), HandleRequests).serve_forever()    