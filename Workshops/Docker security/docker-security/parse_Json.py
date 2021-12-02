import json
import csv
import re

# open json file


def readJSONFile(file):
    """
    Reads the json file
    """
    data = None
    with open(file, "r") as json_file:
        # try:
        # print(file)
        try:
            data = json.loads(json_file.read())  # load json file
        except json.decoder.JSONDecodeError as e:
            print(f"Error '{e}'")
        finally:
            if data:
                return data


def fix_description(description):
    """
    Fix the description
    """
    description = re.sub(r'http\S+', '', description) # remove http links
    pattern = "## NVD Description " # remove the NVD description
    pattern2 = "<i> **Note:** </i> <i> Versions mentioned in the description apply to the upstream" # remove the NVD description
    description = description.replace("\n", " ") # replace new line with space
    description = description.replace("\r", " ") # replace new line with space
    description = description.replace("\t", " ") # replace tab with space
    description = description.replace(pattern, "") # replace pattern with nothing
    description = description.replace(pattern2, "") # replace pattern with nothing
    description = description.replace("</i>", "")  # replace </i> with nothing
    description = re.sub("[\(\[].*?[\)\]]", "", description) # remove ( ) and [ ]
    description = description.replace("<i>", "") # replace <i> with nothing

    # remove links in pattern
    pattern = " ## References - ( "
    description = description.replace(pattern, "")

    return description

# parse json content
def parse_json(data):
    json_output = r".\out"
    full_out_file = json_output + "\\" + 'issues.csv'
    i = 0
    issues_found = list()
    vulnerabilities = {"CVE-ID":[], "DESCRIPTION":[], "SEVERITY":[]}
    description = ""

    with open(full_out_file, 'w', newline='', encoding='UTF8') as csvfile:
        fieldnames = ['CVE-ID', 'DESCRIPTION', 'SEVERITY']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        if i == 0:
            writer.writeheader()

        for item in data["vulnerabilities"]:
            try:
                vulnerabilities["CVE-ID"] = item['identifiers']['CVE']
                description = item['description']

                # fix this
                description = fix_description(description)
                vulnerabilities["DESCRIPTION"] = description
                vulnerabilities["SEVERITY"] = item['severity']

                #print(vulnerabilities)
                # list_to_csv(vulnerabilities)
                writer.writerow(vulnerabilities)
                vulnerabilities = {"CVE-ID": [], "DESCRIPTION": [], "SEVERITY": []}
            except KeyError as e:
                print(f"Error '{e}' parse_json")
            finally:
                if issues_found:
                    return issues_found
        i+=1


def main():
    file_name = "scan.results.json"
    data = readJSONFile(file_name)
    vulnerabilities = parse_json(data)
    

if __name__ == "__main__":
    main()