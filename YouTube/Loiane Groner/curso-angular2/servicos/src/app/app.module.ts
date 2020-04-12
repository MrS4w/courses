import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CriarCursoModule } from './criar-curso/criar-curso.module';
import { CursosComponent } from './cursos/cursos.component';
import { CursosService } from './cursos/cursos.service';
import { LogService } from './shared/log.service';

@NgModule({
  declarations: [AppComponent, CursosComponent],
  imports: [BrowserModule, CriarCursoModule],
  providers: [CursosService, LogService],
  bootstrap: [AppComponent],
})
export class AppModule {}
