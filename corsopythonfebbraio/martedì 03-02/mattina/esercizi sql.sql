select * from film
order by length DESC
LIMIT 10;

select title from film
where title like "WORST%";

select * from film;
select film_id, title from film;

select title from film
where title like "%aby%";

select * from film
where length>120 AND rental_rate<10;

select * from film
where length>180 OR length<60;

select * from film
where length between 60 and 90;

select * from film
where rating IN ("G","R");

select distinct rental_rate from film;

select count(*) from film;

select rating, count(*) as total_film
from film group by rating;

select * from payment;

select customer_id, SUM(amount) as totale_speso
from payment
group by customer_id;

/*Estrai i nomi (first_name) e i cognomi (last_name) di tutti gli attori presenti nella tabella actor. Rinomina le colonne come "Nome" e "Cognome" per rendere il report più leggibile.*/
select first_name as nome, last_name as cognome from actor;

/*Trova tutti i titoli dei film che hanno un rating uguale a 'G' (General Audiences).*/
select title,rating from film where rating="G";

/*Trova tutti i clienti nella tabella customer il cui nome inizia con la lettera "A" e il cognome finisce con la lettera "S".*/
select * from customer
where first_name like "A%" and last_name like "%S";

-- Seleziona i film che hanno una durata (length) superiore a 150 minuti E un costo di noleggio (rental_rate) inferiore a 1.00$.--
select * from film
where length>150 and rental_rate<1.00;

-- Mostra i 10 film più lunghi presenti nel database, ordinandoli dal più lungo al più corto.--
select * from film
order by length DESC
limit 10;

-- Qual è il prezzo medio di noleggio (rental_rate) di tutti i film? Rinomina il risultato come "Prezzo_Medio_Noleggio".--
select AVG(rental_rate) AS prezzo_medio_noleggio from film;

-- Nella tabella film, conta quanti film ci sono per ogni durata di noleggio (rental_duration).--
select rental_duration, count(*) from film group by rental_duration;


-- Vai nella tabella payment e conta quanti pagamenti ha registrato ogni staff_id.
select staff_id, count(*) from payment group by staff_id;

/* Per ogni customer_id nella tabella payment, mostra il pagamento più alto (MAX) e quello più basso (MIN) che abbiano mai effettuato*/
select customer_id, MAX(amount), MIN(amount) from payment group by customer_id;



