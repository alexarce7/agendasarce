create database agendas;

use agendas;



create table contactos(
    
id int not null AUTO_INCREMENT PRIMARY KEY, 
    
nombre varchar (50) not null,

telefono varchar(10) not null,    
email varchar(30) not null
    
);



insert into contactos (nombre, telefono, email) values ('alejandro', '7751221098', 'alex@gmail.com');