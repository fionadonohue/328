from flask import Flask, url_for, render_template, request
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
            a2 = request.form["a2"]
            a3 = request.form["a3"]
            a4 = request.form["a4"]
            a5 = request.form["a5"]
            a6 = request.form["a6"]
            a7 = request.form["a7"]
            a8 = request.form["a8"]

            place = get_place(a2, a3, a4, a5, a6, a7, a8)
            return render_template("populations.html", city = place)
    else:
        return render_template("home.html")
@app.route("/response")
def render_page2():
    return render_template('response.html')

def get_place(a2, a3, a4, a5, a6, a7, a8):
    sum = int(a2) + int(a3) + int(a4) + int(a5) + int(a6) + int(a7) + int(a8)
    if (sum>=28):
        place = "New York City, New York"

    if (28>sum>=21):
        place = "Austin, Texas"

    if (sum<21):
        place = "Sedona, Arizona"

    return place
