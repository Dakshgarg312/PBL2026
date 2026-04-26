#!C:/PROGRA~1/Python311/python.exe
import cgi
from db import connect

print("Content-type: text/html\n")

form = cgi.FieldStorage()

item_id = form.getvalue("id")
name = form.getvalue("name")
contact = form.getvalue("contact")
proof = form.getvalue("proof")

if not item_id or not name or not contact:
    print("<h3>Missing required fields</h3>")
    exit()

conn = connect()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO claims (item_id, name, contact, proof, status) VALUES (%s, %s, %s, %s, 'pending')",
    (item_id, name, contact, proof)
)

conn.commit()

print("Status: 302 Found")
print("Location: /lost_found/index.html")
