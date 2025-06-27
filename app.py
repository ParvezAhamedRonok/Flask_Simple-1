from flask import Flask, render_template, request, session, jsonify, redirect, url_for

app = Flask(__name__)
app.secret_key = 'd93c1a6fdf42b5e4d24f865c6c51a3c4'  # Replace with your own secret key this is Random Secret Key that i made by myself ..


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'count' not in session:
        session['count'] = 0

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'increment':
            session['count'] += 1
        elif action == 'decrement':
            session['count'] -= 1

    return render_template('index.html', count=session['count'])


# ✅ New API Route
@app.route('/api/calculate-hardness', methods=['POST'])
def calculate_hardness():
    data = request.get_json()

    # Validate payload
    if not data or 'field_data' not in data or 'desired_hardness' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    field_data = data['field_data']
    desired_hardness = data['desired_hardness']
    constraints = data.get('constrains', [])

    # Example logic: check if constraints are violated
    constraint_results = []
    for constraint in constraints:
        title = constraint['title']
        min_val = constraint['min']
        max_val = constraint['max']
        actual_value = field_data.get(title)

        if actual_value is None:
            constraint_results.append({title: 'missing'})
        elif actual_value < min_val or actual_value > max_val:
            constraint_results.append({title: 'violation'})
        else:
            constraint_results.append({title: 'ok'})

    # Example output response
    response = {
        "status": "processed",
        "desired_hardness": desired_hardness,
        "field_data_summary": field_data,
        "constraint_results": constraint_results
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
