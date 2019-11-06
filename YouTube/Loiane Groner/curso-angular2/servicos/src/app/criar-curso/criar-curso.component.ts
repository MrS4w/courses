import { Component, OnInit } from '@angular/core';

import { CursosService } from '../cursos/cursos.service';

@Component({
  selector: 'app-criar-curso',
  templateUrl: './criar-curso.component.html',
  styleUrls: ['./criar-curso.component.scss']
})
export class CriarCursoComponent implements OnInit {
  cursos: string[] = [];

  constructor(private cursoService: CursosService) {}

  ngOnInit() {
    this.cursos = this.cursoService.getCursos();
  }

  onAddCurso(curso: string) {
    this.cursoService.addCurso(curso);
  }
}
