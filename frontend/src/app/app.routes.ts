import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home';
import { BebidasComponent} from './pages/bebidas/bebidas';

export const routes: Routes = [
  { path: '',        component: HomeComponent },
  { path: 'bebidas', component: BebidasComponent },
  { path: '**',      redirectTo: '' }
];