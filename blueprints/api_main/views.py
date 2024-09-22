from flask import Blueprint, jsonify

bp_api_main = Blueprint("api_main", __name__)

@bp_api_main.route("/getHomepageMessage")
def getHomepageMessage():
    return jsonify({"ok": True, "message": "Let's build something awesome!"})
