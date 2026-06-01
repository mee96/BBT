import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { Auth } from '@angular/fire/auth';
import { from, switchMap } from 'rxjs';

/**
 * Adjunta l'ID token de Firebase ('Authorization: Bearer <token>') a totes
 * les peticions HTTP quan hi ha un usuari autenticat. Si no n'hi ha, la
 * petició passa sense capçalera (els endpoints públics segueixen funcionant).
 */
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(Auth);
  const currentUser = auth.currentUser;

  if (!currentUser) {
    return next(req);
  }

  return from(currentUser.getIdToken()).pipe(
    switchMap(token => {
      const authReq = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` },
      });
      return next(authReq);
    })
  );
};
