import mysql.connector


# Подключение
conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    port=3306,
    user="sql12779108",
    password="lpcFY6NmfT",
    database="sql12779108"
)

cursor = conn.cursor()

# Выполним запрос
cursor.execute("SELECT * FROM Document LIMIT 5")

# Получим результат
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закроем соединение
cursor.close()
conn.close()