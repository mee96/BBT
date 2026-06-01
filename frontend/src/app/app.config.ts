import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { provideFirebaseApp, initializeApp } from '@angular/fire/app';
import { provideAuth, getAuth } from '@angular/fire/auth';
import { routes } from './app.routes';
import { authInterceptor } from './interceptors/auth-interceptor';

const firebaseConfig = {
  apiKey: "AIzaSyDBfpvjfoziR1UN8wEvat0CmRqPrD_wDP8",
  authDomain: "bbtapi-d80f9.firebaseapp.com",
  projectId: "bbtapi-d80f9",
  storageBucket: "bbtapi-d80f9.firebasestorage.app",
  messagingSenderId: "5071205946",
  appId: "1:5071205946:web:f124c27acaf4a344d3a703"
};

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(withInterceptors([authInterceptor])),
    provideFirebaseApp(() => initializeApp(firebaseConfig)),
    provideAuth(() => getAuth()),
  ]
};