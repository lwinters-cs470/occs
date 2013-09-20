-- drop table if exists entries;
CREATE TABLE IF NOT EXISTS entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null,
  author string
);

-- drop table
CREATE TABLE IF NOT EXISTS studio (
  name string PRIMARY KEY,
  address string
  );

CREATE TABLE IF NOT EXISTS movies (
title string PRIMARY KEY,
year integer,
genre string,
director string
);

INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("The Hangover", 2009, "comedy", "Todd Phillips"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Crazy Stupid Love", 2011, "comedy", "Glenn Ficarra"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Friends with Benefits", 2011, "comedy", "Will Gluck"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Role Models", 2008, "comedy", "David Wain"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Due Date", 2010, "comedy", "Todd Phillips"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Horrible Bosses", 2011, "comedy", "Seth Gordon"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Ted", 2012, "comedy", "Seth MacFarlane"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("Bridesmaids", 2011, "comedy", "Paul Feig"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("The Proposal", 2009, "comedy", "Anne Fletcher"); 
INSERT OR IGNORE INTO movies(title, year, genre, director) VALUES("The Switch", 2010, "comedy", "Josh Gordon"); 


-- drop table if exists users;
CREATE TABLE IF NOT EXISTS users (
  username string not null primary key,
  password string not null
);

INSERT OR IGNORE INTO users(username, password) VALUES("admin", "default");
INSERT OR IGNORE INTO users(username, password) VALUES("pperaza", "pedro");
INSERT OR IGNORE INTO users(username, password) VALUES("cs350", "database");
