import csv
from datetime import datetime, timedelta
from apiclient import sample_tools
from apiclient.discovery import build
from oauth2client import client
 
todaydate = datetime.today().strftime('%Y-%m-%d')
 
def main():   
    scope = ['https://www.googleapis.com/auth/adsense.readonly']
    client_secrets_file = './keys/client_secrets.json'
     
    service, flags = sample_tools.init('', 'adsense', 'v1.4', __doc__, client_secrets_file, parents=[], scope=scope)
     
    ## Get accounts
    accounts = service.accounts().list().execute()
      
    try:
        ## Get account(s) data
        results = service.accounts().reports().generate(
            accountId='pub-6760815152083080',
            startDate='2019-05-01', # choose your own start date
            endDate= todaydate,
            metric=['EARNINGS', 'CLICKS','AD_REQUESTS'],
            dimension=['DOMAIN_NAME','DATE','AD_FORMAT_NAME']).execute()
     
    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')
            
    ## output results into csv
    header = ['hostname','date','type','earnings','clicks','ad_requests']
     
    with open('output_adsense.csv', 'wb') as file:
        file.write(','.join(header) + '\n')       
        for row in results.get('rows'):
            file.write(','.join(row) + '\n')
 
    ## print status for log
    print(str(datetime.now()) + ' adsense')
     
if __name__ == '__main__':
    main()
