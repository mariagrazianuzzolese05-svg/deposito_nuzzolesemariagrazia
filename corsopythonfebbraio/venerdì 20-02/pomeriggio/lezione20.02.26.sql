-- create database prova;
-- drop database prova;
#use prova;

/*
create table utente (
id int primary key,
nome varchar(50) NOT NULL
)

create table acquisti(
id int primary key,
tipo varchar(50),
idUtente int,
foreign key(idUtente) 
references utente(id))

create table acquistiCopia
select * from acquisti


use world;
create table city2
select * from city;

create table city3
select * from city;

drop table city3;

truncate table city2;

drop table city2;

create table city2
select * from city;

alter table city2
#add cap int
#drop Population
modify column ID int primary key


not null : no valori vuoti
unique: solo valori univoci
default: valore di dafault se valore vuoto inserito





create table utente (
id int primary key not null auto_increment,
nome varchar(50) default"nessun nome" NOT NULL,
eta int,
check(eta >17)
)

select count(distinct Population) -- *
from city;

select Name, Region,Population
from country
#where Continent != "Asia";
#where Population between 100 and 1000;
#where Region in("Antarctica","Caribbean" )
#where Region like "a%"
where Continent IS NOT NULL and Region in("Antarctica","Caribbean" )

select * 
from country 
order by Region, SurfaceArea DESC

select Continent, count(Code)
from country
# where
group by Continent
order by count(Code) DESC

use prova;

insert into utente(id,nome)
values(1,"Tommaso"),(2,"Teresa")

insert into utente
values(3,"Alfredo"),(4,"Maria")

insert into utente(id)
values(5)

update utente
set nome = "Michela", altra ="altro valore"
where id = 5 and id = 6

delete from utente
where id = 1*/


select Continent, count(Code)
from world.country
# where
group by Continent
order by count(Code) DESC
limit 1
