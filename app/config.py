import os
user = 'nadeuriADM'
password = 'ghostone1!'
host = os.environ.get('RDS_HOST')
database = 'nadeuri'
port = '3306'

DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
