import psycopg2
import os
import sys

connCmd = ("dbname="
           "'" + os.environ['DB_NAME'] + "' "
           "user="
           "'" + os.environ['DB_USER'] + "' "
           "password="
           "'" + os.environ['DB_PASS'] + "' "
           "host="
           "'" + os.environ['DB_SERVICE'] + "'"
           )

try:
    conn = psycopg2.connect(connCmd)
    print("Postgres db accessible")
except:
    print("Postgres db not accessible")
    sys.exit(1)
