import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MultiSelectModule } from 'primeng/multiselect';
import { ViewBooksComponent } from '../viewBooks/viewbooks.component';
import { Book } from '../../interfaces/book.interface';
import { SearchService } from '../../servicios.service';
import { CommonModule } from '@angular/common';

interface City {
  name: string;
  code: string;
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    MultiSelectModule,
    FormsModule,
    ReactiveFormsModule,
    ViewBooksComponent,
    CommonModule,
  ],
  providers: [SearchService],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent implements OnInit {
  cities!: City[];
  books: Book[] = [];
  loading: boolean = false;

  constructor(private _service: SearchService) {}
  ngOnInit(): void {}

  searchQuery: string = ''; // Almacena el valor del input aquí

  sendSearchQuery(): void {
    // Define una expresión regular que captura únicamente frases dentro de comillas dobles
    const regex = /"([^"]*)"/g;

    // Busca todas las coincidencias de frases entre comillas en la cadena de búsqueda
    const matches = this.searchQuery.match(regex);

    // Extrae las frases capturadas, removiendo las comillas dobles
    const queryArray = matches
      ? matches.map((match) => match.replace(/"/g, ''))
      : [];

    this.loading = true;
    this._service.search(queryArray).subscribe((data: any) => {
      console.log(data);
      this.books = data;
      this.loading = false;
    });
    console.log('"Always Coming Home" "Drowned Wednesday"');
  }
}
