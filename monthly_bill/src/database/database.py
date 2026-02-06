from config.db import db

def get_bills():
    print("teste")
    db.execute("SELECT * FROM bill;")
    teste = db.fetchall()
    return teste