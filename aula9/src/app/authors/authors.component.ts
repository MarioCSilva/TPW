import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import { AUTHORS } from '../authorslist';
import {AuthorService} from '../author.service';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})

export class AuthorsComponent implements OnInit {
  authors: Author[];

  constructor(private authorService: AuthorService) {
    this.authors = AUTHORS;
  }

  // tslint:disable-next-line:typedef
  ngOnInit()  {
    this.getAuthors();
  }

  getAuthors(): void {
    this.authorService.getAuthors().subscribe(authors => this.authors = authors);
  }

}
