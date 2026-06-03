import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { BubbleteaService, BubbleTea } from '../../services/bubbletea';
import { HttpClient } from '@angular/common/http';

interface BubbleTeaForm {
  nombre: string;
  tipo_bubbletea: string;
  descripcion: string;
  categoria_id: number | null;
  disponible_caliente: boolean;
  es_vegano: boolean;
  tiene_cafeina: boolean;
  stock: number;
  active: boolean;
}

@Component({
  selector: 'app-admin',
  imports: [CommonModule, FormsModule],
  templateUrl: './admin.html',
  styleUrl: './admin.scss'
})
export class AdminComponent implements OnInit {

  private readonly apiUrl = 'https://bbt-760x.onrender.com/';

  private bubbleteaService = inject(BubbleteaService);
  private http = inject(HttpClient);

  bebidas = signal<BubbleTea[]>([]);
  categorias = signal<any[]>([]);
  loading = signal<boolean>(false);
  error = signal<string | null>(null);
  success = signal<string | null>(null);

  // Formulari
  mostrarFormulari = signal<boolean>(false);
  editantId = signal<number | null>(null);

  form: BubbleTeaForm = {
    nombre: '',
    tipo_bubbletea: '',
    descripcion: '',
    categoria_id: null,
    disponible_caliente: false,
    es_vegano: false,
    tiene_cafeina: false,
    stock: 0,
    active: true
  };

  ngOnInit(): void {
    this.carregarBebidas();
    this.carregarCategorias();
  }

  // Categories que no s'han de mostrar al formulari
  private readonly categoriesOcultes = ['especial here', 'brown sugar', 'frui tea', 'mousse tea'];

  carregarCategorias(): void {
    this.http.get<any>(`${this.apiUrl}categorias/`).subscribe({
      next: (res) => this.categorias.set(
        (res.result as any[]).filter(
          (c) => !this.categoriesOcultes.includes((c.nombre || '').toLowerCase())
        )
      ),
      error: () => console.error('Error carregant categories')
    });
  }

  carregarBebidas(): void {
    this.loading.set(true);
    this.bubbleteaService.getBebidas().subscribe({
      next: (bebidas) => {
        this.bebidas.set(bebidas);
        this.loading.set(false);
      },
      error: () => {
        this.error.set('Error carregant begudes');
        this.loading.set(false);
      }
    });
  }

  nouFormulari(): void {
    this.editantId.set(null);
    this.form = {
      nombre: '', tipo_bubbletea: '', descripcion: '',
      categoria_id: null, disponible_caliente: false,
      es_vegano: false, tiene_cafeina: false, stock: 0, active: true
    };
    this.mostrarFormulari.set(true);
  }

  editarBebida(bebida: BubbleTea): void {
    this.editantId.set(bebida.bubbletea_id);
    this.form = {
      nombre: bebida.nombre,
      tipo_bubbletea: bebida.tipo_bubbletea,
      descripcion: bebida.descripcion || '',
      categoria_id: bebida.categoria_id,
      disponible_caliente: bebida.disponible_caliente,
      es_vegano: bebida.es_vegano,
      tiene_cafeina: bebida.tiene_cafeina,
      stock: 0,
      active: bebida.activo
    };
    this.mostrarFormulari.set(true);
  }

  guardar(): void {
    this.error.set(null);
    this.success.set(null);

    // tipo_bubbletea es deriva de la categoria (el backend l'exigeix)
    const cat = this.categorias().find((c) => c.categoria_id === Number(this.form.categoria_id));
    const payload = { ...this.form, tipo_bubbletea: cat?.nombre ?? '' };

    const id = this.editantId();
    if (id) {
      this.http.put(`${this.apiUrl}bubbleteas/${id}`, payload).subscribe({
        next: () => {
          this.success.set('Beguda actualitzada! ✅');
          this.mostrarFormulari.set(false);
          this.carregarBebidas();
          setTimeout(() => this.success.set(null), 3000);
        },
        error: () => this.error.set('Error actualitzant')
      });
    } else {
      this.http.post(`${this.apiUrl}bubbleteas/`, payload).subscribe({
        next: () => {
          this.success.set('Beguda creada! ✅');
          this.mostrarFormulari.set(false);
          this.carregarBebidas();
          setTimeout(() => this.success.set(null), 3000);
        },
        error: () => this.error.set('Error creant')
      });
    }
  }

  eliminar(id: number): void {
    if (!confirm('Segur que vols eliminar aquesta beguda?')) return;
    this.http.delete(`${this.apiUrl}bubbleteas/${id}`).subscribe({
      next: () => {
        this.success.set('Beguda eliminada! ✅');
        this.carregarBebidas();
        setTimeout(() => this.success.set(null), 3000);
      },
      error: () => this.error.set('Error eliminant')
    });
  }

  cancelar(): void {
    this.mostrarFormulari.set(false);
    this.editantId.set(null);
  }
}
