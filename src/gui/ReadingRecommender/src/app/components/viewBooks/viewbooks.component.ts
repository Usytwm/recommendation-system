import { Component, ElementRef, Input, ViewChild } from '@angular/core';
import { Book } from '../../interfaces/book.interface';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-viewbooks',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './viewbooks.component.html',
  styleUrl: './viewbooks.component.css',
})
export class ViewBooksComponent {
  @Input() books!: Book[];
  @ViewChild('descriptionContainer') descriptionContainer?: ElementRef;
  selectedBook?: Book;
  selectBook(book: Book): void {
    this.selectedBook = book; // Actualiza el libro seleccionado con el que se ha hecho clic
    this.descriptionContainer!.nativeElement.scrollIntoView({
      behavior: 'smooth',
    });
  }
}
