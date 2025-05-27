CREATE TABLE IF NOT EXISTS Cats
(
    cat_id INTEGER PRIMARY KEY autoincrement,
name   TEXT NOT NULL,
weight INT CHECK (weight > 0)
);

insert into Cats(name, weight)
values ('Tuzik', 15),
('Zevs', 23),
('Mars', 10),
('Busya', 13),
('Dusya', 19);

SELECT *
From Cats
where weight between 10 and 15