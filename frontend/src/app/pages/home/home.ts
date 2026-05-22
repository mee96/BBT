import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BubbleteaService, BubbleTea } from '../../services/bubbletea';

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

  constructor(private bubbleteaService: BubbleteaService) {}

  ngOnInit(): void {
    this.carregarRandom();
  }

  carregarRandom(): void {
    this.loading = true;
    this.error = null;
    this.bubbleteaService.getBebidaRandom().subscribe({
      next: (bebida: BubbleTea) => {
        this.bebidaRandom = bebida;
        this.loading = false;
      },
      error: (err: Error) => {
        this.error = 'No s\'ha pogut connectar amb la API';
        this.loading = false;
        console.error(err);
      }
    });
  }
}