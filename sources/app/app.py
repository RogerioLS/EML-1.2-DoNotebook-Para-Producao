from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Carregar o modelo treinado com pickle
with open('modelo_churn.pkl', 'rb') as file:
    model = pickle.load(file)

# Definir rota para predições
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = data['features']
        prediction = model.predict([features])
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
