import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LogService {
  constructor() {}

  consoleLog(msg: string) {
    console.log(msg);
  }
}
