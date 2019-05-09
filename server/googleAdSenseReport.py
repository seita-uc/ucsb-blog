from flask import Response
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from pytz import timezone
import datetime
import simplejson as json
from oauth2client.file import Storage

SCOPES = ['https://www.googleapis.com/auth/adsense.readonly']
KEY_FILE_LOCATION = './keys/client_secrets.json'
# VIEW_ID = '187987801'

storage = Storage('credentials_file')

def initialize_adsense_reporting():
    flow = flow_from_clientsecrets('keys/client_secrets.json',
                                   SCOPES,
                                   redirect_uri='http://localhost:8080/')

    # auth_uri = flow.step1_get_authorize_url()
    # print(auth_uri)
    code = "4/RQEKcXx6Ku4DFLNsl0Zy_PyBXrk9sg_LsTOiTezCmayBuZVt-mqpKoQlcGbmYVGilu9sOdT73fDOhMhOOpcjGFo"
    # credentials = flow.step2_exchange(code)
    # print(credentials)
    # storage.put(credentials)
    credentials = storage.get()
    adsense = build('adsense', 'v1.4', credentials=credentials)
    return adsense

def get_report(adsense):
    now_pacific = datetime.datetime.now(timezone('US/Pacific'))
    today_pacific = now_pacific.strftime('%Y-%m-%d')
    
    yesterday_pacific = now_pacific - datetime.timedelta(1)
    yesterday_pacific = yesterday_pacific.strftime('%Y-%m-%d')
    
    return adsense.reports().generate(
    startDate = today_pacific, 
    endDate = yesterday_pacific,
    # filter=['AD_CLIENT_ID==' + ad_client_id],
        metric=['PAGE_VIEWS', 'EARNINGS'],
        dimension=['DATE'],
        #sort=['+DATE']
    ).execute()

adsense = initialize_adsense_reporting()
print(adsense)
# report = get_report(adsense)
# print(report)


# def return_analytics_report(response):
    # result = {}
    # resp = Response()
    # for report in response.get('reports', []):
        # columnHeader = report.get('columnHeader', {})
        # dimensionHeaders = columnHeader.get('dimensions', [])
        # metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    # for row in report.get('data', {}).get('rows', []):
        # dimensions = row.get('dimensions', [])
        # dateRangeValues = row.get('metrics', [])
        # for header, dimension in zip(dimensionHeaders, dimensions):
            # # print(header + ': ' + dimension)
            # for i, values in enumerate(dateRangeValues):
                # for metricHeader, value in zip(metricHeaders, values.get('values')):
                    # # print(metricHeader.get('name') + ': ' + value)
                    # if dimension == '(not set)':
                        # dimension = 'Other'
                    # result.update({ dimension: value })
    # resp.status_code = 500
    # resp.set_data(json.dumps(result))
    # return resp
