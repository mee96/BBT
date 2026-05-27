import { Injectable, inject } from '@angular/core';
import { Auth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, user } from '@angular/fire/auth';
import { Observable } from 'rxjs';
import { User } from '@angular/fire/auth';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private auth: Auth = inject(Auth);

  readonly user$: Observable<User | null> = user(this.auth);

  register(email: string, password: string): Promise<void> {
    return createUserWithEmailAndPassword(this.auth, email, password)
      .then(() => {});
  }

  login(email: string, password: string): Promise<void> {
    return signInWithEmailAndPassword(this.auth, email, password)
      .then(() => {});
  }

  logout(): Promise<void> {
    return signOut(this.auth);
  }

  getCurrentUser(): User | null {
    return this.auth.currentUser;
  }
}