import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home';
import { BebidasComponent } from './pages/bebidas/bebidas';
import { LoginComponent } from './pages/login/login';
import { RegisterComponent } from './pages/register/register';
import { User } from './pages/user/user';
import { authGuard } from './guards/auth-guard';
import { AdminComponent } from './pages/admin/admin';


export const routes: Routes = [
  { path: '',         component: HomeComponent },
  { path: 'bebidas',  component: BebidasComponent, canActivate: [authGuard] },
  { path: 'login',    component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'user',     component: User},
  { path: 'admin', component: AdminComponent },
  { path: '**',       redirectTo: '' }
];