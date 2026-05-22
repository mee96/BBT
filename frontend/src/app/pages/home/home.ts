import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { BubbleteaService, BubbleTea } from '../../services/bubbletea';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
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
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.carregarRandom();
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

  copiarUrl(): void {
    navigator.clipboard.writeText('https://bbt-760x.onrender.com');
  }
}