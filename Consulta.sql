CREATE DATABASE IF NOT EXISTS ControlAcceso;
USE ControlAcceso;


CREATE TABLE IF NOT EXISTS Computador (
    id_computador INT AUTO_INCREMENT PRIMARY KEY,   -- Identificador único del computador
    IP VARCHAR(45) NOT NULL,                       -- Dirección IP del computador
    Lugar VARCHAR(255),                            -- Ubicación física del computador
    Estado_paginas BOOLEAN DEFAULT FALSE           -- Indica si el computador tiene páginas bloqueadas
);


CREATE TABLE IF NOT EXISTS Paginas (
    id_pagina INT AUTO_INCREMENT PRIMARY KEY,       -- Identificador único de la página
    URL VARCHAR(2083) NOT NULL,                     -- URL de la página
    Estado BOOLEAN DEFAULT FALSE                    -- Indica si la página está bloqueada
);


CREATE TABLE IF NOT EXISTS Computador_Paginas (
    id_computador INT,
    id_pagina INT,
    PRIMARY KEY (id_computador, id_pagina),
    FOREIGN KEY (id_computador) REFERENCES Computador(id_computador),
    FOREIGN KEY (id_pagina) REFERENCES Paginas(id_pagina)
);

