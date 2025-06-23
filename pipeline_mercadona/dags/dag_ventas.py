CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(255) NOT NULL,
    unidades INT NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT fk_producto FOREIGN KEY (producto) REFERENCES inventario(producto));
GO