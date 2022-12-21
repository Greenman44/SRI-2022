from .cisi_crenfield_parser import parse_docs_CISI_cranfield, parse_query_CISI_cranfield, parse_rel_CISI_cranfield
from .vaswani_parser import parse_docs_vaswani, parse_query_vaswani, parse_rel_vaswani
import os

basePath = os.getcwd() + "\\datasets"

parsers_docs = {
            "cranfield" : parse_docs_CISI_cranfield,
            "cisi" : parse_docs_CISI_cranfield,
            "vaswani" : parse_docs_vaswani
        }
parsers_query = {
            "cranfield" : parse_query_CISI_cranfield,
            "cisi" : parse_query_CISI_cranfield,
            "vaswani" : parse_query_vaswani
        }
parsers_rel = {
            "cranfield" : parse_rel_CISI_cranfield,
            "cisi" : parse_rel_CISI_cranfield,
            "vaswani" : parse_rel_vaswani
        }

def set_parser(file, name = "", docs = False, querys = False, rel = False):
    data_files = [file for file in os.listdir(basePath)]

    if docs:
        if not f"{name}_data.json" in data_files:
            try:
                parsers_docs[name](file, name)
            except:
                raise Exception("Bad file was given")

    if querys:
        if not f"{name}_query.json" in data_files:
            try:
                parsers_query[name](file, name)
            except:
                raise Exception("Bad file was given")

    if rel:
        if not f"{name}_rel.json" in data_files:
            try:
                parsers_rel[name](file, name)
            except:
                raise Exception("Bad file was given")