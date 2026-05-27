import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../services/auth/auth';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './register.html',
  styleUrl: './register.scss'
})
export class RegisterComponent {

  nom: string = '';
  nombre_usuario: string = '';
  email: string = '';
  password: string = '';
  passwordRepeat: string = '';
  error: string | null = null;
  loading: boolean = false;

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  async register(): Promise<void> {
    if (this.password !== this.passwordRepeat) {
      this.error = 'Les contrasenyes no coincideixen';
      return;
    }
    this.loading = true;
    this.error = null;
    try {
      await this.authService.register(this.email, this.password, {
        nombre: this.nom,
        nombre_usuario: this.nombre_usuario,
      });
      this.router.navigate(['/']);
    } catch (err: any) {
      this.error = 'Error al registrar-se. Prova un altre email.';
      this.loading = false;
    }
  }
}