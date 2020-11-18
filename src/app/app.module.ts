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

@NgModule({
  declarations: [
    AppComponent,
    SelecionarFicheirosComponent
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
    MatProgressBarModule  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
