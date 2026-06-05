import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth/auth';
import { User as FirebaseUser } from '@angular/fire/auth';
import { Observable, firstValueFrom } from 'rxjs';
import { UsuarioAiven } from '../../models/usuario';

interface BbtDelDia {
  nom: string;
  img: string;
  color: string;
  borderColor: string;
  titlebarColor: string;
  textColor: string;
}

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './user.html',
  styleUrl: './user.scss',
})
export class User implements OnInit {

  private authService = inject(AuthService);
  private router = inject(Router);

  readonly user$: Observable<FirebaseUser | null> = this.authService.user$;

  usuariAiven: UsuarioAiven | null = null;
  editant: boolean = false;
  loading: boolean = false;
  error: string | null = null;
  success: string | null = null;

  // Edició
  editNom: string = '';
  editCognom: string = '';
  editFechaNacimiento: string = '';
  editNotifications: boolean = true;

  // Beguda del dia
readonly bbts: BbtDelDia[] = [
  {
    nom: 'Taro Bubble Tea',
    img: 'assets/Taro bubble tea.jpg',
    color: '#f0eaf8',
    borderColor: '#b8a0d0',
    titlebarColor: '#e0d0f0',
    textColor: '#7b4fa6'
  },
  {
    nom: 'Matcha Bubble Tea',
    img: 'assets/Matcha bubble tea.jpg',
    color: '#f0f8f0',
    borderColor: '#8ab88a',
    titlebarColor: '#c8e8c8',
    textColor: '#2a6a2a'
  },
  {
    nom: 'Mango Bubble Tea',
    img: 'assets/Mango bubble tea.jpg',
    color: '#fdf8e8',
    borderColor: '#d4a830',
    titlebarColor: '#f0e098',
    textColor: '#806020'
  }
];
  bbtDelDia: BbtDelDia = this.bbts[Math.floor(Math.random() * this.bbts.length)];

  async ngOnInit(): Promise<void> {
    const firebaseUser = this.authService.getCurrentUser();
    if (firebaseUser) {
      try {
        const res: any = await firstValueFrom(
          this.authService.getUsuariAiven(firebaseUser.uid)
        );
        if (res.ok) {
          this.usuariAiven = res.result;
          this.editNom = res.result?.nombre || '';
          this.editCognom = res.result?.apellido || '';
          this.editFechaNacimiento = res.result?.fecha_nacimiento || '';
          this.editNotifications = res.result?.notifications ?? true;
        }
      } catch (err) {
        console.error('Error carregant usuari:', err);
      }
    }
  }

  async guardar(): Promise<void> {
    const firebaseUser = this.authService.getCurrentUser();
    if (!firebaseUser) return;

    this.loading = true;
    this.error = null;
    this.success = null;

    try {
      await firstValueFrom(
        this.authService.updateUsuariAiven(firebaseUser.uid, {
          nombre: this.editNom,
          apellido: this.editCognom,
          fecha_nacimiento: this.editFechaNacimiento || null,
          notifications: this.editNotifications
        })
      );
      this.success = 'Dades actualitzades! ✅';
      this.editant = false;
      await this.ngOnInit();
    } catch (err) {
      this.error = 'Error al guardar';
    } finally {
      this.loading = false;
    }
  }

  async logout(): Promise<void> {
    await this.authService.logout();
    this.router.navigate(['/']);
  }
}