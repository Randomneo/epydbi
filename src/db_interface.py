import logging
from logging.config import fileConfig as logFileConfig

from epc.server import EPCServer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.schema import MetaData

from defaults import (
    localhost,
    config_file,
)


server = EPCServer((localhost, 0))

DBSession = None
Engine = None

logFileConfig(config_file)
logger = logging.getLogger(__name__)


@server.register_function
def init_connection(database_string=None):
    init_engine(database_string)
    init_session()


def init_engine(database_string=None):
    global Engine
    if Engine:
        return None
    try:
        Engine = create_engine(database_string)
    except SQLAlchemyError as e:
        # TODO: log
        print(e)


def init_session():
    global DBSession
    global Engine
    if not Engine:
        print('Engine not initialized')
    try:
        DBSession = sessionmaker(bind=Engine)
    except SQLAlchemyError as e:
        # TODO: log
        print(e)


@server.register_function
def echo():
    return 'aoeaoe12'


@server.register_function
def get_tables():
    meta = MetaData()
    meta.reflect(bind=Engine)
    return sorted(meta.tables)


@server.register_function
def get_columns_by_table(table):
    meta = MetaData()
    meta.reflect(bind=Engine)
    table = meta.tables[table]
    return [(c.name, c.type) for c in table.columns]


if __name__ == '__main__':
    logger.info('test log')
    logger.error('aoe')
