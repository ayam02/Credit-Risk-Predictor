from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if the form is submitted (POST request)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')   
        random = "some random variable that i want to confirm can be accessed"     
        return render_template("results.html", var = random)

    # If it's a GET request, render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)