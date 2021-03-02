from flask import Flask, render_template, request, jsonify
from ski_signup import rikert_signup, bowl_signup
import json

# flask init --
app = Flask(__name__)

#db.init_app(app)
# for later

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        # handle api request
        data = json.loads(request.data)
        try:
            # parse everything in the request
            first = data['fist']
            label = data['last']
            email = data['email']
            id = data['id']
            isBowl = data['isBowl']
        except KeyError:
            return jsonify({'statusCode':400})

        response = False
        # it's times like these where I need a ternary operator to make my code look nice
        if isBowl:
            response = bowl_signup(first,last,email,id)
        else:
            response = rikert_signup(first,last,email,id)

        if response:
            return jsonify({'statusCode':200})
        # if the response from ski_signup comes out false, there's something wrong with your inputs
        return jsonify({'statusCode':402})

    else: # then return the instructions instead
        return render_template("index.html")
