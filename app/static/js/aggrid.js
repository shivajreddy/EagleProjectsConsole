//? AG Grid script

var columnDefs = [

  //! Status Column
  {
    headerName: 'Status',
    children :
    [
      {headerName : 'Edit', field: 'edit', sortable:false, filter:false, width:70, pinned:'left', cellClass:'editor-only'},
      {headerName : '✅.', field: 'finished', sortable:false, filter:false, width:50, pinned:'left', cellClass: 'editor-only'},
    ]
  },

  //! Lot info
  {
    headerName: 'Lot Info',
    children: 
    [
      {headerName : 'Community', field: 'community', sortable:true, filter:true},
      {headerName : 'Section', field: 'section', sortable:true, filter:true},
      {headerName : 'Lot-Number', field: 'lot_number', sortable:true, filter:true,
        cellStyle: params => {
          if (params.value > 10){
            return {color: 'white', backgroundColor : 'green'}
          }
        }
      },
      {headerName : 'Product', field: 'product', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Elevation', field: 'elevation', sortable:true, filter:true, columnGroupShow: 'open'},
      {headerName : 'Contract-Date', field: 'contract_date', sortable:true, filter:true, columnGroupShow: 'open',
      cellClass: params => {
        return params.value > today ? 'late_1' : 'late_2';
      }},
    ]
  },
  
  //! Drafting
  {
    headerName: 'Drafting',
    children:
    [
      {headerName : 'Assigned To', field: 'assigned', sortable:true, filter:true, resizable: true},
      {headerName : 'Draft Deadline', field: 'draft_deadline', sortable:true, filter:true},
      {headerName : 'Actual', field: 'actual', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Time', field: 'time', sortable:true, filter:true, columnGroupShow:'open'},
    ],
  },
  
  //! Engineering
  {
    headerName: 'Engineering',
    children:
    [
      {headerName : 'Engineering', field: 'eng', sortable:true, filter:true},
      {headerName : 'Eng. Sent', field: 'eng_sent', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Eng. Planned Receipt', field: 'eng_planned_receipt', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Eng. Actual Receipt', field: 'eng_actual_receipt', sortable:true, filter:true},
    ]
  },
  
  //! Plat
  {
    headerName: 'Plat',
    children:
    [
      {headerName : 'Plat Engineering', field: 'plat_eng', sortable:true, filter:true},
      {headerName : 'Plat Sent', field: 'plat_sent', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Plat Planned Receipt', field: 'plat_planned_receipt', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Plat Actual Receipt', field: 'plat_actual_receipt', sortable:true, filter:true},
    ]
  },
  
  //! Permit
  {
    headerName: 'Permit',
    children:
    [
      {headerName : 'Permit Jurisdiction', field: 'permit_jurisdiction', sortable:true, filter:true},
      {headerName : 'Permit Planned Submit', field: 'permit_planned_submit', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Permit Actual Submit', field: 'permit_actual_submit', sortable:true, filter:true, columnGroupShow:'open'},
      {headerName : 'Permit Received', field: 'permit_received', sortable:true, filter:true},
    ]
  },
  
  //! BBP
  {
    headerName: 'BBP',
    children:
    [
      {headerName : 'BBP Planned Posted', field: 'bbp_planned_posted', sortable:true, filter:true},
      {headerName : 'BBP Actual Posted', field: 'bbp_actual_posted', sortable:true, filter:true, columnGroupShow:'open'},
    ]
  },

  //! Notes
  {
    headerName: 'Notes',
    children:
    [
      {headerName : 'Notes', field: 'notes', sortable:true, filter:true},
    ]
  },
]

var rowDefs = [
  // {community : 'Row1', section : 's1', lot_number : 'l1', product: 'p1', elevation:'e1', contract_date:'date1'},
  // {community : 'Roww', section : 's2', lot_number : 'l2', product: 'p2', elevation:'e2', contract_date:'date2'},
]

function cellClass(params){
  return params.value >= 10 ? '.late_1' : '.late_2';
}

fetch('/api/get-lots').then(response => response.json()
  ).then(data => {
    for (const lot_data of data){
      
      const currentRow = {}
      for (const k of Object.keys(lot_data.lot_info)) {
        currentRow[k] = lot_data.lot_info[k]
      }
      for (const k of Object.keys(lot_data.drafting)) {
        currentRow[k] = lot_data.drafting[k]
      }
      for (const k of Object.keys(lot_data.engineering)) {
        currentRow[k] = lot_data.engineering[k]
      }
      for (const k of Object.keys(lot_data.plat)) {
        currentRow[k] = lot_data.plat[k]
      }
      for (const k of Object.keys(lot_data.permit)) {
        currentRow[k] = lot_data.permit[k]
      }
      for (const k of Object.keys(lot_data.bbp)) {
        currentRow[k] = lot_data.bbp[k]
      }
      for (const k of Object.keys(lot_data.notes)) {
        currentRow[k] = lot_data.notes[k]
      }

      rowDefs.push(currentRow)
    }
  }).then(()=>{

    var gridOptions = {
      columnDefs : columnDefs,
      rowData : rowDefs,
      rowSelection : 'multiple',
      domLayout: 'autoHeight'
    }
    
    const lotGrid = document.querySelector('#lotGrid');
    new agGrid.Grid(lotGrid, gridOptions);

  })
