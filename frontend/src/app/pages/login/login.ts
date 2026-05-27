import { Component } from '@angular/core';
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
  error: string | null = null;
  loading: boolean = false;

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  async login(): Promise<void> {
    this.loading = true;
    this.error = null;
    try {
      await this.authService.login(this.email, this.password);
      this.router.navigate(['/']);
    } catch (err: any) {
      this.error = 'Email o contrasenya incorrectes';
      this.loading = false;
    }
  }
}