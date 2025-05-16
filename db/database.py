from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# conectio string
# representa la base de datos que se use
# y el lenjuage de programación
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3315/lookation1'

#crear el objeto de conexión
conn = create_engine(SQLALCHEMY_DATABASE_URL)

# la base para los modelos
Base = declarative_base()

