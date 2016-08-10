-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

-- Players table
CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL
);

-- Matches table
CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  winner SERIAL REFERENCES players (id),
  loser SERIAL REFERENCES players (id),
  draw BOOLEAN DEFAULT FALSE
);
