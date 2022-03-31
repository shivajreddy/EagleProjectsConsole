//? AG Grid script

const  today = new Date();

const prevWeekDate = new Date()
prevWeekDate.setDate(new Date().getDate() - 7)

function color_code(date_str){

  let date = new Date(date_str)
  // return [date, today]
  if (parseInt(date.getMonth()) >= parseInt(today.getMonth())){
    console.log(today.getMonth(), date.getMonth())
    return "late_3"
  }
  // if (date >= prevWeekDate){
  //   return "late_2"
  // }
  else{
    return "late_1"
  }

}

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
      {headerName : 'Community', field: 'community', sortable:true, filter:true, headerTooltip:'Community', pinned:'left', },
      {headerName : 'Section', field: 'section', sortable:true, filter:true, headerTooltip:'Section', width:80, pinned:'left', },
      {headerName : 'Lot-Number', field: 'lot_number', sortable:true, filter:true, headerTooltip:'Lot-Number', width:80, pinned:'left', 
        cellStyle: params => {
          if (params.value > 10){
            return {color: 'white', backgroundColor : 'green'}
          }
        }
      },
      {headerName : 'Product', field: 'product', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Product', pinned:'left', },
      {headerName : 'Elevation', field: 'elevation', sortable:true, filter:true, columnGroupShow: 'open', headerTooltip:'Elevation', pinned:'left', },
      {headerName : 'Contract-Date', field: 'contract_date', sortable:true, filter:true, columnGroupShow: 'open', headerTooltip:'Contract-Date', width:120, pinned:'left', 
      cellClass: params => {
        console.log(color_code(params.value), params.value)
        return color_code(params)
        // return params.value > today ? 'late_1' : 'late_2';
      }},
    ],
  },
  
  //! Drafting
  {
    headerName: 'Drafting',
    children:
    [
      {headerName : 'Assigned To', field: 'assigned', sortable:true, filter:true, headerTooltip:'Drafter Name',width:100, },
      {headerName : 'Draft Deadline', field: 'draft_deadline', sortable:true, filter:true, headerTooltip:'Drafting-Deadline Date', width:120, },
      {headerName : 'Actual', field: 'actual', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Actual Finished Date', width:120, },
      {headerName : 'Time', field: 'time', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Total Time in minutes', width:120, },
    ],
  },
  
  //! Engineering
  {
    headerName: 'Engineering',
    children:
    [
      {headerName : 'Engineering', field: 'eng', sortable:true, filter:true, headerTooltip:'Engineering Name', },
      {headerName : 'Eng. Sent', field: 'eng_sent', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Engineering Sent Date', width:120, },
      {headerName : 'Eng. Planned Receipt', field: 'eng_planned_receipt', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Engineering Planned Receipt Date', width:120, },
      {headerName : 'Eng. Actual Receipt', field: 'eng_actual_receipt', sortable:true, filter:true, headerTooltip:'Engineering Actual Receipt Date', width:120, },
    ]
  },
  
  //! Plat
  {
    headerName: 'Plat',
    children:
    [
      {headerName : 'Plat Engineering', field: 'plat_eng', sortable:true, filter:true, headerTooltip:'Plat Engineering Name', },
      {headerName : 'Plat Sent', field: 'plat_sent', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Plat Sent Date', width:120, },
      {headerName : 'Plat Planned Receipt', field: 'plat_planned_receipt', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Plat Planned Receipt Date', width:120, },
      {headerName : 'Plat Actual Receipt', field: 'plat_actual_receipt', sortable:true, filter:true, headerTooltip:'Plat Actual Receipt Date', width:120, },
    ]
  },
  
  //! Permit
  {
    headerName: 'Permit',
    children:
    [
      {headerName : 'Permit Jurisdiction', field: 'permit_jurisdiction', sortable:true, filter:true, headerTooltip:'Jurisdiction Name', },
      {headerName : 'Permit Planned Submit', field: 'permit_planned_submit', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Permit Planned Submit Date', width:120, },
      {headerName : 'Permit Actual Submit', field: 'permit_actual_submit', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Permit Actual Submit Date', width:120, },
      {headerName : 'Permit Received', field: 'permit_received', sortable:true, filter:true, headerTooltip:'Permit Received Date', width:120, },
    ]
  },
  
  //! BBP
  {
    headerName: 'BBP',
    children:
    [
      {headerName : 'BBP Planned Posted', field: 'bbp_planned_posted', sortable:true, filter:true, headerTooltip:'BBP Planned Posted Date', width:120, },
      {headerName : 'BBP Actual Posted', field: 'bbp_actual_posted', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'BBP Actual Posted Date', width:120, },
    ]
  },

  //! Notes
  {
    headerName: 'Notes',
    children:
    [
      {headerName : 'Notes', field: 'notes', sortable:true, filter:true, headerTooltip:'Extra notes', width:400, },
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

fetch('/api/get-lots')
  .then(response => response.json())
  .then(data => {
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
      domLayout: 'autoHeight',

      tooltipShowDelay:0,
      tooltipHideDelay: 2000,

      defaultColDef: {
        width: 150,
        editable: false,
        filter: 'agTextColumnFilter',
        floatingFilter: true,
        // resizable: false,
        // lockPosition: true,
      },
    }

    const lotGrid = document.querySelector('#lotGrid');
    new agGrid.Grid(lotGrid, gridOptions);
    
    //* Auto - size columns
    // const allColumnIds = [];
    // gridOptions.columnApi.getAllColumns().forEach((column) => {
    //   allColumnIds.push(column.getId());
    // })
    // gridOptions.columnApi.autoSizeColumns(allColumnIds, true);

    //! Save as CSV
    const $print_table = $('#print-table')
    $print_table.on('click', function (e){
      e.preventDefault();
      gridOptions.api.exportDataAsCsv();
    });

  })

