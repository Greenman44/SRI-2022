def parse_docs():
    import json
    docs = open("doc-text").read()
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
    with open("data.json","w") as f:
        json.dump(re, f,indent=4)
def parse_qrys():
    import json
    qrys = open("query-text").read()
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
    with open("data.json","w") as f:
        json.dump(re, f,indent=4)

def parse_rel():
    import json
    rel = open("rlv-ass").read()
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
    with open("data.json","w") as f:
        json.dump(reljson, f,indent=4)

