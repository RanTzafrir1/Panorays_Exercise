from flask import url_for


class TestPage(object):
    def test_title_page(self, client):
        """ Title page should respond with a success 200. """
        response = client.get(url_for('page.getMetaData'))
        assert response.status_code == 200

    def test_landingpage_page(self, client):
        """ Landingpage page should respond with a success 200. """
        response = client.get(url_for('page.getLandingPage'))
        assert response.status_code == 200

    def test_googleanalyticsid_page(self, client):
        """ Google Analytics Id page should respond with a success 200. """
        response = client.get(url_for('page.getGoogleAnalyticsId'))
        assert response.status_code == 200
