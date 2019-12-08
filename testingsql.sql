show databases;

create database filmdb;
use filmdb;
show tables;

create table film (
id int NOT NULL auto_increment,
title varchar(250),

director varchar(250),
year YEAR,
PRIMARY KEY(id)
);


insert into film (title, director, year) values ("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004);
insert into film (title, director, year) values ("Amélie", "Jean-Pierre Jeunet", 2001);
insert into film (title, director, year) values ("Requiem for a Dream", "Darren Aronofsky", 2000);

select * from film;

DROP table film;