

--creating an identifier field for automatic value substitution
CREATE TABLE kata (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    ext_id TEXT, 
    name TEXT, 
    solution DEFAULT ' '
    );


