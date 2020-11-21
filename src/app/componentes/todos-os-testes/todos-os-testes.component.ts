import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos-os-testes',
  templateUrl: './todos-os-testes.component.html',
  styleUrls: ['./todos-os-testes.component.css']
})
export class TodosOsTestesComponent implements OnInit {

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }
  gethist(){
    this.http.get('http://localhost:8000/hist-Tests').subscribe(res => console.log(res))
  }

}
