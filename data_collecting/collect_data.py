import pandas as pd
import numpy as np


class CollectData:

    def __init__(self, log_object):
        self.log_object = log_object

    def collect_data(self, obj):

        """
                    THis is collect_data function of Collect data class,
                    responsible for catching the data form the URL
                    :param obj: A flask request object
                    :return: A pandas DataFrame
                    Written by : Adesh Kumar
        """
        self.log_object.info("'collection_data' function of CollectData class has been called")
        try:
            Item_Weight = float(obj["Item_Weight"])
            Item_Fat_Content = str(obj["Item_Fat_Content"])
            Item_Visibility = float(obj["Item_Visibility"])
            Item_Type = str(obj["Item_Type"])
            Item_MRP = float(obj["Item_MRP"])
            Outlet_Size = str(obj["Outlet_Size"])
            Outlet_Location_Type = str(obj["Outlet_Location_Type"])
            Outlet_Type = str(obj["Outlet_Type"])
            Outlet_Years = 2022 - float(obj["Outlet_Year_Establishment"])

            test_data = [Item_Weight, Item_Fat_Content, Item_Visibility,
                         Item_Type, Item_MRP,
                         Outlet_Size, Outlet_Location_Type, Outlet_Type,
                         Outlet_Years]

            test_data = np.reshape(test_data, (1, -1))

            test = pd.DataFrame(test_data, columns=["Item_Weight", "Item_Fat_Content", "Item_Visibility",
                                                    "Item_Type", "Item_MRP",
                                                    "Outlet_Size", "Outlet_Location_Type", "Outlet_Type",
                                                    "Outlet_Years"])

            return test

        except Exception as e:
            self.log_object.error("Error occured while collecting the data due to %s" % str(e))

            raise e
