import pandas as pd
from .con import ConnectionDatabase

class InsertData:

    def read_insert(self):

        #define_connectiom
        con_database = ConnectionDatabase.conn_database(self)

        #read_data
        category_db = pd.read_csv("/home/ajied/Project/Bank_BTPN_Syariah/Data/Data_Task_5-ff9872f9-5f5c-4f6d-8579-cc8530951b8a/category_db.csv")

        #read_data
        customer_data_history = pd.read_csv("/home/ajied/Project/Bank_BTPN_Syariah/Data/Data_Task_5-ff9872f9-5f5c-4f6d-8579-cc8530951b8a/customer_data_history.csv")

        #read_data
        education_db = pd.read_csv("/home/ajied/Project/Bank_BTPN_Syariah/Data/Data_Task_5-ff9872f9-5f5c-4f6d-8579-cc8530951b8a/education_db.csv")

        #read_data
        marital_db = pd.read_csv("/home/ajied/Project/Bank_BTPN_Syariah/Data/Data_Task_5-ff9872f9-5f5c-4f6d-8579-cc8530951b8a/marital_db.csv")

        #read_data
        status_db = pd.read_csv("/home/ajied/Project/Bank_BTPN_Syariah/Data/Data_Task_5-ff9872f9-5f5c-4f6d-8579-cc8530951b8a/status_db.csv")


        try :

            category_db.to_sql("Category_db", con_database, if_exists = "replace", index = False)

            customer_data_history.to_sql("Customer_data_history", con_database, if_exists = "replace", index = False)

            education_db.to_sql("Education_db", con_database, if_exists = "replace", index = False)

            marital_db.to_sql("Marital_db", con_database, if_exists = "replace", index = False)

            status_db.to_sql("Status_db", con_database, if_exists = "replace", index = False)

            print("Succes entry Database")
        
        except :

            print("Cannot ELT Data")