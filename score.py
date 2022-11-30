import dataclasses
import collections
from operator import itemgetter
import databases
from quart import Quart, g, request, jsonify, abort
from quart_schema import validate_request, RequestSchemaValidationError, QuartSchema
import redis


app = Quart(__name__)
QuartSchema(app)

@dataclasses.dataclass
class scoreData:
    gameId: str
    guesses: int
    win: bool


@app.errorhandler(401)
def unauthorized(e):
    return {"error": str(e).split(':', 1)[1][1:]}, 401, {"WWW-Authenticate": "Basic realm"}

@app.errorhandler(404)
def unauthorized(e):
    return {"error": str(e).split(':', 1)[1][1:]}, 404

#------------POSTING NEW SCORE-----------------#

@app.route("/add-score", methods=["POST"])
@validate_request(scoreData)
async def add_score(data):
    r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='')

    r.set('1', 'Joe')
    r.set('2', 'Mama')
    value = r.get('1')
    print(value)

    return {"work1": "work1"}


#------------RETRIEVE TOP 10 SCORES-----------------#
@app.route("/get-scores", methods=["GET"])
async def get_scores():
    return {"work": "work"}