# -*- coding: utf-8 -*-
from . import f1
from . import l1
from . import long_comment

import os
from pathlib import Path


DOLLAR_SIGN = '$'
ORIGIN_PATH = Path().resolve()
OS_SEP = os.path.sep # platform-specific path separator (for linux `/`, for windows `\`)


def generate_ini(project_name):
    """ `alembic.ini` file inside base project directory """
    sqlalchemy_db_url = 'sqlite:///'+str(ORIGIN_PATH)+OS_SEP+project_name+OS_SEP+'default.db'
    return f"""# A generic, single database configuration.

[alembic]
# path to migration scripts
script_location = migrations

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python-dateutil library that can be
# installed by adding `alembic[tz]` to the pip requirements
# string value is passed to dateutil.tz.gettz()
# leave blank for localtime
# timezone =

# max length of characters to apply to the
# "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to migrations/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "version_path_separator" below.
# version_locations = %(here)s/bar:%(here)s/bat:migrations/versions

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses os.pathsep.
# If this key is omitted entirely, it falls back to the legacy behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
version_path_separator = os  # Use os.pathsep. Default configuration used for new projects.

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = {sqlalchemy_db_url}


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
"""


def generate_env():
    """ `env.py` file inside migrations """
    return f"""from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

from flask_unity.contrib import db
# from <app_name>.models import <app_model>
target_metadata = db.Model.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    {long_comment}Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    {long_comment}
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={f1}"paramstyle": "named"{l1},
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    {long_comment}Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    {long_comment}
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {f1}{l1}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata, render_as_batch=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
"""


def generate_script_py_mako():
    """ `script.py.mako` file inside migrations """
    return f"""{long_comment}{DOLLAR_SIGN}{f1}message{l1}

Revision ID: {DOLLAR_SIGN}{f1}up_revision{l1}
Revises: {DOLLAR_SIGN}{f1}down_revision | comma,n{l1}
Create Date: {DOLLAR_SIGN}{f1}create_date{l1}

{long_comment}
from alembic import op
import sqlalchemy as sa
{DOLLAR_SIGN}{f1}imports if imports else ""{l1}

# revision identifiers, used by Alembic.
revision = {DOLLAR_SIGN}{f1}repr(up_revision){l1}
down_revision = {DOLLAR_SIGN}{f1}repr(down_revision){l1}
branch_labels = {DOLLAR_SIGN}{f1}repr(branch_labels){l1}
depends_on = {DOLLAR_SIGN}{f1}repr(depends_on){l1}


def upgrade() -> None:
    {DOLLAR_SIGN}{f1}upgrades if upgrades else "pass"{l1}


def downgrade() -> None:
    {DOLLAR_SIGN}{f1}downgrades if downgrades else "pass"{l1}
"""


def generate_readme():
    """ `README` file inside migrations """
    return f"""Generic single-database configuration."""
