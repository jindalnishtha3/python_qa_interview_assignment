import json

# double backslash separated input file location/directory
FILE_LOCATION = '\\abc\\xyz\\'
INPUT_FILENAME = 'test_payload'

def delete_element(elem_name):
    
    # handle various exception/error cases like invalid json format, inaccessible/unavailable file for writing/reading
    # if the structure or schema of the provided json is different than the expectation
    try:
        with open(FILE_LOCATION + INPUT_FILENAME + '.json', 'r+') as input_file:
            data = json.load(input_file)

            # iterating over the outParams list to check if the property to be deleted is present in it
            for i, outParam in enumerate(data['outParams']):
                if outParam == elem_name:
                    del data['outParams'][i]

            # iterating over the inParams dict to check if the property to be deleted is present in it
            for key, value in list(data['inParams'].items()):
                if key == elem_name:
                    del data['inParams'][key]

            # check if the property to be deleted is one of the root elements
            if elem_name in data:
                del data[elem_name]

            with open(FILE_LOCATION + INPUT_FILENAME + '_output.json', 'w') as output_file:
                json.dump(data, output_file)
    except Exception as e:
        print(e)

delete_element('appdate') # I have passed appdate just as an example argument
