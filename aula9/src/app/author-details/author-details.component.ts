import {Component, Input, OnInit} from '@angular/core';
import { Author } from '../author';
import { AUTHORS } from '../authorslist';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-author-details',
  templateUrl: './author-details.component.html',
  styleUrls: ['./author-details.component.css']
})

export class AuthorDetailsComponent implements OnInit {
  @Input() author: Author;

  constructor(
    private route: ActivatedRoute,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.getAuthor();
  }

  getAuthor(): void {
    const num = +this.route.snapshot.paramMap.get('num');
    this.author = AUTHORS.find(author => author.num === num);
  }

  goBack(): void {
    this.location.back();
  }
}
