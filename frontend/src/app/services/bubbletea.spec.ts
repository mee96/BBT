import { TestBed } from '@angular/core/testing';

import { Bubbletea } from './bubbletea';

describe('Bubbletea', () => {
  let service: Bubbletea;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Bubbletea);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
