from flask import Flask, url_for, render_template, request
import json

webapp = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)


@webapp.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST": #if submit button is hit and data is updated
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        county = request.form["county"]

        ten_pop, fourteen_pop, percent_change, county_name, med_income, ownership_rate, households = get_info(data, county)

        return render_template("populations.html", countyname = county_name , json = data, ten_population = ten_pop , fourteen_population = fourteen_pop, percent_population = percent_change)
    else:
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        return render_template("populations.html", json = data)

#Housing
@webapp.route("/housing", methods = ["POST", "GET"])
def housing():
    if request.method == "POST": #if submit button is hit and data is updated
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        county = request.form["county"]

        ten_pop, fourteen_pop, percent_change, county_name, med_income, ownership_rate, households = get_info(data, county)

        return render_template("housing.html", countyname = county_name , json = data, medianincome = med_income, ownershiprate = ownership_rate, numhouseholds = households)
    else:
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        return render_template("housing.html", json = data)



#Housing


def get_info(data, county):
    for i in range(len(data)):
        if data [i]["County"] == county:
            #pop
            fourteen_pop = int(data[i]["Population"]["2014 Population"])
            ten_pop = int(data[i]["Population"]["2010 Population"])
            countyname = data[i]["County"]
            #pop

            #housing
            med_income = int(data[i]["Housing"]["Median Value of Owner-Occupied Units"])
            ownership_rate = int(data[i]["Housing"]["Homeownership Rate"])
            households = int(data[i]["Housing"]["Households"])
            #housing

            percent_change = str(round((((fourteen_pop - ten_pop) / ten_pop) * 100), 2))

            percent_change_string = percent_change + "%"
            return ten_pop, fourteen_pop, percent_change_string, countyname, med_income, ownership_rate, households

    return false

if __name__ == "__main__":
    webapp.run(debug=True)
