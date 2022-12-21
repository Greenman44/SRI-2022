from .cisi_crenfield_parser import parse_docs_CISI_cranfield, parse_query_CISI_cranfield, parse_rel_CISI_cranfield

def set_parser(file, docs = False, querys = False, rel = False):
    if docs:
        try :
            parse_docs_CISI_cranfield(file)
        except:
            raise Exception("Bad file was given")
    if querys:
        try :
            parse_query_CISI_cranfield(file)
        except:
            raise Exception("Bad file was given")
    if rel:
        try :
            parse_rel_CISI_cranfield(file)
        except:
            raise Exception("Bad file was given")