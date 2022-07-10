from ast import JoinedStr
from flask import render_template
from app.main import bp
from flask import jsonify, request, abort

from app.main.functions import (
    combine_letters,
    check_word,
    wordle_solver,
    combine_results,
    best_word,
    letter_freq,
    reset_state
)


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    reset_state()
    return render_template("index.html")


@bp.route("/api/validate_word", methods=["POST"])
def validate_word():
    word_list = request.get_json() or {}
    print(word_list)
    recent_word = combine_letters(word_list[-1])
    return jsonify(check_word(recent_word))


@bp.route("/api/process_words", methods=["POST"])
def process_words():
    word_list = request.get_json() or {}
    recent_word = combine_letters(word_list[-1])
    if not check_word(recent_word):
        response = jsonify("Not a word")
        response.status_code = 201
        return response
    recent_result = combine_results(word_list[-1])
    suggested_words = wordle_solver(recent_word, recent_result)
    #print(suggested_words)
    if(suggested_words is True):
        response = jsonify("Won")
        return response
    if(not suggested_words):
        response = jsonify("Lost")
        return response
    suggested_word = best_word(suggested_words, letter_freq(suggested_words))
    response = jsonify(suggested_word, suggested_words)
    #print("SUGGESTION:", suggested_word)
    #print(suggested_words)
    #print(response)
    response.status_code = 201
    return response
