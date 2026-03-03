# Authenticates a user by checking credentials against a SQLite database.
import sqlite3

def authenticate(username, password):
    conn = sqlite3.connect("app.db")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = conn.execute(query).fetchone()
    conn.close()

    if result:
        return {"status": "success", "user": result}
    else:
        return {"status": "fail", "message": f"No account found for {username}"}
