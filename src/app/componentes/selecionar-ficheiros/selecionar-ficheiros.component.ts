import { UploadServiceService } from './upload-service.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-selecionar-ficheiros',
  templateUrl: './selecionar-ficheiros.component.html',
  styleUrls: ['./selecionar-ficheiros.component.css']
})
export class SelecionarFicheirosComponent implements OnInit {

  files: Set<File>; //evitar arquivos duplicados
  nomeFicheiros = [];

  constructor(private service: UploadServiceService) { }

  ngOnInit(): void {
  }

  onChange(event){

    console.log(event)
    const ficheiros_selecionados = <FileList>event.srcElement.files;
    this.nomeFicheiros = [];


    this.files = new Set();
    for(let i = 0; i< ficheiros_selecionados.length; i++){
     this.nomeFicheiros.push(ficheiros_selecionados[i].name);
     this.files.add(ficheiros_selecionados[i]);
    }
    document.getElementById('customFileLabel').innerHTML = this.nomeFicheiros.join(', ')
  }

  onUpload(){
    if(this.files && this.files.size > 0){
      this.service.upload(this.files, 'http://localhost:8000/uploads')
        .subscribe(res => {
          const obj = JSON.parse(res[0]);
          console.log(obj)

        })

    }
  }

}
