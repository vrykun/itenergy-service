import os

import sqlalchemy as sa


def get_db_url() -> str:
    return 'postgresql://%s:%s@%s:%s/%s' % (
        os.getenv('POSTGRES_USER', 'itenergy'),
        os.getenv('POSTGRES_PASSWORD', 'password'),
        os.getenv('PGHOST', 'localhost'),
        os.getenv('PGPORT', '5788'),
        os.getenv('POSTGRES_DB', 'itenergy'),
    )


engine = sa.create_engine(get_db_url(), pool_size=500, max_overflow=0, pool_pre_ping=True)

metadata = sa.MetaData()
