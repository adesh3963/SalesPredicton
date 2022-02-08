from file_loader.File_Loader import FileLoader

class Preprocessor:
    """
                    This is Preprocessor class having two methods in it,
                    used to preprocess the data
    """

    def __init__(self,log_object):
        self.log_object= log_object
        self.fileLoder = FileLoader(log_object)

    def lebel_encode(self,data):
        """
                    This function is responsible for label encoding of
                    categorical features.
                    :param data: A pandas DataFrame
                    :return: A pandas DataFrame
                    On Failure: raise error
                    Written by: Adesh Kumar
        """

        self.log_object.info("'label_encode' function of Preprocessor class has been called")

        labels = ["Item_Fat_Content", "Outlet_Size", "Outlet_Location_Type", "Outlet_Type",
                  "Item_Type"]
        try:
            for label in labels:
                encoder = self.fileLoder.load_encoder(label)
                data[label] = encoder.transform(data[label])
                self.log_object.info("label encoding done for %s"%label)

            return data
        except Exception as e:
            self.log_object.info("ERROR occurred while label encoding due to: %s"%str(e))
            raise e

    def scaling(self,data):
        """
                    This function is responsible for scaling the data
                    :param data: A pandas DataFrame
                    :return: numpy object
                    Written by : Adesh Kumar
        """
        self.log_object.info("'scaling' function of Preprocessor class has been called")
        try:
            scaler = self.fileLoder.load_scaler()
            data = scaler.transform(data)
            return data
        except Exception as e:
            self.log_object.erro("ERROR occurred while scaling due to :%s"%str(e))
            raise e
