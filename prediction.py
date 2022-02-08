from file_loader.File_Loader import FileLoader
from preprocessing.preprocessing import Preprocessor
# from data_collecting.collect_data import CollectData
# import pandas as pd
# import numpy as np
class Prediction:
    """
                    This is Prediction class, having predict function in it that will be used for
                    preprocessing and prediction.
                    Written By : Adesh Kumar
    """
    def __init__(self,log_object):
        self.log = log_object
        self.fileLoder = FileLoader(log_object)
        # self.collect_data= CollectData()
        self.preprocessor = Preprocessor(log_object)

    def predict(self,data):
        """
                    This is predict function of Prediction class
                    :param data: A pandas DataFrame
                    :return: An nd-array
                    Written by: Adesh Kumar
        """

        try:
            self.log.info("this is 'predict' funtion of 'Prediction' class..")

            self.log.info(" going for label encoding of data")

            test= self.preprocessor.lebel_encode(data)
            self.log.info(" label encoding of data is Done")

            self.log.info(" going for scaling of data")
            test= self.preprocessor.scaling(test)
            self.log.info(" scaling of data Done")

            self.log.info("Loading Model...")
            model= self.fileLoder.load_model()
            self.log.info(" Model loaded")
            self.log.info("using model for prediction")
            result= model.predict(test)
            self.log.info(" prediction done successfully....!")

            return result[0]



        except Exception as e:
            self.log.info("prediction Faild due to : %s"%str(e))
            raise e


