import { Component, OnInit } from '@angular/core';
import { Author } from '../author';
import { AUTHORS } from '../authorslist';

@Component({
  selector: 'app-authors',
  templateUrl: './authors.component.html',
  styleUrls: ['./authors.component.css']
})

export class AuthorsComponent implements OnInit {

  authors: Author[];
  selectedAuthor: Author;

  constructor() {
    this.authors = AUTHORS;
  }

  onSelect(author: Author): void {
    this.selectedAuthor = author;
  }

  ngOnInit() {
  }

}
