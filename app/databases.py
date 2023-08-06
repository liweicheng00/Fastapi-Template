from sqlalchemy.orm import sessionmaker

from app.config import settings
from sqlalchemy import create_engine

# PostgreDB
engine = create_engine(
    f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_URL}/{settings.POSTGRES_DB}"
)
Session = sessionmaker(bind=engine)
session = Session()
# import pymongo
# connection = pymongo.MongoClient(settings.mongodb_host,
#                                  username=settings.mongodb_user,
#                                  password=settings.mongodb_password,
#                                  tls=True,
#                                  tlsAllowInvalidCertificates=True,
#                                  tlsCAFile=settings.mongodb_ca_cert,
#                                  retryWrites=False)
# db = connection[settings.mongodb_db]
