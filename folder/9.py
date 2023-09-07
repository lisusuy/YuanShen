from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        return render_template_string('<p>You entered: {{ user_input | safe }}</p>', user_input=user_input)
    return '''
        <form method="post">
            <label for="user_input">Enter text:</label>
            <input type="text" name="user_input" id="user_input">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
