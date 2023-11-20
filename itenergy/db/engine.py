import os

import sqlalchemy as sa


def get_db_url() -> str:
    return 'postgresql://%s:%s@%s:%s/%s' % (
        os.getenv('POSTGRES_USER', 'itenergy'),
        os.getenv('POSTGRES_PASSWORD', 'password'),
        os.getenv('PGHOST', 'itenergy-service-postgres'),
        os.getenv('PGPORT', '5432'),
        os.getenv('POSTGRES_DB', 'itenergy'),
    )


engine = sa.create_engine(get_db_url())

metadata = sa.MetaData()
