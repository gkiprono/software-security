import json
import os
import bandit
from pathlib import Path

def parseFILES(path):
    """
    Parses the files in the given path
    """
    files = []
    for file in os.listdir(path):
        if file.endswith(".py"):
            files.append(file)
    return files


# apply bandit to files given in the paramaeter
def applyBanditToFiles(py_paths, path):
    """
    Applies bandit to all files in the given path
    """
    full_path = Path(py_paths)
    os.chdir(full_path)
    for file in os.listdir(py_paths):
        if file.endswith(".py"):
            # save the output of bandit to a json file in the given path
            out_file = file + ".json"
            print(out_file)
            print(file)

            os.system("bandit -f json " + file + " > " + out_file)
            
        
# read json files in the given path
def readJSON(path):
    """
    Reads the json files in the given path
    """
    files = []
    for file in os.listdir(path):
        if file.endswith(".json"):
            files.append(path + "\\" + file)
    return files

#read the json file and return the contents
def readJSONFile(file):
    """
    Reads the json file
    """
    data = None
    with open(file, "r") as json_file:
        # try:
        print(file)
        try:
            data = json.loads(json_file.read()) # load json file
        except json.decoder.JSONDecodeError as e:
            print(f"Error '{e}'")
        finally:
            if data:
                return data

def appendToJSON(issues_found, full_out_file):
    """
    Appends the issues to the json file
    """
    with open(full_out_file, 'r+') as outfile:
        data = json.load(outfile)
        data.append(issues_found)
        outfile.seek(0)
        json.dump(data, outfile, indent=4, sort_keys=False,ensure_ascii=False)  

        

def processJSON(file, data):
    """
    Processes the json file
    """
    json_output = r".\out"
    full_out_file = json_output + "\\" + 'issues.json'

    result_toKeep = {"FILENAME":[], "ALERTS":{"CONFIDENCE":[], "SEVERITY":[], "NAME":[], "LINE_NO":[]}}
    issues_found = []
    # print(data['metrics'])
    # print(data['metrics'])
    # check if results are empty
    i=0
    for result in data['results']:
    
        if result['issue_confidence'] != 'LOW' or result['issue_severity'] != 'LOW':
            try:
                print("results: " , len(data['results']))
                #change filename to the file name in the json file
                result_toKeep["FILENAME"] = file
                result_toKeep["ALERTS"]["CONFIDENCE"]= result['issue_confidence']
                result_toKeep["ALERTS"]["SEVERITY"]= result['issue_severity']
                result_toKeep["ALERTS"]["NAME"]= result['issue_text']
                result_toKeep["ALERTS"]["LINE_NO"]= result['line_number']

                appendToJSON(result_toKeep, full_out_file)
                
                result_toKeep = {"FILENAME":[], "ALERTS":{"CONFIDENCE":[], "SEVERITY":[], "NAME":[], "LINE_NO":[]}}
                
            except Exception as e:
                print(e)
                print()
            print()
            i+=1
            # add to the list of issues
    # check if issues are empty
    if len(issues_found) != 0:
        return issues_found
                
            


def main():
    """
    Main function
    """
    issues_found = []
    path = r".\ML-CODE"
    files = parseFILES(path)
    
    file = "prac.py"
    out_file = "out_file.json"

    # applyBanditToFiles(path, json_output)
    # os.chdir(os.getcwd())

    #read json in path
    json_files = readJSON(path)
    
    for file in json_files:
        data = readJSONFile(file)
        ret_val = processJSON(file, data)
        # if ret_val:
        #     issues_found.append(ret_val)

    # print(issues_found)
    # print(len(issues_found))
   # convert list to json

    #issue to json
    # with open() as outfile:
    #     json.dump(issues_found, outfile, indent=4, sort_keys=False,ensure_ascii=False)
        


if __name__ == "__main__":
    main()
