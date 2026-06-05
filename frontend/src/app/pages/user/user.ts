import { Component, inject, OnInit, signal } from '@angular/core';
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

  usuariAiven = signal<UsuarioAiven | null>(null);
  editant = signal<boolean>(false);
  loading = signal<boolean>(false);
  error = signal<string | null>(null);
  success = signal<string | null>(null);

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

  ngOnInit(): void {
    // Esperem que Firebase resolgui la sessió abans de carregar les dades.
    this.user$.subscribe((firebaseUser) => {
      if (firebaseUser) {
        this.carregarUsuari(firebaseUser.uid);
      }
    });
  }

  private async carregarUsuari(uid: string): Promise<void> {
    try {
      const res: any = await firstValueFrom(this.authService.getUsuariAiven(uid));
      if (res.ok && res.result) {
        this.editNom = res.result.nombre || '';
        this.editCognom = res.result.apellido || '';
        this.editFechaNacimiento = res.result.fecha_nacimiento || '';
        this.editNotifications = res.result.notifications ?? true;
        this.usuariAiven.set(res.result);
      }
    } catch (err) {
      console.error('Error carregant usuari:', err);
    }
  }

  async guardar(): Promise<void> {
    const firebaseUser = this.authService.getCurrentUser();
    if (!firebaseUser) return;

    this.loading.set(true);
    this.error.set(null);
    this.success.set(null);

    try {
      await firstValueFrom(
        this.authService.updateUsuariAiven(firebaseUser.uid, {
          nombre: this.editNom,
          apellido: this.editCognom,
          fecha_nacimiento: this.editFechaNacimiento || null,
          notifications: this.editNotifications
        })
      );
      this.success.set('Dades actualitzades! ✅');
      this.editant.set(false);
      await this.carregarUsuari(firebaseUser.uid);
    } catch (err) {
      this.error.set('Error al guardar');
    } finally {
      this.loading.set(false);
    }
  }

  async logout(): Promise<void> {
    await this.authService.logout();
    this.router.navigate(['/']);
  }
}