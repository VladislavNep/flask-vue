from flask import jsonify, request
from flask_cors import CORS
from backend.cart import services
from backend.cart import app


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/user/cart', methods=['GET', 'POST'])
def all_product():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        services.add_product(post_data)
    else:
        response_object['products'] = services.PRODUCTS
    return jsonify(response_object)


@app.route('/api/user/cart/product/<path:product_id>', methods=['PUT', 'DELETE'])
def single_product(product_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        services.remove_product(product_id)
        services.add_product(post_data)
    elif request.method == 'DELETE':
        services.remove_product(product_id)
    return jsonify(response_object)


