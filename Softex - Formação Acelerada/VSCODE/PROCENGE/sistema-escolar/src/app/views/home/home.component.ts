import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatTable } from '@angular/material/table';
import { ElementDialogComponent } from 'src/app/shared/element-dialog/element-dialog.component';

export interface CursosSoftex {
  position: number;
  nome: string;
  instrutor: string;
  local: string;
  cargaHoraria: number;
  dataInicio: string;
}

const ELEMENT_DATA: CursosSoftex[] = [
  {
    position: 1,
    nome: 'Angular',
    instrutor: 'Genival',
    local: 'Softex',
    cargaHoraria: 36,
    dataInicio: '03/02/2020',
  },
  {
    position: 2,
    nome: 'Java',
    instrutor: 'Genival',
    local: 'Softex',
    cargaHoraria: 60,
    dataInicio: '06/02/2020',
  },
];

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  @ViewChild(MatTable)
  table!: MatTable<any>;
  displayedColumns: string[] = [
    'position',
    'nome',
    'instrutor',
    'local',
    'cargaHoraria',
    'dataInicio',
    'actions',
  ];
  dataSource = ELEMENT_DATA;

  constructor(public dialog: MatDialog) {}

  ngOnInit(): void {}

  openDialog(element: CursosSoftex | null): void {
    const dialogRef = this.dialog.open(ElementDialogComponent, {
      data:
        element === null
          ? {
              position: null,
              nome: '',
              instrutor: '',
              local: '',
              cargaHoraria: null,
              dataInicio: null,
            }
          : {
              position: element.position,
              nome: element.nome,
              instrutor: element.instrutor,
              local: element.local,
              cargaHoraria: element.cargaHoraria,
              dataInicio: element.dataInicio,
            },
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result !== undefined) {
        if (this.dataSource.map((p) => p.position).includes(result.position)) {
          this.dataSource[result.position - 1] = result;
          this.table.renderRows();
        } else {
          this.dataSource.push(result);
          this.table.renderRows();
        }
      }
    });
  }

  editElement(element: CursosSoftex): void {
    this.openDialog(element);
  }

  deleteElement(position: number): void {
    this.dataSource = this.dataSource.filter((p) => p.position !== position);
  }
}
