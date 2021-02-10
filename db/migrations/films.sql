create table films (
  id int primary key generated always as identity,
  name varchar not null,
  movie_db_id int null,
  director varchar null,
  image_path varchar null,
  released date null,
  added date not null,
  watched date null,
  imdb_id varchar null,
  rotten_tomatoes_id int null
);
