#Carga los datos del archivo inventario.csv a la tabla inventario.
CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(255) NOT NULL,
    cantidad INT NOT NULL,
    almacen VARCHAR(255) NOT NULL,
    CONSTRAINT unique_producto UNIQUE (producto));
GO