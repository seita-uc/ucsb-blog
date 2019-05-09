from flask import Flask, Response
import simplejson as json
from googleAnalyticsReport import return_analytics_report

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/googleAnalyticsReport', methods=['GET'])
    def analyticsReport():
        return return_analytics_report()

    @app.route('/googleAdSenseReport', methods=['GET'])
    def adSenseReport():
        analytics = initialize_analyticsreporting()
        response = get_report(analytics)
        return return_response(response)


    app.run('127.0.0.1', 8000, debug=True)