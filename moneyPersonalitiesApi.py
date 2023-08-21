from flask import Flask, request, Response
from moneyPersonalitiesCode import money_personality

app = Flask(__name__)


@app.route('/my-money-personality/<given_responses>', methods=['GET'])
def processing_money_personality(given_responses):
    if request.method == 'GET':
        if len(given_responses) < 13:
            return Response('Responses are incomplete!', 400)
        else:
            return money_personality(given_responses)



if __name__ == "__main__":
    app.run(debug=True)
