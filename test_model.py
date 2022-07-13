import joblib

def load_model():
    return joblib.load('regression.joblib')

model = load_model()

X = [[100, 3, 0]]
prediction = model.predict(X)
actual_result = prediction

assert 0 < actual_result , "C kc"