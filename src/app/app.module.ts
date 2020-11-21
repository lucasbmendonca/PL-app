import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { SelecionarFicheirosComponent } from './componentes/selecionar-ficheiros/selecionar-ficheiros.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule} from '@angular/material/icon';
import {  MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import {  MatProgressBarModule } from '@angular/material/progress-bar';
import { EstatisticasComponent } from './componentes/estatisticas/estatisticas.component';
import { TodosOsTestesComponent } from './componentes/todos-os-testes/todos-os-testes.component';
import { ResultadoTestesComponent } from './componentes/resultado-testes/resultado-testes.component';
import {MatDividerModule} from '@angular/material/divider';

@NgModule({
  declarations: [
    AppComponent,
    SelecionarFicheirosComponent,
    EstatisticasComponent,
    TodosOsTestesComponent,
    ResultadoTestesComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    MatCardModule,
    MatProgressBarModule,
    MatDividerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
