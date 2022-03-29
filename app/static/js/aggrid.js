//? AG Grid script

var columnDefs = [
  //* Lot info
  {headerName : 'Edit', field: 'edit', sortable:false, filter:false, width:70, pinned:'left'},
  {headerName : '✅.', field: 'finished', sortable:false, filter:false, width:50, pinned:'left'},
  {headerName : 'Community', field: 'community', sortable:true, filter:true},
  {headerName : 'Section', field: 'section', sortable:true, filter:true},
  {headerName : 'Lot-Number', field: 'lot_number', sortable:true, filter:true},
  {headerName : 'Product', field: 'product', sortable:true, filter:true},
  {headerName : 'Elevation', field: 'elevation', sortable:true, filter:true},
  {headerName : 'Contract-Date', field: 'contract_date', sortable:true, filter:true},
  
  //* Drafting
  {headerName : 'Assigned To', field: 'assigned', sortable:true, filter:true},
  {headerName : 'Draft Deadline', field: 'draft_deadline', sortable:true, filter:true},
  {headerName : 'Actual', field: 'actual', sortable:true, filter:true},
  {headerName : 'Time', field: 'time', sortable:true, filter:true},
  
  //* Engineering
  {headerName : 'Engineering', field: 'eng', sortable:true, filter:true},
  {headerName : 'Eng. Sent', field: 'eng_sent', sortable:true, filter:true},
  {headerName : 'Eng. Planned Receipt', field: 'eng_planned_receipt', sortable:true, filter:true},
  {headerName : 'Eng. Actual Receipt', field: 'eng_actual_receipt', sortable:true, filter:true},
  
  //* Plat
  {headerName : 'Plat Engineering', field: 'plat_eng', sortable:true, filter:true},
  {headerName : 'Plat Sent', field: 'plat_sent', sortable:true, filter:true},
  {headerName : 'Plat Planned Receipt', field: 'plat_planned_receipt', sortable:true, filter:true},
  {headerName : 'Plat Actual Receipt', field: 'plat_actual_receipt', sortable:true, filter:true},
  
  //* Permit
  {headerName : 'Permit Jurisdiction', field: 'permit_jurisdiction', sortable:true, filter:true},
  {headerName : 'Permit Planned Submit', field: 'permit_planned_submit', sortable:true, filter:true},
  {headerName : 'Permit Actual Submit', field: 'permit_actual_submit', sortable:true, filter:true},
  {headerName : 'Permit Received', field: 'permit_received', sortable:true, filter:true},
  
  //* BBP
  {headerName : 'BBP Planned Posted', field: 'bbp_planned_posted', sortable:true, filter:true},
  {headerName : 'BBP Actual Posted', field: 'bbp_actual_posted', sortable:true, filter:true},
  
  //* Notes
  {headerName : 'Notes', field: 'notes', sortable:true, filter:true},

]

var rowDefs = [
  {community : 'Row1', section : 's1', lot_number : 'l1', product: 'p1', elevation:'e1', contract_date:'date1'},
  {community : 'Roww', section : 's2', lot_number : 'l2', product: 'p2', elevation:'e2', contract_date:'date2'},
]

var gridOptions = {
  columnDefs : columnDefs,
  rowData : rowDefs,
  rowSelection : 'multiple'
}

const lotGrid = document.querySelector('#lotGrid');

new agGrid.Grid(lotGrid, gridOptions);


fetch('/api/get-lots')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    gridOptions.api.setRowData(data);
  })

