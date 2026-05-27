import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home';
import { BebidasComponent } from './pages/bebidas/bebidas';
import { LoginComponent } from './pages/login/login';
import { RegisterComponent } from './pages/register/register';
// import { UserComponent } from './pages/user/user';

export const routes: Routes = [
  { path: '',         component: HomeComponent },
  { path: 'bebidas',  component: BebidasComponent },
  { path: 'login',    component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  // { path: 'user',     component: UserComponent },
  { path: '**',       redirectTo: '' }
];