import os

# noinspection PyUnresolvedReferences
import sqlalchemy.orm

import pypi_org
from data import db_session
from data.package import Package
from data.releases import Release


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()

    p.summary = input('Package summary: ').strip()
    p.author_name = input('Author: ').strip()
    p.license = input('License: ').strip()

    print("Release 1:")
    # noinspection DuplicatedCode
    r = Release()
    r.major_ver = int(input('Major version: '))
    r.minor_ver = int(input('Minor version: '))
    r.build_ver = int(input('Build version: '))
    r.size = int(input('Size in bytes: '))
    p.releases.append(r)

    print("Release 2:")
    # noinspection DuplicatedCode
    r = Release()
    r.major_ver = int(input('Major version: '))
    r.minor_ver = int(input('Minor version: '))
    r.build_ver = int(input('Build version: '))
    r.size = int(input('Size in bytes: '))
    p.releases.append(r)

    session = db_session.create_session()
    session.add(p)
    session.commit()


def main():
    init_db()
    while True:
        insert_a_package()


if __name__ == '__main__':
    main()
