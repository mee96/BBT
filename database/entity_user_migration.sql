-- =====================================================================
-- Migración: tabla `usuario` (PK int autoincrement) -> `entity_user`
-- (PK = firebase_uid en VARCHAR). Pedidos quedan DESACOPLADOS de usuario.
-- Ejecutar en orden contra la BD de Aiven (MySQL).
-- ⚠️ DESTRUCTIVO E IRREVERSIBLE: borra la tabla usuario y sus datos.
-- =====================================================================

-- 1) Quitar la FK de pedido -> usuario (desacoplar pedidos).
--    El nombre de la constraint suele ser 'pedido_ibfk_1'. Si no, búscalo con:
--      SELECT CONSTRAINT_NAME
--      FROM information_schema.KEY_COLUMN_USAGE
--      WHERE TABLE_SCHEMA = DATABASE()
--        AND TABLE_NAME = 'pedido'
--        AND REFERENCED_TABLE_NAME = 'usuario';
ALTER TABLE pedido DROP FOREIGN KEY pedido_ibfk_1;

-- 2) Eliminar la tabla usuario antigua.
DROP TABLE IF EXISTS usuario;

-- 3) Crear la nueva tabla entity_user.
DROP TABLE IF EXISTS entity_user;
CREATE TABLE entity_user (
  usuario_id        VARCHAR(128) PRIMARY KEY,   -- = firebase_uid
  nombre            VARCHAR(50)  NOT NULL,
  apellido          VARCHAR(50),
  email             VARCHAR(50)  UNIQUE NOT NULL,
  fecha_nacimiento  DATE,
  active            BOOLEAN DEFAULT TRUE,
  notifications     BOOLEAN DEFAULT TRUE
);
