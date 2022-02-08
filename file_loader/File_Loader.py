import pickle


class FileLoader:
    """
                    This is FileLoder class, have three methods in it, used to load files.
                    written by: Adesh Kumar
    """

    def __init__(self,log_object):
        self.log_object = log_object

    def load_model(self):
        """
                    This method is used to load the model from a directory
                    :return: A Model object
                    On Failure: OS ERROR
                    Written by: Adesh Kumar
        """
        self.log_object.info("Loading Model by using 'load_model' function of FileLoader class")
        try:
            with open("./model_training/model.sav", "rb") as f:
                model = pickle.load(f)

            return model

        except Exception as e:
            self.log_object.error("ERROR occurred while loading the model in 'load_model' function due to : %s"%str(e))
            raise e


    def load_scaler(self):
        """
                    This is load_scaler function of FileLoader class,
                    designed to return standard scaler object
                    :param: None
                    :return: scaler object
                    On Failure: OS ERROR
                    Written by : Adesh Kumar
        """
        self.log_object.info("'load_scaler' function of FileLoder class has been called")
        try:

            with open("./model_training/scaler.sav", "rb") as f:
                scaler = pickle.load(f)

            return scaler
        except Exception as e:
            self.log_object.error("ERROR occurred while loading scaler object in load_scaler Function due to: %s"%str(e))
            raise e

    def load_encoder(self,name):
        """
                    THis is load_encoder funtion of FIleLoader class Used to load
                    label encoder object of given string.
                    :param name: A sting object
                    :return: label encoder object
                    On Failure: OS ERROR
                    Written by :Adesh Kumar
        """

        self.log_object.info("This is 'load_encoder' function of FileLoader class")
        try:
            self.log_object.info("loading label encoder for %s"%name)
            filename = "le_" + name + ".sav"
            encoder = pickle.load(open("./cleaning/Label_encoder/" + filename, "rb"))
            #self.log_object.info("loaded label encoder for %s" % name)
            return encoder

        except Exception as e:
            self.log_object.error("ERROR occured while loding label encoder for %s,deu to %s"%(name,str(e)))
            raise e