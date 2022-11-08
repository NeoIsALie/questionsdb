create role dbowner with
createdb
login
password 'temppass';

create database questionsdb
owner dbowner;

create table literature (
    id serial,
    title varchar(256) not null,
    author varchar(256) not null
)

create table questions (
    id bigserial,
    question varchar(256) not null,
    answer varchar(256) not null,
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
)

create table unification (
    id serial,
    job references jobs(id),
    company references companies(id),
    kwyword references keywords(id),
    question references questions(id)
)
