import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DiretivaNgswitchComponent } from './diretiva-ngswitch.component';

describe('DiretivaNgswitchComponent', () => {
  let component: DiretivaNgswitchComponent;
  let fixture: ComponentFixture<DiretivaNgswitchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DiretivaNgswitchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DiretivaNgswitchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
