import { Injectable, EventEmitter } from '@angular/core';

@Injectable()
export class CursosService {
  emitirCusoCriado = new EventEmitter<string>();
  static criouNovoCurso = new EventEmitter<string>();

  private cursos: string[] = ['Angular2', 'Java', 'Git'];

  constructor() {
    console.log('CursosService');
  }

  getCursos() {
    return this.cursos;
  }

  addCurso(curso: string) {
    this.cursos.push(curso);
    this.emitirCusoCriado.emit(curso);
    CursosService.criouNovoCurso.emit(curso);
  }
}
