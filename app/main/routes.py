from flask import render_template
from app.main import bp
from flask import jsonify, request, abort

from app.main.functions import check_word


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    most_likely_word = "Hello"
    return render_template("index.html", display_likely_word=most_likely_word)


@bp.route("/api/process_words", methods=["POST"])
def process_words():
    data = request.get_json() or {}
    word_list = data["words"]
    # if not check_word(word_list[-1]):
    #     return jsonify({"error": "Not a word"}), 400

    response = jsonify(word_list)
    response.status_code = 201
    return response
