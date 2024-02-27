import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { MessageService } from 'primeng/api';
import { Book } from './interfaces/book.interface';

@Injectable({
  providedIn: 'root',
})
export class SearchService {
  private baseUrl = 'http://localhost:40000/';
  private apiurl = 'api/search';
  constructor(private httpClient: HttpClient) {}

  search(query: string[]): Observable<Book[]> {
    let params = new HttpParams();
    query.forEach((q) => (params = params.append('title', q)));
    return this.httpClient.get<Book[]>(`${this.baseUrl}${this.apiurl}`, {
      params,
    });
  }
  searcsh(query: string[]): Observable<Book[]> {
    return this.httpClient.get<Book[]>(`${this.baseUrl}/api/search/${query}`);
  }
}
