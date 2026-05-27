import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth/auth';
import { User as FirebaseUser } from '@angular/fire/auth';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './user.html',
  styleUrl: './user.scss',
})
export class User {

  private authService = inject(AuthService);
  private router = inject(Router);

  readonly user$: Observable<FirebaseUser | null> = this.authService.user$;

  async logout(): Promise<void> {
    await this.authService.logout();
    this.router.navigate(['/']);
  }
}