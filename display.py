#!C:/PROGRA~1/Python311/python.exe
from db import connect

print("Content-type: text/html\n")

conn = connect()
cursor = conn.cursor()

cursor.execute("SELECT * FROM items WHERE status!='returned'")
rows = list(cursor.fetchall())

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][4] < right[j][4]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

merge_sort(rows)

item_map = {}
for item in rows:
    item_map[item[0]] = item

print("<html><body>")

for item in rows:
    print(f"""
    <div>
    <img src='/lost_found/{item[5]}' width='150'><br>
    <b>{item[1]}</b><br>
    <p>Date: {item[4]}</p>
    <a href='/lost_found/view.html?id={item[0]}'>View</a>
    </div><hr>
    """)

print("</body></html>")