CREATE DATABASE tvshows;

CREATE USER tvshows_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE tvshows TO tvshows_admin;