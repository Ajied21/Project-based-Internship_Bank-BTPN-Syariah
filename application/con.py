from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class ConnectionDatabase:
    

    def conn_database(self):
        
        # load dotenv
        load_dotenv()

        # define env
        URL             = os.environ['url']
        USER            = os.environ['usr']
        PASSWORD        = os.environ['pas']


        engine_one      = create_engine('postgresql://{USER}:{PASSWORD}@{URL}:5432/postgres'.format(
                        USER=USER,
                        PASSWORD=PASSWORD,
                        URL=URL
        ))

        return engine_one
