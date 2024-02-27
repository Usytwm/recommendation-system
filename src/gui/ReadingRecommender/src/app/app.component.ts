import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PrimeNgModule } from './prime-ng/prime-ng.module';
import { FormsModule } from '@angular/forms';
import { SearchService } from './servicios.service';
import { HttpClientModule } from '@angular/common/http';
import { HomeComponent } from './components/home/home.component';
import { ViewBooksComponent } from './components/viewBooks/viewbooks.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    PrimeNgModule,
    FormsModule,
    HttpClientModule,
    HomeComponent,
  ],
  providers: [SearchService, HomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {}
