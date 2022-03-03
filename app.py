from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")   #home", methods=['GET', 'POST'])
def home():
    return "Hello, Flask!"
    #return render_template(
    #    "FuelQuoteForm.html",
    #)



#if __name__ == "__main__":
 #   app.run(debug=True)