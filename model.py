import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


data = pd.read_csv('diabetes_data_upload.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Encoding each column manually, there was an issue trying to use One Hot Encoding or Ordinal Encoding.


def diabetes_rate(categories_from_form):
    age = X[:, 0]

    for h in range(0, len(age)):
        if age[h] > 65:
            age[h] = 0
        elif age[h] >= 20 or age[h] <= 65:
            age[h] = 1

    age = age.reshape(-1, 1)

    gender = X[:, 1]

    for i in range(0, len(gender)):
        if gender[i] == 'Male':
            gender[i] = 1
        elif gender[i] == 'Female':
            gender[i] = 0

    gender = gender.reshape(-1, 1)

    # For polyuria

    polyuria = X[:, 2]

    for j in range(0, len(polyuria)):
        if polyuria[j] == 'Yes':
            polyuria[j] = 1
        elif polyuria[j] == 'No':
            polyuria[j] = 0

    polyuria = polyuria.reshape(-1, 1)

    # For Polydipsia

    polydipsia = X[:, 3]

    for k in range(0, len(polydipsia)):
        if polydipsia[k] == 'Yes':
            polydipsia[k] = 1
        elif polydipsia[k] == 'No':
            polydipsia[k] = 0

    polydipsia = polydipsia.reshape(-1, 1)

    # For sudden weight loss

    weight_loss = X[:, 4]

    for l in range(0, len(weight_loss)):
        if weight_loss[l] == 'Yes':
            weight_loss[l] = 1
        elif weight_loss[l] == 'No':
            weight_loss[l] = 0

    weight_loss = weight_loss.reshape(-1, 1)

    # For weakness

    weakness = X[:, 5]

    for m in range(0, len(weakness)):
        if weakness[m] == 'Yes':
            weakness[m] = 1
        elif weakness[m] == 'No':
            weakness[m] = 0

    weakness = weakness.reshape(-1, 1)

    # For Polyphagia

    polyphagia = X[:, 6]

    for n in range(0, len(polyphagia)):
        if polyphagia[n] == 'Yes':
            polyphagia[n] = 1
        elif polyphagia[n] == 'No':
            polyphagia[n] = 0

    polyphagia = polyphagia.reshape(-1, 1)

    genital_thrush = X[:, 7]

    for o in range(0, len(genital_thrush)):
        if genital_thrush[o] == 'Yes':
            genital_thrush[o] = 1
        elif genital_thrush[o] == 'No':
            genital_thrush[o] = 0

    genital_thrush = genital_thrush.reshape(-1, 1)

    # For visual_blurring

    visual_blurring = X[:, 8]

    for p in range(0, len(visual_blurring)):
        if visual_blurring[p] == 'Yes':
            visual_blurring[p] = 1
        elif visual_blurring[p] == 'No':
            visual_blurring[p] = 0

    visual_blurring = visual_blurring.reshape(-1, 1)

    itching = X[:, 9]

    for q in range(0, len(itching)):
        if itching[q] == 'Yes':
            itching[q] = 1
        elif itching[q] == 'No':
            itching[q] = 0

    itching = itching.reshape(-1, 1)

    # For irritability

    irritability = X[:, 10]

    for r in range(0, len(irritability)):
        if irritability[r] == 'Yes':
            irritability[r] = 1
        elif irritability[r] == 'No':
            irritability[r] = 0

    irritability = irritability.reshape(-1, 1)

    delayed_healing = X[:, 11]

    for s in range(0, len(delayed_healing)):
        if delayed_healing[s] == 'Yes':
            delayed_healing[s] = 1
        elif delayed_healing[s] == 'No':
            delayed_healing[s] = 0

    delayed_healing = delayed_healing.reshape(-1, 1)

    # For paresis

    paresis = X[:, 12]

    for t in range(0, len(paresis)):
        if paresis[t] == 'Yes':
            paresis[t] = 1
        elif paresis[t] == 'No':
            paresis[t] = 0

    paresis = paresis.reshape(-1, 1)

    muscle_stiffness = X[:, 13]

    for u in range(0, len(muscle_stiffness)):
        if muscle_stiffness[u] == 'Yes':
            muscle_stiffness[u] = 1
        elif muscle_stiffness[u] == 'No':
            muscle_stiffness[u] = 0

    muscle_stiffness = muscle_stiffness.reshape(-1, 1)

    # For alopecia

    alopecia = X[:, 14]

    for v in range(0, len(alopecia)):
        if alopecia[v] == 'Yes':
            alopecia[v] = 1
        elif alopecia[v] == 'No':
            alopecia[v] = 0

    alopecia = alopecia.reshape(-1, 1)

    obesity = X[:, 15]

    for w in range(0, len(obesity)):
        if obesity[w] == 'Yes':
            obesity[w] = 1
        elif obesity[w] == 'No':
            obesity[w] = 0

    obesity = obesity.reshape(-1, 1)

    diabetes = y

    for x in range(0, len(diabetes)):
        if diabetes[x] == 'Positive':
            diabetes[x] = 1
        elif diabetes[x] == 'Negative':
            diabetes[x] = 0

    diabetes = diabetes.reshape(-1, 1)

    categories = np.concatenate(([age, gender, polyuria, polydipsia, weight_loss, weakness, polyphagia, genital_thrush,
                                  visual_blurring, itching, irritability, delayed_healing, paresis, muscle_stiffness,
                                  alopecia, obesity]), 1)

    categories_train, categories_test, diabetes_train, diabetes_test = \
        train_test_split(categories, diabetes, test_size = 0.25, random_state = 0)

    classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)

    # I had to cast the dependent variable as an 'int'. In the original data, it was an 'int64', but got an error that
    # it had become a column vector instead of a 1d array

    diabetes_train = diabetes_train.astype('int')

    # Making the dependent variable a 1d array

    diabetes_train = diabetes_train.ravel()

    # Fitting the Logistic Regression Model

    classifier.fit(categories_train, diabetes_train)

    diabetes_pred = classifier.predict([categories_from_form])

    result = None

    if diabetes_pred == 0:
        result = 'You do not have symptoms of Diabetes'
    elif diabetes_pred == 1:
        result = 'You have symptoms of Diabetes'
    else:
        result = 'Your symptoms are inconclusive at the moment. You can fill the form again'

    return result
