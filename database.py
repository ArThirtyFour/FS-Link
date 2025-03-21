import random
import string
from sqlalchemy import create_engine, Column, Integer, String , MetaData, Table

engine = create_engine('sqlite:///urls.db')
metadata = MetaData()
urls_code = Table('urls_code', metadata,
                  Column('urls', String),
                  Column('code', String,unique=True),
                  )
metadata.create_all(engine)
conn = engine.connect()


def random_url() -> str:
    characters = string.ascii_letters + string.digits
    url = ''.join(random.choice(characters) for _ in range(5))
    return url

def add_url(url: str) -> str:
    link = random_url()
    conn.execute(urls_code.insert().values(urls=url, code=link))
    conn.commit()
    return link

def get_url(code: str) -> str:
    url = conn.execute(urls_code.select().where(urls_code.c.code == code)).fetchone()
    print(url[0])
    return url[0] if url else None