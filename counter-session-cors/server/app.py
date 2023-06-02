from flask import Flask, make_response, request, session
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'supersecret'


CORS(app, supports_credentials=True, origins=["http://localhost:3000"])


@app.route('/count')
def count():
    print(f"request cookies {request.cookies}")
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1

    counter_dict = {
        "value": session['count']
    }

    response = make_response(
        counter_dict,
        200
    )

    return response


if __name__ == '__main__':
    app.run(port=5555)
