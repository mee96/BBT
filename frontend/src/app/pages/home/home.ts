import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { BubbleteaService, BubbleTea } from '../../services/bubbletea';
import { AuthService } from '../../services/auth/auth';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.html',
  styleUrl: './home.scss'
})
export class HomeComponent implements OnInit {

  bebidaRandom: BubbleTea | null = null;
  loading: boolean = false;
  error: string | null = null;
  tabActiu: string = 'js';

  constructor(
    private bubbleteaService: BubbleteaService,
    private cdr: ChangeDetectorRef,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.carregarRandom();
  }

  explorarBegudes(): void {
    const user = this.authService.getCurrentUser();
    if (user) {
      this.router.navigate(['/bebidas']);
    } else {
      this.router.navigate(['/login']);
    }
  }

  copiarUrl(): void {
    navigator.clipboard.writeText('https://bbt-760x.onrender.com');
  }

  carregarRandom(): void {
    this.loading = true;
    this.error = null;
    this.cdr.detectChanges();
    this.bubbleteaService.getBebidaRandom().subscribe({
      next: (bebida: BubbleTea) => {
        this.bebidaRandom = bebida;
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err: Error) => {
        this.error = 'No s\'ha pogut connectar amb la API';
        this.loading = false;
        this.cdr.detectChanges();
        console.error(err);
      }
    });
  }
}