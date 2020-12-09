import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthorsComponent } from './authors/authors.component';
import { PublishersComponent } from './publishers/publishers.component';
import { OverviewComponent } from './overview/overview.component';
import { AuthorDetailsComponent } from './author-details/author-details.component';
import { PublisherDetailsComponent } from './publisher-details/publisher-details.component';

const routes: Routes = [
  { path: 'authors', component: AuthorsComponent },
  { path: 'publishers', component: PublishersComponent },
  { path: 'overview', component: OverviewComponent },
  { path: 'authordetails/:num', component: AuthorDetailsComponent },
  { path: 'publisherdetails/:num', component: PublisherDetailsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
