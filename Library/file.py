import json

class ReadJson:
    """class to read loctors from json"""

    def read_locators(self,filelocation):
        """loading the data from  json file"""
        with open(filelocation) as file:
            json_obj = json.load(file)
            dict_={}
            for key, value in json_obj.items():
                dict_[key] = (value['loctype'], value['locvalue'])
        return dict_

    # def read_test_data(self,file):
    #     with open(file)as fileobj3:
    #         j_obj=json.load(fileobj3)
    #         list_=[ (value['product'], value['specified_product']) for key,value in j_obj.items()]
    #     return list_
