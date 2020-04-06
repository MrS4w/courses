import { Component, OnInit } from '@angular/core';

import { CursosService } from './cursos.service';

@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.scss']
})
export class CursosComponent implements OnInit {
  cursos: string[] = [];
  // cursoService: CursosService;

  constructor(private cursoService: CursosService) {
    // this.cursoService = new CursosService();
    // this.cursoService = _cursoService;
  }

  ngOnInit() {
    this.cursos = this.cursoService.getCursos();

    CursosService.criouNovoCurso.subscribe(curso => console.log(curso));
  }
}
