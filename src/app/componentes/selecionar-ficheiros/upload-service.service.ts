import { HttpClient, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UploadServiceService {

  constructor(private http: HttpClient) { }

  upload(files: Set<File>, url: string){

    const formData = new FormData();
    files.forEach(file => formData.append('files', file, file.name ));

    // const request = new HttpRequest('POST', url, formData);
    // return this.http.request(request);
// OU

    return this.http.post(url, formData);

  }
}
