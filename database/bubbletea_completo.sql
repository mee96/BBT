-- ============================================================
--  BUBBLETEA DATABASE GNAAARLY
--  Inspirado en el menú CoCo BubbleTea
-- ============================================================

DROP DATABASE IF EXISTS bubbletea;
CREATE DATABASE bubbletea CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bubbletea;

-- ------------------------------------------------------------
-- 1. USUARIO
-- ------------------------------------------------------------
CREATE TABLE usuario (
  usuario_id     INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre         VARCHAR(50)  NOT NULL,
  nombre_usuario VARCHAR(30)  UNIQUE NOT NULL,
  email          VARCHAR(50)  UNIQUE NOT NULL,
  contrasena     VARCHAR(20)  NOT NULL,
  pais           VARCHAR(30),
  ciudad         VARCHAR(30),
  direccion      VARCHAR(60),
  telf           INT
);

-- ------------------------------------------------------------
-- 2. PERFIL_USUARIO  (1-a-1 con usuario)
-- ------------------------------------------------------------
CREATE TABLE perfil_usuario (
  usuario_id     INT UNSIGNED PRIMARY KEY,
  nombre_usuario VARCHAR(30)  UNIQUE NOT NULL,
  email          VARCHAR(50)  UNIQUE NOT NULL,
  contrasena     VARCHAR(20)  NOT NULL,
  pais           VARCHAR(30),
  ciudad         VARCHAR(30),
  direccion      VARCHAR(60),
  telf           INT,
  CONSTRAINT fk_perfil_usuario
    FOREIGN KEY (usuario_id) REFERENCES usuario (usuario_id)
    ON UPDATE CASCADE ON DELETE CASCADE
);

-- ------------------------------------------------------------
-- 3. CATEGORIA  (Té con Leche, Frutal, Probiótico, etc.)
-- ------------------------------------------------------------
CREATE TABLE categoria (
  categoria_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(50) NOT NULL,
  nombre_zh    VARCHAR(50)             -- nombre en chino (opcional)
);

-- ------------------------------------------------------------
-- 4. TAMANO  (M, L)
-- ------------------------------------------------------------
CREATE TABLE tamano (
  tamano_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  codigo    VARCHAR(5)  NOT NULL,      -- 'M', 'L'
  nombre    VARCHAR(20) NOT NULL       -- 'Mediano', 'Grande'
);

-- ------------------------------------------------------------
-- 5. TIPO_LECHE  (Regular, Fresca, Soja, Avena)
-- ------------------------------------------------------------
CREATE TABLE tipo_leche (
  tipo_leche_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre        VARCHAR(40)  NOT NULL,
  precio_extra  DECIMAL(4,2) NOT NULL DEFAULT 0.00
);

-- ------------------------------------------------------------
-- 6. TOPPING  (Perlas, Gelatinas, Pudding, Nube Crema...)
-- ------------------------------------------------------------
CREATE TABLE topping (
  topping_id   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(60)  NOT NULL,
  precio_extra DECIMAL(4,2) NOT NULL DEFAULT 0.00
);

-- ------------------------------------------------------------
-- 7. ALERGENOS
-- ------------------------------------------------------------
CREATE TABLE alergenos (
  alergeno_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre      VARCHAR(30) UNIQUE NOT NULL
);

-- ------------------------------------------------------------
-- 8. BUBBLETEA  (producto principal)
-- ------------------------------------------------------------
CREATE TABLE bubbletea (
  bubbletea_id        INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre              VARCHAR(100) NOT NULL,
  tipo_bubbletea      VARCHAR(50)  NOT NULL,
  descripcion         TEXT,
  categoria_id        INT UNSIGNED,
  disponible_caliente BOOLEAN      NOT NULL DEFAULT FALSE,
  es_vegano           BOOLEAN      NOT NULL DEFAULT FALSE,
  tiene_cafeina       BOOLEAN      NOT NULL DEFAULT FALSE,
  stock               INT UNSIGNED          DEFAULT 0,
  CONSTRAINT fk_bt_categoria
    FOREIGN KEY (categoria_id) REFERENCES categoria (categoria_id)
    ON UPDATE CASCADE ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- 9. BUBBLETEA_TAMANO  (precio por bebida y tamaño)
-- ------------------------------------------------------------
CREATE TABLE bubbletea_tamano (
  bubbletea_id INT UNSIGNED NOT NULL,
  tamano_id    INT UNSIGNED NOT NULL,
  precio       DECIMAL(8,2) NOT NULL,
  disponible   BOOLEAN      NOT NULL DEFAULT TRUE,
  PRIMARY KEY (bubbletea_id, tamano_id),
  CONSTRAINT fk_bts_bubbletea
    FOREIGN KEY (bubbletea_id) REFERENCES bubbletea (bubbletea_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_bts_tamano
    FOREIGN KEY (tamano_id) REFERENCES tamano (tamano_id)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- ------------------------------------------------------------
-- 10. BUBBLETEA_ALERGENO  (relación N:M)
-- ------------------------------------------------------------
CREATE TABLE bubbletea_alergeno (
  bubbletea_id INT UNSIGNED NOT NULL,
  alergeno_id  INT UNSIGNED NOT NULL,
  PRIMARY KEY (bubbletea_id, alergeno_id),
  CONSTRAINT fk_ba_bubbletea
    FOREIGN KEY (bubbletea_id) REFERENCES bubbletea (bubbletea_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_ba_alergeno
    FOREIGN KEY (alergeno_id) REFERENCES alergenos (alergeno_id)
    ON UPDATE CASCADE ON DELETE CASCADE
);

-- ------------------------------------------------------------
-- 11. PEDIDO  (cabecera — precio_total calculado desde líneas)
-- ------------------------------------------------------------
CREATE TABLE pedido (
  pedido_id       INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id      INT UNSIGNED NOT NULL,
  fecha_pedido    TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  envio_nacional  BOOLEAN               DEFAULT FALSE,
  direccion_envio VARCHAR(60),
  estado          ENUM('PENDIENTE','ENVIADO','RECIBIDO','DEVUELTO') NOT NULL DEFAULT 'PENDIENTE',
  precio_total    DECIMAL(8,2)          DEFAULT 0.00,  -- se actualiza desde pedido_linea
  CONSTRAINT fk_pedido_usuario
    FOREIGN KEY (usuario_id) REFERENCES usuario (usuario_id)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- ------------------------------------------------------------
-- 12. PEDIDO_LINEA  (cada bebida dentro de un pedido)
-- ------------------------------------------------------------
CREATE TABLE pedido_linea (
  linea_id      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  pedido_id     INT UNSIGNED NOT NULL,
  bubbletea_id  INT UNSIGNED NOT NULL,
  tamano_id     INT UNSIGNED NOT NULL,
  tipo_leche_id INT UNSIGNED,
  cantidad      INT UNSIGNED NOT NULL DEFAULT 1,
  nivel_azucar  ENUM('Extra','Regular','70%','50%','30%','Sin azucar') NOT NULL DEFAULT 'Regular',
  nivel_hielo   ENUM('Extra','Regular','Poco','No','Tibio','Caliente')  NOT NULL DEFAULT 'Regular',
  precio_unidad DECIMAL(8,2) NOT NULL,  -- precio en el momento de la compra
  CONSTRAINT fk_pl_pedido
    FOREIGN KEY (pedido_id)     REFERENCES pedido (pedido_id)          ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_pl_bubbletea
    FOREIGN KEY (bubbletea_id)  REFERENCES bubbletea (bubbletea_id)    ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT fk_pl_tamano
    FOREIGN KEY (tamano_id)     REFERENCES tamano (tamano_id)          ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT fk_pl_tipo_leche
    FOREIGN KEY (tipo_leche_id) REFERENCES tipo_leche (tipo_leche_id)  ON UPDATE CASCADE ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- 13. PEDIDO_LINEA_TOPPING  (toppings elegidos por línea)
-- ------------------------------------------------------------
CREATE TABLE pedido_linea_topping (
  linea_id   INT UNSIGNED NOT NULL,
  topping_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (linea_id, topping_id),
  CONSTRAINT fk_plt_linea
    FOREIGN KEY (linea_id)   REFERENCES pedido_linea (linea_id) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_plt_topping
    FOREIGN KEY (topping_id) REFERENCES topping (topping_id)    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- ============================================================
--  TRIGGER: actualiza precio_total en pedido al insertar línea
-- ============================================================
DELIMITER $$

CREATE TRIGGER trg_actualiza_total_insert
AFTER INSERT ON pedido_linea
FOR EACH ROW
BEGIN
  UPDATE pedido
  SET precio_total = (
    SELECT COALESCE(SUM(pl.precio_unidad * pl.cantidad), 0)
    FROM pedido_linea pl
    WHERE pl.pedido_id = NEW.pedido_id
  )
  WHERE pedido_id = NEW.pedido_id;
END$$

CREATE TRIGGER trg_actualiza_total_update
AFTER UPDATE ON pedido_linea
FOR EACH ROW
BEGIN
  UPDATE pedido
  SET precio_total = (
    SELECT COALESCE(SUM(pl.precio_unidad * pl.cantidad), 0)
    FROM pedido_linea pl
    WHERE pl.pedido_id = NEW.pedido_id
  )
  WHERE pedido_id = NEW.pedido_id;
END$$

CREATE TRIGGER trg_actualiza_total_delete
AFTER DELETE ON pedido_linea
FOR EACH ROW
BEGIN
  UPDATE pedido
  SET precio_total = (
    SELECT COALESCE(SUM(pl.precio_unidad * pl.cantidad), 0)
    FROM pedido_linea pl
    WHERE pl.pedido_id = OLD.pedido_id
  )
  WHERE pedido_id = OLD.pedido_id;
END$$

DELIMITER ;

-- ============================================================
--  DATOS DE EJEMPLO  (inspirados en el menú CoCo)
-- ============================================================

-- Categorías
INSERT INTO categoria (nombre, nombre_zh) VALUES
  ('Té con Leche',  '奶茶'),
  ('Leche Fresca',  '鲜奶'),
  ('Frutal',        '果茶'),
  ('Probiótico',    '养乐多'),
  ('Frappé',        '冰沙'),
  ('Especiales',    '特调'),
  ('Té',            '茶');

-- Tamaños
INSERT INTO tamano (codigo, nombre) VALUES
  ('M', 'Mediano'),
  ('L', 'Grande');

-- Tipos de leche
INSERT INTO tipo_leche (nombre, precio_extra) VALUES
  ('Regular (té de la leche)', 0.00),
  ('Leche Fresca',             0.50),
  ('Leche de Soja',            0.50),
  ('Leche de Avena',           0.50);

-- Toppings
INSERT INTO topping (nombre, precio_extra) VALUES
  ('Perlas de Tapioca',              0.50),
  ('Gelatina de Hierba Aromática',   0.50),
  ('Pudding',                        0.50),
  ('Gelatina de Coco',               0.80),
  ('Perlas de Tapioca con Azúcar Moreno', 0.80),
  ('Perlas Popping - Fresa',         0.80),
  ('Perlas Popping - Lichi',         0.80),
  ('Nube Crema de Leche',            1.00);

-- Alérgenos
INSERT INTO alergenos (nombre) VALUES
  ('Lácteo'),
  ('Gluten'),
  ('Soja'),
  ('Frutos secos'),
  ('Cafeína');

-- Bebidas
INSERT INTO bubbletea (nombre, tipo_bubbletea, descripcion, categoria_id, disponible_caliente, tiene_cafeina, es_vegano) VALUES
  -- Té con Leche
  ('Té con Leche Clásico',  'Té con Leche', 'Clásico té negro con leche', 1, TRUE,  TRUE,  FALSE),
  ('Té con Leche y Jazmín', 'Té con Leche', 'Té de jazmín con leche',     1, TRUE,  TRUE,  FALSE),
  ('Leche sabor a Taro',    'Té con Leche', 'Bebida de taro con leche',    1, FALSE, FALSE, FALSE),
  -- Leche Fresca
  ('3 Hermanos con Leche Fresca', 'Leche Fresca', 'Tapioca, Pudding y Gelatina de Hierba con leche fresca', 2, FALSE, FALSE, FALSE),
  -- Frutal
  ('Té Verde con Sabor a Mango',         'Frutal', 'Té verde con sirope de mango',              3, FALSE, TRUE, TRUE),
  ('Té Negro con Sabor a Maracuyá',      'Frutal', 'Té negro con maracuyá',                     3, FALSE, TRUE, TRUE),
  ('Té Verde con Zumo de Limón Natural', 'Frutal', 'Té verde con zumo de limón exprimido',      3, FALSE, TRUE, TRUE),
  ('Té Negro con Zumo de Limón Natural', 'Frutal', 'Té negro con zumo de limón exprimido',      3, FALSE, TRUE, TRUE),
  ('Rey del Limón',                      'Frutal', 'Té verde con un limón entero',               3, FALSE, TRUE, TRUE),
  -- Probiótico
  ('Té Verde con Yakult',         'Probiótico', 'Té verde con Yakult',              4, FALSE, TRUE,  TRUE),
  ('Mango Yakult',                'Probiótico', 'Mango con Yakult',                 4, FALSE, FALSE, TRUE),
  ('Zumo de Limón Natural con Yakult', 'Probiótico', 'Limón natural con Yakult',   4, FALSE, FALSE, TRUE),
  -- Frappé
  ('Frappé de Taro',              'Frappé', 'Frappé de taro',                       5, FALSE, FALSE, FALSE),
  ('Frappé de Mango y Maracuyá', 'Frappé', 'Frappé de mango con maracuyá',         5, FALSE, FALSE, TRUE),
  -- Especiales
  ('Popping Marte',     'Especial', 'Té verde de mango con perlas popping de fresa', 6, FALSE, TRUE, TRUE),
  ('Piruleta de Fresa', 'Especial', 'Té verde con leche y perlas popping de fresa',  6, FALSE, TRUE, FALSE),
  -- Té
  ('Té Negro',  'Té', 'Té negro solo', 7, TRUE, TRUE, TRUE),
  ('Té Verde',  'Té', 'Té verde solo', 7, TRUE, TRUE, TRUE);

-- Precios por tamaño (bubbletea_id, tamano_id M=1 L=2, precio)
INSERT INTO bubbletea_tamano (bubbletea_id, tamano_id, precio, disponible) VALUES
  (1,  1, 4.50, TRUE),
  (2,  1, 4.50, TRUE),
  (3,  1, 4.50, TRUE),
  (4,  1, 6.00, TRUE),
  (5,  1, 5.00, TRUE),
  (6,  1, 5.00, TRUE),
  (7,  1, 5.00, TRUE),
  (8,  1, 5.00, TRUE),
  (9,  1, 5.90, TRUE),  (9,  2, 5.90, TRUE),  -- Solo talla L según menú
  (10, 1, 5.90, TRUE),
  (11, 1, 5.90, TRUE),
  (12, 1, 5.90, TRUE),
  (13, 1, 5.50, TRUE),
  (14, 1, 5.50, TRUE),
  (15, 1, 5.50, TRUE),
  (16, 1, 6.00, TRUE),  (16, 2, 6.00, TRUE),  -- Solo talla L
  (17, 1, 3.90, TRUE),
  (18, 1, 3.90, TRUE);

-- Alérgenos por bebida (ejemplos)
INSERT INTO bubbletea_alergeno (bubbletea_id, alergeno_id) VALUES
  (1,  1), (1,  5),   -- Clásico: lácteo + cafeína
  (2,  1), (2,  5),
  (3,  1),
  (4,  1),
  (5,  5),
  (6,  5),
  (7,  5),
  (8,  5),
  (9,  5),
  (10, 5),
  (17, 5),
  (18, 5);

-- Usuario de ejemplo
INSERT INTO usuario (nombre, nombre_usuario, email, contrasena, pais, ciudad, direccion, telf) VALUES
  ('Ana García', 'anagarcia', 'ana@email.com', 'pass1234', 'España', 'Barcelona', 'Calle Mayor 10', 612345678);

INSERT INTO perfil_usuario (usuario_id, nombre_usuario, email, contrasena, pais, ciudad, direccion, telf) VALUES
  (1, 'anagarcia', 'ana@email.com', 'pass1234', 'España', 'Barcelona', 'Calle Mayor 10', 612345678);

-- Pedido de ejemplo
INSERT INTO pedido (usuario_id, envio_nacional, direccion_envio, estado) VALUES
  (1, FALSE, 'Calle Mayor 10, Barcelona', 'PENDIENTE');

-- Líneas del pedido (precio_total se calcula automáticamente con el trigger)
INSERT INTO pedido_linea (pedido_id, bubbletea_id, tamano_id, tipo_leche_id, cantidad, nivel_azucar, nivel_hielo, precio_unidad) VALUES
  (1, 1, 1, 1, 2, 'Regular', 'Regular', 4.50),   -- 2x Té con Leche Clásico M
  (1, 5, 1, NULL, 1, '70%',     'Poco',    5.00); -- 1x Té Verde Mango M

-- Toppings de las líneas
INSERT INTO pedido_linea_topping (linea_id, topping_id) VALUES
  (1, 1),  -- Perlas de Tapioca en línea 1
  (2, 6);  -- Perlas Popping Fresa en línea 2

-- Verificación final
SHOW TABLES;
