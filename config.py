import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGO_URL= os.getenv('MONGODB_URI')
    DATABASE_NAME= os.getenv('DATABASE_NAME')
    OPEN_AI_KEY= os.getenv('OPENAI_API_KEY')



