import json
from os import getcwd

basePath = getcwd() + "\\datasets\\"
def parse_docs_CISI_cranfield(file, name):
    lines = file.read()
    docs = []
    token = ":)"
    text  = ""
    tdict = {}
    id = "1"
    try:
        for line in lines.split():
            if token != "" and token == ".I" and len(tdict) > 0:
                id = line
                docs.append(tdict)
                tdict = {}
                token = ""
                text = ""
            token = line

            if token == ".T":
                    tdict["id"]= id
                    text = ""
            elif token == ".A":
                    tdict["tittle"]= text
                    text = ""
            elif token == ".W":
                    tdict["author"]= text
                    text = ""
            elif token == ".X":
                    tdict["body"] = text
                    text = ""
            else:
                    text += line + " "
            with open(basePath + f"{name}_data.json","w") as f:
                json.dump(docs, f,indent=4)
    except:
        raise Exception("Bad file was given")

def parse_query_CISI_cranfield(file, name):
    lines = file.read()
    qrys = []
    try:
        for doc in lines.split(".I"):
            token = ""
            text    = ""
            tdict = {}
            for line in doc.split():
                token = line
                if token == ".W":
                    tdict["query number"]= text
                    text = ""
                else:
                    text += line + " "
            if text != "":
                tdict["query"] = text
                qrys.append(tdict)
            token = ""
            text = ""
        with open(basePath + f"{name}_query.json", "w") as f:
            json.dump(qrys, f,indent=4)
    except:
        raise Exception("Bad file was given")

def parse_rel_CISI_cranfield(file, name):
    rel = []
    lines = file.read()
    try:
        for line in lines.split("\n"):
            doc = line.split()
            if doc != []:
                tdict = {}
                tdict["query_num"] = doc[0]
                tdict["position"] = 4
                tdict["id"] = doc[1]
                rel.append(tdict)
        with open(basePath + f"{name}_rel.json", "w") as f:
            json.dump(rel, f,indent=4) 
    except:
        raise Exception("Bad file was given")
    