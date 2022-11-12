
class Models:
    def __init__(self,dictOfDoc:list[dict],query:list[str]):
        self.dictOfDoc=dictOfDoc
        self.query=query

    def RankingFunc(self):
        pass

class BooleanModel(Models):
    def __init__(self,dictOfDoc:list[dict], query : list[str]):
        super(Models, self).__init__(dictOfDoc, query)
    
    def RankingFunc(self):
        #TODO: Implementation of the selection of Documents
        pass

class VectorialModel(Models):
    def __init__(self, dictOfDoc : list[dict], query: list[str]):
        super(Models, self).__init__(dictOfDoc, query)

    def RankingFunc(self):
        #TODO: Implementation of the search of Documents
        pass

class BooleanExtendedModel(Models):
    def __init__(self,dictOfDoc:list[dict] , query : list[str]):
        super(Models, self).__init__(dictOfDoc, query)
        
    def RankingFunc(self):
        #TODO: Implementation of the search of Documents
        pass



