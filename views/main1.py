# importing Flask and other modules
from flask import Flask, request, render_template, url_for
from geopy.geocoders import Nominatim
from geopy import distance
from flask import Blueprint

#app = Flask(__name__)
app1 = Blueprint('app1', __name__,template_folder="templates")


@app1.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        # I get moscow cordinate (right langtitude top latitude from api)
        a, b, km = konum(first_name, last_name)
        # I get moscow cordinate (left langtitude bottom latitude input manually because of api return map center )
        bottom = 55.503
        left = 37.329

        ##area check
        if bottom < b[0] < a[0] and left < b[1] < a[1]:
            print("This area inside the MKAD")
        else:
            file = open("log.txt", "a")
            first_name = repr(first_name)
            last_name = repr(last_name)
            km = repr(km)
            file.write("Target Location = " + first_name + "\n" + "Second location = " + last_name + "\n" + "Distance (km) = " + km + "\n")
            file.close


        print(a)
        print(b)
        # return '{}  {} {} // {} {} '.format(a, b, km ,first_name ,last_name )
        return render_template('result.html', first_name=a, last_name=b, km=km)

    return render_template('den.html')


geolocator = Nominatim(user_agent="geoapiExercises")


def konum(Input_place1, Input_place2):
    # Get location of the input strings
    place1 = geolocator.geocode(Input_place1)
    place2 = geolocator.geocode(Input_place2)

    # Get latitude and longitude
    Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
    Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

    location1 = (Loc1_lat, Loc1_lon)
    location1_list = list(location1)
    location2 = (Loc2_lat, Loc2_lon)
    location2_list = list(location2)

    print(location1)
    print(location2)

    km = distance.distance(location1, location2).km

    return location1_list, location2_list, km



#
# if __name__ == '__main__':
#     #app.register_blueprint(app ,url_prefix="/")
#     app1.run()
