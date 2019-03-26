drop table if exists customer;
create table customer(
	id integer primary key autoincrement,
	name text not null,
	email text not null
)
