import { Injectable, inject } from '@angular/core';
import { Auth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, user } from '@angular/fire/auth';
import { HttpClient } from '@angular/common/http';
import { Observable, firstValueFrom } from 'rxjs';
import { User } from '@angular/fire/auth';
import { UsuarioAiven } from '../../models/usuario';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private auth: Auth = inject(Auth);
  private http: HttpClient = inject(HttpClient);
  private readonly apiUrl: string = 'https://bbt-760x.onrender.com/';

  readonly user$: Observable<User | null> = user(this.auth);

  async register(email: string, password: string, usuariDades: Omit<UsuarioAiven, 'firebase_uid' | 'email'>): Promise<void> {
    const credential = await createUserWithEmailAndPassword(this.auth, email, password);
    const firebase_uid = credential.user.uid;

    await firstValueFrom(
      this.http.post(`${this.apiUrl}usuarios/`, {
        firebase_uid,
        email,
        ...usuariDades
      })
    );
  }

  async login(email: string, password: string): Promise<void> {
    await signInWithEmailAndPassword(this.auth, email, password);
  }

  logout(): Promise<void> {
    return signOut(this.auth);
  }

  getCurrentUser(): User | null {
    return this.auth.currentUser;
  }

  getUsuariAiven(firebase_uid: string): Observable<any> {
    return this.http.get(`${this.apiUrl}usuarios/firebase/${firebase_uid}`);
  }

  updateUsuariAiven(firebase_uid: string, dades: any): Observable<any> {
  return this.http.put(`${this.apiUrl}usuarios/firebase/${firebase_uid}`, dades);
}
}

