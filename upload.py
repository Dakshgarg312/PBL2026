#!C:/PROGRA~1/Python311/python.exe
import cgi, os, uuid
from db import connect

print("Content-type: text/html\n")

form = cgi.FieldStorage()

name = form.getvalue("name")
desc = form.getvalue("desc")
location = form.getvalue("location")
date = form.getvalue("date")
fileitem = form["image"]

if fileitem.filename:
    filename = str(uuid.uuid4()) + "_" + os.path.basename(fileitem.filename)
    filepath = "images/" + filename

    with open("C:/xampp/htdocs/lost_found/" + filepath, "wb") as f:
        f.write(fileitem.file.read())

    conn = connect()
    cursor = conn.cursor()

    item_id = str(uuid.uuid4())

    cursor.execute(
        "INSERT INTO items VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (item_id,name,desc,location,date,filepath,"available")
    )

    conn.commit()

print("<h2>Item Uploaded</h2>")
print("<a href='/lost_found/index.html'>Back</a>")