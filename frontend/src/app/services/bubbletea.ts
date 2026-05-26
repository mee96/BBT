import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

export interface BubbleTea {
  bubbletea_id: number;
  nombre: string;
  tipo_bubbletea: string;
  descripcion: string | null;
  categoria_id: number | null;
  disponible_caliente: boolean;
  es_vegano: boolean;
  tiene_cafeina: boolean;
  precio_M: number | null;
  precio_L: number | null;
  alergenos: string[];
  activo: boolean;
}

export interface BebidaFiltres {
  activo?: boolean;
  vegano?: boolean;
  caliente?: boolean;
  categoria_id?: number;
}

interface ApiResponse<T> {
  ok: boolean;
  result: T;
}

@Injectable({
  providedIn: 'root'
})
export class BubbleteaService {

  private readonly apiUrl: string = 'https://bbt-760x.onrender.com/';

  constructor(private http: HttpClient) {}

  getBebidas(): Observable<BubbleTea[]> {
    return this.http.get<ApiResponse<BubbleTea[]>>(`${this.apiUrl}bubbleteas/`)
      .pipe(map(res => res.result));
  }

  getBebida(id: number): Observable<BubbleTea> {
    return this.http.get<ApiResponse<BubbleTea>>(`${this.apiUrl}bubbleteas/${id}`)
      .pipe(map(res => res.result));
  }

  getBebidaRandom(): Observable<BubbleTea> {
    return this.http.get<ApiResponse<BubbleTea>>(`${this.apiUrl}bubbleteas/random`)
      .pipe(map(res => res.result));
  }

  getBebidasFiltrades(filtres: BebidaFiltres): Observable<BubbleTea[]> {
    let params = new HttpParams();

    if (filtres.activo !== undefined) {
      params = params.set('activo', filtres.activo.toString());
    }
    if (filtres.vegano !== undefined) {
      params = params.set('vegano', filtres.vegano.toString());
    }
    if (filtres.caliente !== undefined) {
      params = params.set('caliente', filtres.caliente.toString());
    }
    if (filtres.categoria_id !== undefined) {
      params = params.set('categoria_id', filtres.categoria_id.toString());
    }

    return this.http.get<ApiResponse<BubbleTea[]>>(`${this.apiUrl}bubbleteas/`, { params })
      .pipe(map(res => res.result));
  }
}