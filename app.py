from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def post_data():
    input_data = request.form.get('input')
    # Code for processing the input data
    result = {"success": True, "data": input_data}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
 
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return jsonify({'message': 'Hello, world!'})

# if __name__ == '__main__':
#     app.run()
