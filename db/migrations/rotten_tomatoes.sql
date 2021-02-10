create table rotten_tomatoes (
  id int primary key generated always as identity,
  name varchar not null,
  url varchar not null,
  score int not null
);
