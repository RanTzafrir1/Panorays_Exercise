from flask import Blueprint, request
from panorays.util.metadata import metadata

page = Blueprint('page',__name__, template_folder='templates')

@page.route('/')
def index():
    """

    :return: Flask response
    """
    return 'Welcome to Panorays Exercise'

@page.route('/title', methods=['GET'])
def getMetaData():
    jsonRequest = request.get_json()
    if 'url' in jsonRequest:
        baseUrl = metadata(jsonRequest['url'])
        return {
            "message": baseUrl.getTitle(),
            "status": 200
        }
    else:
        return {
            "message": "request must contain the url attribute",
            "status": 403
        }

@page.route('/landingpage', methods=['GET'])
def getLandingPage():
    jsonRequest = request.get_json()
    if 'url' in jsonRequest:
        baseUrl = metadata(jsonRequest['url'])
        return {
            "message": baseUrl.getLandingPage(),
            "status": 200
        }
    else:
        return {
            "message": "request must contain the url attribute",
            "status": 403
        }

@page.route('/googleanalyticsid', methods=['GET'])
def getGoogleAnalyticsId():
    jsonRequest = request.get_json()
    if 'url' in jsonRequest:
        baseUrl = metadata(jsonRequest['url'])
        return {
            "message": baseUrl.getGoogleAnalyticsId(),
            "status": 200
        }
    else:
        return {
            "message": "request must contain the url attribute",
            "status": 403
        }
