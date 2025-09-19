from flask import Blueprint, request, jsonify
from ..models.user import User
from ..ml_model.src.predict import make_prediction

screening_bp = Blueprint('screening', __name__)

@screening_bp.route('/api/screening', methods=['POST'])
def submit_screening():
    data = request.json
    user_id = data.get('user_id')
    responses = data.get('responses')

    if not user_id or not responses:
        return jsonify({'error': 'Invalid input'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    prediction = make_prediction(responses)
    
    return jsonify({'user_id': user_id, 'prediction': prediction}), 200

@screening_bp.route('/api/screening/<int:user_id>', methods=['GET'])
def get_screening_results(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Assuming we have a method to retrieve screening results
    results = user.get_screening_results()  
    return jsonify({'user_id': user_id, 'results': results}), 200