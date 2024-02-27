import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PrimeNgModule } from './prime-ng/prime-ng.module';
import { FormsModule } from '@angular/forms';
import { SearchService } from './servicios.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    PrimeNgModule,
    FormsModule
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'ReadingRecommender';

  results: string[] = ['libro_1', 'libro_2', 'libro_3', 'libro_4', 'libro_5']

  constructor(private _service: SearchService) { }

  query!: string;
  queries!: string[];

  search() {
    console.log(this.query)
    this.queries.push(this.query)
    this._service.search(this.queries).subscribe(
      (data: any) => {
        console.log(data)
        this.results = data
      })
  }
}
