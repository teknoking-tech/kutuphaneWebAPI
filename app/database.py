import os
import oracledb

# database.py
def get_db_connection():
    return oracledb.connect(
        user=os.getenv("DB_USER"),       # SYSTEM
        password=os.getenv("DB_PASSWORD"), # MyPassword123
        dsn=f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_SERVICE_NAME')}"
    )