import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, firstValueFrom } from 'rxjs';
import { MessageService } from 'primeng/api';
interface SearchResult {
  title: string,
  description: string
}

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  private apiUrl = 'http://localhost:40000';
  constructor(private httpClient: HttpClient, private messageService: MessageService) { }

  search(query: string[]): Observable<SearchResult[]> {
    let params = new HttpParams();
    query.forEach(q => params = params.append('title', q));
    return this.httpClient.get<SearchResult[]>(this.apiUrl, { params });
  }
  searcsh(query: string[],): Observable<SearchResult[]> {
    return this.httpClient.get<SearchResult[]>(`${this.apiUrl}/api/search/${query}`)
  }
}
