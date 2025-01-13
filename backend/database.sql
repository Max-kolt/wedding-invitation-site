create table guests_form (
	id integer primary key GENERATED ALWAYS AS IDENTITY,
	fullnames varchar(255) not null,
	is_present boolean not null default 't',
	will_congratulating boolean not null default 'f',
	meat_or_fish varchar(255) not null,

	created_at timestamp default (now())
);

grant SELECT, DELETE, UPDATE, INSERT on guests_form to wedding_admin;
