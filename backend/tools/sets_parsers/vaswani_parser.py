import json
from os import getcwd

basePath = getcwd() + "\\datasets\\"
def parse_docs_vaswani(file, name):
    docs = file.read()
    re = []
    token = ""
    text = ""
    tdict = {}
    for line in docs.split():
        if token == "" or token == ":(":
            tdict["id"] = line
            token = ":)"
            text = ""
        elif token == ":)": text = text + " " + line
        if line == "/": 
            token = ":("
            tdict["body"] = text
            re.append(tdict)
            tdict = {}
    with open(basePath + "vaswani_data.json","w") as f:
        json.dump(re, f,indent=4)

def parse_query_vaswani(file, name):
    qrys = file.read()
    re = []
    token = ""
    text = ""
    tdict = {}
    for line in qrys.split():
        if token == "" or token == ":(":
            tdict["query number"] = line
            token = ":)"
            text = ""
        elif token == ":)": text = text + " " + line
        if line == "/": 
            token = ":("
            tdict["query"] = text
            re.append(tdict)
            tdict = {}
    with open(basePath + "vaswani_query.json","w") as f:
        json.dump(re, f,indent=4)

def parse_rel_vaswani(file, name):
    rel = file.read()
    reljson = []
    token = ""
    tdict = {}
    qid = -1
    for line in rel.split():
        if token == "" or token == ":(":
            qid = line
            token = ":)"
        elif token == ":)":
            for doc in line.split():
                tdict["query_num"] = qid
                tdict["position"] = 4
                tdict["id"] = doc
                reljson.append(tdict)
                tdict = {}
        if line == "/":
            token = ":("
    with open(basePath + "vaswani_rel.json","w") as f:
        json.dump(reljson, f,indent=4)

