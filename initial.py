#импортируем либу для рабты с зами
import sqlite
#делаем соединение дл бд и проверяем базу или создаем новую
connection = sqlite3.connect('data.db')
#закрываем соединение
connection.close()
