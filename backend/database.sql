create table guests_form (
	id integer primary key GENERATED ALWAYS AS IDENTITY,
	name varchar(255) not null,
	present boolean not null default 't',
	marry boolean not null default 't',
	twoday boolean not null default 'f',
	food varchar(255) not null,

	created_at timestamp default (now())
);

grant SELECT, DELETE, UPDATE, INSERT on guests_form to wedding_admin;
