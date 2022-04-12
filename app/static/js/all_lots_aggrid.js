//? AG Grid script

const  today = new Date();

const prevWeekDate = new Date()
prevWeekDate.setDate(new Date().getDate() - 7)

function color_code(date_str){

  let date = new Date(date_str)
  // return [date, today]
  if (parseInt(date.getMonth()) >= parseInt(today.getMonth())){
    // console.log(today.getMonth(), date.getMonth())
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
]


//! Status Column
async function get_curr_usr() {
  const usr = await axios.get('/api/get-current-user');
  if (usr.data.editor){
    columnDefs.push(
      {headerName : '✎', field: 'edit', sortable:false, filter:false, width:50, pinned:'left', cellClass:['editor-only'],headerTooltip:'Edit Lot',
      cellRenderer: params => {
        return `<a type="button" class="modify-lot" data-id="${params.data.id}" href="/lot/edit/${params.data.id}"><i class="bi bi-pencil-fill"></i></a>`;
      }
    },
      {headerName : '✔️', field: 'finished', sortable:false, filter:false, width:80, pinned:'left', cellClass:['editor-only'], headerTooltip:'Finished Status', sortable:true, filter:true, },
      )
    }
  
  columnDefs.push(
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
        // console.log(color_code(params.value), params.value)
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
      {headerName : 'Actual', field: 'actual', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Actual Finished Date', width:120,  },
      {headerName : 'Time', field: 'time', sortable:true, filter:true, columnGroupShow:'open', headerTooltip:'Total Time in minutes', width:120, },
    ],
  },
  
  //! Engineering
  {
    headerName: 'Engineering',
    children:
    [
      {headerName : 'Engineering', field: 'eng', sortable:true, filter:true, headerTooltip:'Engineering Name',  },
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
  )
}
get_curr_usr();

// const rowDefs = [];

const gridOptions = {
  columnDefs : columnDefs,
  // rowData : rowDefs,
  rowSelection : 'multiple',
  domLayout: 'autoHeight',

  tooltipShowDelay:0,
  tooltipHideDelay: 2000,

  defaultColDef: {
    width: 150,
    editable: false,
    filter: 'agTextColumnFilter',
    floatingFilter: true,
    resizable: false,
    lockPosition: true,
  },
  // pagination: true,
  // paginationPageSize: 20,

}

//! AJAX CALL TO GET THE LOTS
async function get_lots(){
  console.log("xxxxxxxxxxx ASYNC FUNCTION STARTED xxxxxxxxx")
  
  const result = await axios.get('/api/get-all-lots')

  gridOptions.rowData = result.data
  // for (const lot of result.data){
  //   rowDefs.push(lot);
  // }

  // gridOptions.api is undefined because it has to be called only after the grid is ready
  // console.log("this is api", gridOptions.api );
  // for (const lot of result.data){
  //   gridOptions.api.setRowData([lot])
  // }

  const lotGrid = document.querySelector('#all-lotGrid');
  new agGrid.Grid(lotGrid, gridOptions);
  
  // remove loading spinner
  const spinner = document.getElementById('home-spinner');
  spinner.parentNode.removeChild(spinner);
  
  console.log("----------- ASYNC FUNCTION END -------------")
}

get_lots()
// Make AJAX call only on home page
// if (document.domain == '127.0.0.1' ){
//   get_lots()
// }


//! Save as CSV
const $print_table = $('#print-table')
$print_table.on('click', function (e){
  e.preventDefault();
  gridOptions.api.exportDataAsCsv();
});