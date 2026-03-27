from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# 🔢 VISITOR COUNTER (SAFE)
def get_visitors():
    try:
        if not os.path.exists("counter.txt"):
            with open("counter.txt", "w") as f:
                f.write("0")

        with open("counter.txt", "r") as f:
            count = int(f.read())

        count += 1

        with open("counter.txt", "w") as f:
            f.write(str(count))

        return count
    except:
        return 1


# 🏠 HOME PAGE
@app.route("/")
def home():
    try:
        if os.path.exists("data.json"):
            with open("data.json") as f:
                ipos = json.load(f)
        else:
            ipos = []

        # SORT SAFE
        ipos = sorted(ipos, key=lambda x: int(x.get("GMP", 0)), reverse=True)

    except:
        ipos = []

    visitors = get_visitors()

    return render_template("index.html", ipos=ipos, visitors=visitors)


# ℹ️ ABOUT PAGE
@app.route("/about")
def about():
    return render_template("about.html")


# 🛠 SERVICES PAGE
@app.route("/services")
def services():
    return render_template("services.html")


# 🚀 RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)