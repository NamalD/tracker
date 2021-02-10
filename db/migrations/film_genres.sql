create table film_genres (
  id int primary key generated always as identity,
  film_id int not null,
  genre_id int not null
);
