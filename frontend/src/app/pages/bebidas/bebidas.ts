import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BubbleteaService, BubbleTea } from '../../services/bubbletea';

@Component({
  selector: 'app-bebidas',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './bebidas.html',
  styleUrl: './bebidas.scss'
})
export class BebidasComponent implements OnInit {

  bebidas: BubbleTea[] = [];
  totes: BubbleTea[] = [];
  loading: boolean = false;
  error: string | null = null;
  filtreActiu: string = 'totes';

  readonly categories: string[] = [
    'Té con Leche',
    'Leche Fresca',
    'Frutal',
    'Probiótico',
    'Frappé',
    'Especiales',
    'Té'
  ];

  constructor(
    private bubbleteaService: BubbleteaService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.carregarBebidas();
  }

  carregarBebidas(): void {
    this.loading = true;
    this.error = null;
    this.cdr.detectChanges();
    this.bubbleteaService.getBebidas().subscribe({
      next: (bebidas: BubbleTea[]) => {
        this.totes = bebidas;
        this.bebidas = bebidas;
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

  aplicarFiltre(filtre: string): void {
    this.filtreActiu = filtre;
    if (filtre === 'totes') {
      this.bebidas = this.totes;
    } else {
      this.bebidas = this.totes.filter(
        (b: BubbleTea) => b.tipo_bubbletea === filtre
      );
    }
    this.cdr.detectChanges();
  }

  getImatge(tipusBebida: string): string {
  const mapa: Record<string, string> = {
    'Té con Leche': 'assets/bbt-lila.png',
    'Leche Fresca': 'assets/bbt-lila.png',
    'Frappé':       'assets/bbt-lila.png',
    'Frutal':       'assets/bbt-red.png',
    'Probiótico':   'assets/bbt-red.png',
    'Especial':     'assets/bbt-red.png',
    'Té':           'assets/bbt-red.png',
  };
  return mapa[tipusBebida] ?? 'assets/bbt-lila.png';
}

  
}