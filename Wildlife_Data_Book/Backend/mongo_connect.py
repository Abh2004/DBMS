from pymongo import MongoClient
from urllib.parse import quote_plus

# Replace 'your_actual_password' and 'your_database_name' with your actual password and database name
password = 'Alock@123'
dbname = 'Wildlifedatabase'

# Escape the username and password using quote_plus
escaped_username = quote_plus('arjunmaurya1920')
escaped_password = quote_plus(password)

# Construct the connection URI with escaped username and password
conn_str = f"mongodb+srv://{escaped_username}:{escaped_password}@wildlifedatabase.oksw5df.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=Wildlifedatabase"
conn = MongoClient(conn_str)

# Access your database
db = conn[dbname]
