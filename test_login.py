def login_user(username, password):
    # VULNERABILITY: SQL Injection!
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return query
