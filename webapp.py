from flask import Flask, url_for, render_template, request
import json

webapp = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@webapp.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST": #if submit button is hit and data is updated
        with open('./demographics.json') as json_file:
            data = json.load(json_file)
        county = request.form["county"]

        ten_pop, fourteen_pop, percent_change, county_name, med_income, ownership_rate, households, white_not_hispanic, bi_racial, asian_alone, pacific_islander, white_alone, hispanic_alone, black_alone, native_alone = get_info(data, county)

#population route...

        return render_template("populations.html", countyname = county_name , json = data, ten_population = ten_pop , fourteen_population = fourteen_pop, percent_population = percent_change, )
    else:
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        return render_template("populations.html", json = data)
#...population route

#housing route...
@webapp.route("/housing", methods = ["POST", "GET"])
def housing():
    if request.method == "POST": #if submit button is hit and data is updated
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        county = request.form["county"]

        ten_pop, fourteen_pop, percent_change, county_name, med_income, ownership_rate, households, white_not_hispanic, bi_racial, asian_alone, pacific_islander, white_alone, hispanic_alone, black_alone, native_alone = get_info(data, county)

        return render_template("housing.html", countyname = county_name , json = data, medianincome = med_income, ownershiprate = ownership_rate, numhouseholds = households)
    else:
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        return render_template("housing.html", json = data)
#...housing route

#dversity route...
@webapp.route("/diversity", methods = ["POST", "GET"])
def diversity():
    if request.method == "POST": #if submit button is hit and data is updated
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        county = request.form["county"]

        ten_pop, fourteen_pop, percent_change, county_name, med_income, ownership_rate, households, white_not_hispanic, bi_racial, asian_alone, pacific_islander, white_alone, hispanic_alone, black_alone, native_alone = get_info(data, county)

        return render_template("housing.html", countyname = county_name , json = data, whitenothispanic = white_not_hispanic, biracial = bi_racial, asianalone = asian_alone, pacificislander = pacific_islander, white = white_alone, hispanic = hispanic_alone, black = black_alone, native = native_alone)
    else:
        with open('./demographics.json') as json_file:
            data = json.load(json_file)

        return render_template("diversity.html", json = data)
#...diversity route


def get_info(data, county):
    for i in range(len(data)):
        if data [i]["County"] == county:
            #population...
            fourteen_pop = int(data[i]["Population"]["2014 Population"])
            ten_pop = int(data[i]["Population"]["2010 Population"])
            countyname = data[i]["County"]
            percent_change = str(round((((fourteen_pop - ten_pop) / ten_pop) * 100), 2))
            percent_change_string = percent_change + "%"
            #...population

            #housing...
            med_income = int(data[i]["Housing"]["Median Value of Owner-Occupied Units"])
            ownership_rate = int(data[i]["Housing"]["Homeownership Rate"])
            households = int(data[i]["Housing"]["Households"])
            #...housing

#diversity...
white_not_hispanic = int(data[i]["Ethnicities"]["White Alone, not Hispanic or Latino"])
bi_racial = int(data[i]["Ethnicities"]["Two or More Races"])
asian_alone = int(data[i]["Ethnicities"]["Asian Alone"])
pacific_islander = int(data[i]["Ethnicities"]["Hispanic or Latino"])
white_alone = int(data[i]["Ethnicities"]["White Alone"])
hispanic_alone = int(data[i]["Ethnicities"]["Hispanic or Latino"])
black_alone = int(data[i]["Ethnicities"]["Black Alone"])
native_alone = int(data[i]["Ethnicities"]["American Indian and Alaska Native Alone"])
#...diversity

#white_not_hispanic, bi_racial, asian_alone, pacific_islander, white_alone, hispanic_alone, black_alone, native_alone

            return ten_pop, fourteen_pop, percent_change_string, countyname, med_income, ownership_rate, households, white_not_hispanic, bi_racial, asian_alone, pacific_islander, white_alone, hispanic_alone, black_alone, native_alone

    return false

if __name__ == "__main__":
    webapp.run(debug=True)
