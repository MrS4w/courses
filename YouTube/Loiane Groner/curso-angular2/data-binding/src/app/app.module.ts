import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { DataBindingComponent } from './data-binding/data-binding.component';
import { MeuFormModule } from './meu-form/meu-form.module';


@NgModule({
  declarations: [AppComponent, DataBindingComponent],
  imports: [BrowserModule, FormsModule, MeuFormModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
