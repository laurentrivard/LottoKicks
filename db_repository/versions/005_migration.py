from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=64)),
    Column('lastname', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=256)),
    Column('address_street', String(length=256)),
    Column('address_city', String(length=128)),
    Column('address_state', String(length=64)),
    Column('address_country', String(length=128)),
    Column('address_zipcode', String(length=20)),
    Column('total_tickets', Integer),
    Column('shoe_size', Integer),
    Column('role', SmallInteger, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['shoe_size'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['shoe_size'].drop()
