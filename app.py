from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey123"


# ================= DATABASE INITIALIZATION =================
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            emoji TEXT,
            secret_question TEXT,
            secret_answer TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS login_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            status TEXT,
            ip_address TEXT,
            login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ================= HOME =================
@app.route("/")
def home():
    return redirect("/login")


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        emoji = request.form["emoji_sequence"]
        secret_question = request.form["secret_question"]
        secret_answer = request.form["secret_answer"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        try:
            c.execute("""
                INSERT INTO users 
                (username, password, emoji, secret_question, secret_answer)
                VALUES (?, ?, ?, ?, ?)
            """, (username, password, emoji, secret_question, secret_answer))
            conn.commit()
        except:
            conn.close()
            return "Username already exists!"

        conn.close()
        return redirect("/login")

    return render_template("register.html")


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        emoji = request.form["emoji_sequence"]
        ip = request.remote_addr

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute("""
            SELECT * FROM users
            WHERE username=? AND password=? AND emoji=?
        """, (username, password, emoji))

        user = c.fetchone()

        if user:

            # Delete all failed attempts for this user
            c.execute("""
                DELETE FROM login_activity
                WHERE username=? AND status='Failed'
            """, (username,))

            # Insert successful login
            c.execute("""
                INSERT INTO login_activity (username, status, ip_address)
                VALUES (?, ?, ?)
            """, (username, "Success", ip))

            conn.commit()
            conn.close()

            session["user"] = username
            return redirect("/dashboard?popup=1")

        else:

            c.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = c.fetchone()

            if existing_user:
                c.execute("""
                    INSERT INTO login_activity (username, status, ip_address)
                    VALUES (?, ?, ?)
                """, (username, "Failed", ip))
                conn.commit()

            conn.close()
            return "Invalid Credentials"

    return render_template("login.html")


# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    username = session["user"]
    show_popup = request.args.get("popup") == "1"

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Total successful logins
    c.execute("""
        SELECT COUNT(*) FROM login_activity
        WHERE username=? AND status='Success'
    """, (username,))
    login_count = c.fetchone()[0]

    # Failed attempts 
    c.execute("""
        SELECT COUNT(*) FROM login_activity
        WHERE username=? AND status='Failed'
    """, (username,))
    failed_count = c.fetchone()[0]

    # Previous successful login
    c.execute("""
        SELECT login_time FROM login_activity
        WHERE username=? AND status='Success'
        ORDER BY id DESC
        LIMIT 1 OFFSET 1
    """, (username,))
    last_login = c.fetchone()

    # Last login IP
    c.execute("""
        SELECT ip_address FROM login_activity
        WHERE username=? AND status='Success'
        ORDER BY id DESC
        LIMIT 1
    """, (username,))
    last_ip = c.fetchone()

    conn.close()

    security_score = 100 - (failed_count * 10)
    if security_score < 0:
        security_score = 0

    active_sessions = 1

    return render_template(
        "dashboard.html",
        user=username,
        login_count=login_count,
        failed_count=failed_count,
        last_login=last_login,
        last_ip=last_ip,
        security_score=security_score,
        active_sessions=active_sessions,
        show_popup=show_popup
    )


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ================= RUN APP =================
if __name__ == "__main__":
    app.run(debug=True)