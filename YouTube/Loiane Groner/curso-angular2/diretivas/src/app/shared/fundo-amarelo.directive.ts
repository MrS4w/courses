import { Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive({
  selector: 'p[fundoAmarelo]'
})
export class FundoAmareloDirective {
  constructor(private elementRef: ElementRef, private renderer2: Renderer2) {
    // this.elementRef.nativeElement.style.backgroundColor = 'yellow';
    this.renderer2.setStyle(
      this.elementRef.nativeElement,
      'background-color',
      'yellow'
    );
  }
}
