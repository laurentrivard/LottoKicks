from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
kicks = Table('kicks', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('picture', String(length=128)),
    Column('picture2', String(length=128)),
    Column('picture3', String(length=128)),
    Column('picture4', String(length=128)),
    Column('shoe_name', String(length=64)),
    Column('shoe_size', String(length=5)),
    Column('shoe_condition', String(length=64)),
    Column('date_added', DateTime),
    Column('contest_start', DateTime),
    Column('contest_end', DateTime),
    Column('winner_id', Integer),
    Column('text', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['kicks'].columns['picture2'].create()
    post_meta.tables['kicks'].columns['picture3'].create()
    post_meta.tables['kicks'].columns['picture4'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['kicks'].columns['picture2'].drop()
    post_meta.tables['kicks'].columns['picture3'].drop()
    post_meta.tables['kicks'].columns['picture4'].drop()
