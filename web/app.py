from flask import Flask, request, redirect, url_for, render_template_string, session

app = Flask(__name__)
app.secret_key = "change-me-in-production"

COMMON_PASSWORDS_FILE = "10-million-password-list-top-1000.txt"
MIN_LENGTH = 12
MAX_LENGTH = 128

with open(COMMON_PASSWORDS_FILE, encoding="utf-8", errors="ignore") as f:
    COMMON_PASSWORDS = {line.strip() for line in f if line.strip()}

HOME_PAGE = """
<h2>Login</h2>
{% if error %}<p style="color:red">{{ error }}</p>{% endif %}
<form method="POST" action="/">
    <input type="password" name="password" placeholder="Enter password">
    <button type="submit">Login</button>
</form>
"""

WELCOME_PAGE = """
<h2>Welcome</h2>
<p>Your password: {{ password }}</p>
<form method="POST" action="/logout">
    <button type="submit">Logout</button>
</form>
"""


def is_valid_password(password: str) -> tuple[bool, str]:
    """OWASP ASVS 4.0.3 C6 Level 1 password checks."""
    if len(password) < MIN_LENGTH:
        return False, f"Password must be at least {MIN_LENGTH} characters."
    if len(password) > MAX_LENGTH:
        return False, f"Password must not exceed {MAX_LENGTH} characters."
    if password in COMMON_PASSWORDS:
        return False, "This password is too common. Please choose another."
    return True, ""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password", "")
        valid, error = is_valid_password(password)
        if valid:
            session["password"] = password
            return redirect(url_for("welcome"))
        return render_template_string(HOME_PAGE, error=error)
    return render_template_string(HOME_PAGE, error=None)


@app.route("/welcome")
def welcome():
    password = session.get("password")
    if not password:
        return redirect(url_for("home"))
    return render_template_string(WELCOME_PAGE, password=password)


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("password", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)