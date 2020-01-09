from flask import Blueprint
from panorays.util.metadata import metadata

page = Blueprint('page',__name__, template_folder='templates')

@page.route('/')
def index():
    """
    
    :return: Flask response
    """
    return 'Welcome to Panorays'

@page.route('/title', methods=['GET'])
def getMetaData():
    baseUrl = metadata('https://www.panorays.com')
    return {
        "message": baseUrl.getTitle(),
        "status": 200
    }

@page.route('/landingpage', methods=['GET'])
def getLandingPage():
    baseUrl = metadata('https://www.panorays.com')
    return {
        "message": baseUrl.getLandingPage(),
        "status": 200
    }

@page.route('/googleanalyticsid', methods=['GET'])
def getGoogleAnalyticsId():
    baseUrl = metadata('https://www.panorays.com')
    return {
        "message": baseUrl.getGoogleAnalyticsId(),
        "status": 200
    }
