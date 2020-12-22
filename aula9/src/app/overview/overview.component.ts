import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import {AUTHORS} from '../authorslist';
import { Publisher } from '../publisher';
import {PUBLISHERS} from '../publisherslist';
import {AuthorService} from '../author.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})

export class OverviewComponent implements OnInit {
  authors: Author[];
  publishers: Publisher[];

  constructor(private authorService: AuthorService) {
    this.authors = AUTHORS.slice(0, 4);
    this.publishers = PUBLISHERS.slice(0, 4);
  }

  // tslint:disable-next-line:typedef
  ngOnInit(): void {
    this.getAuthors();
  }

  getAuthors(): void {
    this.authorService.getAuthorsN(4).subscribe(authors => this.authors = authors);
  }

}

