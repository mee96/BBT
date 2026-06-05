import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../services/auth/auth';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.scss'
})
export class LoginComponent {

  email: string = '';
  password: string = '';
  error = signal<string | null>(null);
  loading = signal<boolean>(false);
  showPassword = signal<boolean>(false);

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  async login(): Promise<void> {
    this.loading.set(true);
    this.error.set(null);
    try {
      await this.authService.login(this.email, this.password);
      this.router.navigate(['/']);
    } catch (err: any) {
      this.error.set(this.missatgeError(err?.code));
      this.loading.set(false);
    }
  }

  private missatgeError(code: string): string {
    switch (code) {
      case 'auth/user-not-found':
        return 'Usuari no trobat';
      case 'auth/wrong-password':
        return 'Contrasenya incorrecta';
      default:
        return 'Hi ha hagut un error. Torna-ho a provar.';
    }
  }
}
