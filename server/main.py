from flask import Flask, Response
import simplejson as json
from googleAnalyticsReport import return_analytics_report
from googleAdSenseReport import return_adsense_report

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/googleAnalyticsReport', methods=['GET'])
    def googleAnalyticsReport():
        return return_analytics_report()

    @app.route('/googleAdSenseReport', methods=['GET'])
    def googleAdSenseReport():
        return return_adsense_report()

    app.run('127.0.0.1', 8000, debug=True)
