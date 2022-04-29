import csv
from datetime import datetime
from pytz import timezone
import pytz

date_format = '%Y-%m-%d %H:%M:%S %Z'

# double backslash separated input file location/directory
FILE_LOCATION = '\\abc\\xyz\\'

INPUT_FILENAME = 'Jmeter_log1'

# initializing a dict so that it is easier to access the columns by their name instead of index
label_to_index = {
    "timeStamp": 0,
    "elapsed": 1,
    "label": 2,
    "responseCode": 3,
    "responseMessage": 4,
    "threadName": 5,
    "dataType": 6,
    "success": 7,
    "failureMessage": 8,
    "bytes": 9,
    "sentBytes": 10,
    "grpThreads": 11,
    "allThreads": 12,
    "URL": 13,
    "Latency": 14,
    "IdleTime": 15,
    "Connect": 16
}

def get_non_successful_endpoints():
    # handle various exception/error cases like invalid csv format, inaccessible/unavailable file for reading
    # if the structure or schema of the provided csv is different than the expectation 
    # like if the number of columns is different, order of columns is different or type of columns is different that the expected format
    try:
        with open(FILE_LOCATION + INPUT_FILENAME + '.jtl', 'r') as file:
            reader = csv.reader(file)
            next(reader) # skipping the header row
            for row in reader:
                response_code_idx = label_to_index['responseCode']
                response_code_value = int(row[response_code_idx])

                # 4xx are error http status codes which are normally associated with the client side problems like bad request etc
                # 5xx are error http status codes which are normally associated with the server side problems like internal server error etc
                if response_code_value >= 400 and response_code_value <= 599:

                    # convert the timestamp in milliseconds to seconds
                    timestamp_in_secs = int(row[label_to_index['timeStamp']])/1000.0

                    # convert the timestamp in seconds to human readbale format
                    timestamp_human_readable = datetime.utcfromtimestamp(timestamp_in_secs).strftime(date_format) + ' PST'
                    label_value = row[label_to_index['label']]
                    response_message_value = row[label_to_index['responseMessage']]
                    failure_message_value = row[label_to_index['failureMessage']]
                    print('{},{},{},{},{}'.format(
                        label_value, 
                        str(response_code_value), 
                        response_message_value, 
                        failure_message_value, 
                        timestamp_human_readable))
    except Exception as e:
        print(e)
                
get_non_successful_endpoints()
