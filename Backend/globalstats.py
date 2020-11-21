import os
import json
from TAPParser import TAPLexer

class GlobalStats():

    '''
    "GlobalStats" class is used to store the global results of all the files processed.
    The class is composed by the following atributes:
        - totalFiles: total number of files processed to the moment;
        - totalTests: total number of tests on files processed;
        - totalOkTests: total number of tests with "ok" status;
        - totalNotOktests: total number of tests with "not ok" status;
        - totalOkSubtests: total number of subtests with "ok" status;
        - totalNotOkSubtests: total number of subtests with "not ok" status;
    '''
    def __init__(self):
       
        self.totalFiles = 0
        self.totalTests = 0
        self.totalOkTests = 0 #só dos testes
        self.totalNotOktests = 0 #só dos testes
        self.totalSubtests = 0
        self.totalOkSubtests = 0
        self.totalNotOkSubtests = 0

    def UpdateStats(self, lexObj):
        '''
        This method updates the stats of all files processed.
        '''
        self.totalFiles += 1
        self.totalTests += lexObj.n_tests
        self.totalOkTests += lexObj.n_ok_tests
        self.totalNotOktests += lexObj.n_nok_tests
        self.totalSubtests += lexObj.n_subtests
        self.totalOkSubtests += lexObj.n_ok_subtests
        self.totalNotOkSubtests += lexObj.n_nok_subtests

    
    def LoadFile(self,filePath):
        '''
        This method loads JSON file information to a class instance, making it possible to update the global stats.
        Arguments:
            - filePath: path of the JSON file to be loaded.
        '''
        try:
            with open(filePath, 'r') as f:
                obj_dict = json.loads(f.read())
                self.totalFiles = obj_dict["totalFiles"]
                self.totalTests = obj_dict["totalTests"]
                self.totalOkTests = obj_dict["totalOkTests"]
                self.totalNotOktests = obj_dict["totalNotOkTests"]
                self.totalSubtests = obj_dict["totalSubtests"]
                self.totalOkSubtests = obj_dict["totalOkSubtests"]
                self.totalNotOkSubtests = obj_dict["totalNotOkSubtests"]
        except:
            exit
            

    def SaveToFile(self, filePath):

        '''
        This method saves the updated global stats in a JSON file.
        Arguments:
            - filePath: path of the JSON file to be stored.
        '''
        jsonified_object = self.__dict__
        with open(filePath, 'w') as output:
            json.dump(jsonified_object, output)
        return self