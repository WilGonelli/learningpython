import mysql.connector # type: ignore

# Configuration dictionary (best practice for security)
config = {
    'user': 'root',
    'password': 'admin',
    'host': '172.21.164.50', # or your host's IP address
    'database': 'Mounthly_bills'
}

cnx = mysql.connector.connect(**config)
db = cnx.cursor()