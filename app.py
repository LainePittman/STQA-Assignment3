from flask import Flask, request, jsonify
from views import views
from person import Person, parseAndConvert, poundToKilograms, calcBMI, BMIcat

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    # Getting form data

    name = request.form['Name']
    height_input = request.form['Height']
    weight_input = float(request.form['Weight'])

    # Parse and convert height
    total_cm = parseAndConvert(height_input)

    # Convert weight from lbs to kg
    kilos = poundToKilograms(weight_input)

    # Calculate BMI
    BMI = calcBMI(total_cm, kilos)

    # Determine BMI category
    category = BMIcat(BMI)

    # Create a Person instance
    person = Person(name, total_cm, weight_input, BMI, category)

    return jsonify({
        'name': person.name,
        'height_cm': person.height,
        'weight_lbs': person.weight,
        'BMI': person.BMI,
        'category': person.category
    })

if __name__ == "__main__":
    app.run(debug=True)