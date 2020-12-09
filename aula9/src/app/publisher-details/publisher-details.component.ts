import { Component, Input, OnInit } from '@angular/core';
import { Publisher } from '../publisher';
import { PUBLISHERS } from '../publisherslist';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import {Author} from '../author';
import {AUTHORS} from '../authorslist';

@Component({
  selector: 'app-publisher-details',
  templateUrl: './publisher-details.component.html',
  styleUrls: ['./publisher-details.component.css']
})
export class PublisherDetailsComponent implements OnInit {
  @Input() publisher: Publisher;

  constructor(
    private route: ActivatedRoute,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.getPublisher();
  }

  getPublisher(): void {
    const num = +this.route.snapshot.paramMap.get('num');
    this.publisher = PUBLISHERS.find(publisher => publisher.num === num);
  }

  goBack(): void {
    this.location.back();
  }

}
