import xml.etree.ElementTree as et
import datetime as dt

# double backslash separated input file location/directory
FILE_LOCATION = '\\abc\\xyz\\'
INPUT_FILENAME = 'test_payload1'

def update_depart_return_dates(X, Y):
    today = dt.date.today() # current date
    
    # handle various exception/error cases like invalid xml format, inaccessible/unavailable file for writing/reading
    try:
        payload_tree = et.parse(FILE_LOCATION + INPUT_FILENAME + '.xml')
        payload_tree_root = payload_tree.getroot()

        for depart_date in payload_tree_root.findall("./REQUEST/TP/DEPART"):
            updated_depart_date = today + dt.timedelta(days=X)
            depart_date.text = updated_depart_date.strftime("%Y%m%d") # save depart date in required format

        for return_date in payload_tree_root.findall("./REQUEST/TP/RETURN"):
            updated_return_date = today + dt.timedelta(days=Y)
            return_date.text = updated_return_date.strftime("%Y%m%d") # save return date in required format

        payload_tree.write(FILE_LOCATION + INPUT_FILENAME + '_output.xml') # save the updated xml object in new output xml file
    except Exception as e:
        print(e)
        

update_depart_return_dates(11, 21)
