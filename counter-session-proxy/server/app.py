from flask import Flask, make_response, request, session

app = Flask(__name__)
app.secret_key = 'supersecret'


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
    response.set_cookie('mouse', 'mickey')

    return response


if __name__ == '__main__':
    app.run(port=5555)
