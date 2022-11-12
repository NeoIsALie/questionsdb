import sqlalchemy

with sqlalchemy.create_engine(
        'postgresql:///postgres',
        isolation_level='AUTOCOMMIT'
).connect() as connection:
    connection.execute("""create role dbowner with
                          createdb
                          login
                          password 'temppass';"""
                       )
    connection.execute(""" create database questionsdb
                           owner dbowner;"""
                       )
    connection.execute(
        """
        create table literature (
        id serial,
        title varchar(256) not null,
        author varchar(256) not null
    )
    
    create table questions (
        id bigserial,
        question varchar not null,
        answer varchar,
        literature_id references literature(id)
    )
    
    create table jobs (
        id serial,
        title varchar(256) not null,
        definition varchar(256)
    )
    
    create table companies (
        id serial,
        title varchar(256) not null,
        definition varchar(256),
        attitude numeric(1, 1)
    )
    
    create table keywords (
        id serial
        keyword text not null
    )
    
    create table unification (
        id bigserial,
        job references jobs(id),
        company references companies(id),
        keyword references keywords(id),
        question references questions(id)
    )
        """
    )
