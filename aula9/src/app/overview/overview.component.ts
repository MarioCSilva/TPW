import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import {AUTHORS} from '../authorslist';
import { Publisher } from '../publisher';
import {PUBLISHERS} from '../publisherslist';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})

export class OverviewComponent implements OnInit {
  authors: Author[];
  publishers: Publisher[];

  constructor() {
    this.authors = AUTHORS.slice(0, 4);
    this.publishers = PUBLISHERS.slice(0, 4);
  }

  // tslint:disable-next-line:typedef
  ngOnInit() { }

}

