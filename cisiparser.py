def parse_docs():
    import json
    lines = open("CISI.ALL").read()
    docs = []
    for doc in lines.split(".I"):
        token = ""
        text    = ""
        tdict = {}
        for line in doc.split():
            token = line
            if token == ".T":
                tdict["id"]= text
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
        docs.append(tdict)
        token = ""
        text = ""
    with open("data.json","w") as f:
        json.dump(docs, f,indent=4)

def parse_query():
    import json
    lines = open("CISI.QRY").read()
    qrys = []
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
    with open("data.json","w") as f:
        json.dump(qrys, f,indent=4)

def parse_rel():
    import json
    rel = []
    lines = open("CISI.REL").read()
    for line in lines.split("\n"):
        doc = line.split()
        if doc != []:
            tdict = {}
            tdict["query_num"] = doc[0]
            tdict["position"] = 4
            tdict["id"] = doc[1]
            rel.append(tdict)
    with open("data.json","w") as f:
        json.dump(rel, f,indent=4) 
parse_rel()

    