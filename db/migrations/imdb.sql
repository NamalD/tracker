create table imdb (
  id int generated always as identity,
  name varchar not null,
  url varchar not null,
  score numeric(3, 1) not null
);
