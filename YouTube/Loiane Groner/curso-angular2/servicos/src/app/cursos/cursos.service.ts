import { Injectable } from '@angular/core';

@Injectable()
export class CursosService {
  private cursos: string[] = ['Angular2', 'Java', 'Git'];

  constructor() {
    console.log('CursosService');
  }

  getCursos() {
    return this.cursos;
  }

  addCurso(curso: string) {
    this.cursos.push(curso);
  }
}
