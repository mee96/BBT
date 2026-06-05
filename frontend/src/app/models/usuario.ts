export interface UsuarioAiven {
  usuario_id: string;
  nombre: string;
  apellido?: string;
  email: string;
  fecha_nacimiento?: string;
  active?: boolean;
  notifications?: boolean;
}
