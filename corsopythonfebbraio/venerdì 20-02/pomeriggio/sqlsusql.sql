/*Scrivete una query SQL che restituisca solo i record dalla tabella "products"con un prezzo superiore a 50*/
#use classicmodels

#select * from products
#where buyPrice >50;

/*Scrivete una query SQL che elimini tutti gli ordini nella tabella "orders" con lo stato "Cancelled".*/
#delete from orders
#where status is null

#select * from orders
#where status ='Cancelled';

#create table orderdetails2
#select * from orderdetails;

#delete from orderdetails
#where orderNumber in (select orderNumber from orders where status = 'Cancelled')
#una volta che tolgli e stai sicuro togli da coso originale

delete from orderdetails
where orderNumber IN (
select orderNumber from orders where status = "Cancelled"
);

#eliminazione della tabella dove ce la chiave primaria
delete from orders
where status = "Cancelled";

