import psycopg2
from config import DB_VARS

conn = psycopg2.connect(
    host = DB_VARS['HOST'],
    database = DB_VARS['DATABASE'],
    user = DB_VARS['USER'],
    password = DB_VARS['PASSWORD']
)

cur = conn.cursor()
cur.execute("SELECT * FROM public.\"Batters\"")
batter = cur.fetchone()

print(batter)