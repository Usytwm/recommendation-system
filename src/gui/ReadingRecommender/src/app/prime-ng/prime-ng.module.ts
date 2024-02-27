import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { InputGroupModule } from 'primeng/inputgroup';
import { InputGroupAddonModule } from 'primeng/inputgroupaddon';
import { TableModule } from 'primeng/table';

@NgModule({
  declarations: [],
  imports: [
    CommonModule

  ],
  exports: [
    ButtonModule,
    InputGroupAddonModule,
    InputGroupModule,
    TableModule
  ]
})
export class PrimeNgModule { }
