from flask import Flask, render_template, url_for, redirect, request
from model import diabetes_rate


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        # Process the various categorical user inputs

        age = request.form['age']
        age = int(age)
        if age >= 20 or age < 65:
            age = 1
        else:
            age = 0

        gender = request.form['gender']
        gender = gender.lower()
        if gender == 'male':
            gender = 1
        elif gender == 'female':
            gender = 0

        polyuria = request.form['polyuria']
        polyuria = polyuria.lower()
        if polyuria == 'yes':
            polyuria = 1
        elif polyuria == 'no':
            polyuria = 0

        polydipsia = request.form['polydipsia']
        polydipsia = polydipsia.lower()
        if polydipsia == 'yes':
            polydipsia = 1
        elif polydipsia == 'no':
            polydipsia = 0

        weight_loss = request.form['weight_loss']
        weight_loss = weight_loss.lower()
        if weight_loss == 'yes':
            weight_loss = 1
        elif weight_loss == 'no':
            weight_loss = 0

        weakness = request.form['weakness']
        weakness = weakness.lower()
        if weakness == 'yes':
            weakness = 1
        elif weakness == 'no':
            weakness = 0

        polyphagia = request.form['polyphagia']
        polyphagia = polyphagia.lower()
        if polyphagia == 'yes':
            polyphagia = 1
        elif polyphagia == 'no':
            polyphagia = 0

        genital_thrush = request.form['genital_thrush']
        genital_thrush = genital_thrush.lower()
        if genital_thrush == 'yes':
            genital_thrush = 1
        elif genital_thrush == 'no':
            genital_thrush = 0

        visual_blurring = request.form['visual_blurring']
        visual_blurring = visual_blurring.lower()
        if visual_blurring == 'yes':
            visual_blurring = 1
        elif visual_blurring == 'no':
            visual_blurring = 0

        itching = request.form['itching']
        itching = itching.lower()
        if itching == 'yes':
            itching = 1
        elif itching == 'no':
            itching = 0

        irritability = request.form['irritability']
        irritability = irritability.lower()
        if irritability == 'yes':
            irritability = 1
        elif irritability == 'no':
            irritability = 0

        delayed_healing = request.form['delayed_healing']
        delayed_healing = delayed_healing.lower()
        if delayed_healing == 'yes':
            delayed_healing = 1
        elif delayed_healing == 'no':
            delayed_healing = 0

        paresis = request.form['paresis']
        paresis = paresis.lower()
        if paresis == 'yes':
            paresis = 1
        elif paresis == 'no':
            paresis = 0

        muscle_stiffness = request.form['muscle_stiffness']
        muscle_stiffness = muscle_stiffness.lower()
        if muscle_stiffness == 'yes':
            muscle_stiffness = 1
        elif muscle_stiffness == 'no':
            muscle_stiffness = 0

        alopecia = request.form['alopecia']
        alopecia = alopecia.lower()
        if alopecia == 'yes':
            alopecia = 1
        elif alopecia == 'no':
            alopecia = 0

        obesity = request.form['obesity']
        obesity = obesity.lower()
        if obesity == 'yes':
            obesity = 1
        elif obesity == 'no':
            obesity = 0

        form_categories = [age, gender, polyuria, polydipsia, weight_loss, weakness, polyphagia, genital_thrush,
                                  visual_blurring, itching, irritability, delayed_healing, paresis, muscle_stiffness,
                                  alopecia, obesity]

        form_data = diabetes_rate(form_categories)
        return render_template('check.html', form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)




app.run(host='0.0.0.0', port=8080)