import { Injectable, inject } from '@angular/core';
import { Auth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, user } from '@angular/fire/auth';
import { HttpClient } from '@angular/common/http';
import { Observable, firstValueFrom } from 'rxjs';
import { User } from '@angular/fire/auth';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private auth: Auth = inject(Auth);
  private http: HttpClient = inject(HttpClient);
  private readonly apiUrl: string = 'https://bbt-760x.onrender.com/';

  readonly user$: Observable<User | null> = user(this.auth);

  async register(email: string, password: string, dades: { nombre: string; apellido: string }): Promise<void> {
    const credential = await createUserWithEmailAndPassword(this.auth, email, password);

    await firstValueFrom(
      this.http.post(`${this.apiUrl}usuarios/`, {
        firebase_uid: credential.user.uid,
        nombre: dades.nombre,
        apellido: dades.apellido,
        email
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

