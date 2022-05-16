//? AG Grid script for homepage showing unfinished lots

var toastTrigger = document.getElementById('liveToastBtn')
var toastLiveExample = document.getElementById('liveToast')
// var toastLiveExample = document.getElementsByClassName('legendbtn');
if (toastTrigger) {
  toastTrigger.addEventListener('click', function () {
    var toast = new bootstrap.Toast(toastLiveExample)

    toast.show()
  })
}

//! Color Coding the dates Feature ----- START
const today = new Date();
const prevWeekDate = new Date();
prevWeekDate.setDate(new Date().getDate() - 7);

// styles represent the urgency. 1 being less urgent, 3 being most urgent
const style_1 = { color: 'black', backgroundColor: '#a2d2ff' }  //bg blue. dist >= 11
const style_2 = { color: 'black', backgroundColor: '#99d98c' }  //bg green. 6<=dist<=10 purple
const style_3 = { color: 'black', backgroundColor: '#ffb703' }  //bg yellow. 3<=dist<=5 green
const style_4 = { color: 'white', backgroundColor: '#e85d04' }  //bg Orange. 1<=dist<=2 yellow
const style_5 = { color: 'white', backgroundColor: '#dc2f02' }  //bg dark-orange. dist==0 orange
const style_6 = { color: 'white', backgroundColor: '#d00000' }  //bg red. dist < 0 red
const style_none = { color: 'black' }  // No Style

// based on the given date_str return the style_n object
function color_code(date_str) {
  let curr_date = create_date(date_str);
  let today = new Date();
  let diff = curr_date.getTime() - today.getTime();
  let mins = 1000 * 3600 * 24;
  let diff_days = diff / mins;

  if (diff_days >= 11) {
    return style_1
  }
  if (6 <= diff_days) {
    return style_2
  }
  if (3 <= diff_days) {
    return style_3
  }
  if (1 <= diff_days) {
    return style_4
  }
  if (0 <= diff_days) {
    return style_5
  }
  if (diff_days < 0) {
    return style_6
  }
  return style_none
}

//? Calculate next N'th work date from given Date
// Helper function to create actual date object from string
function create_date(str_date) {
  const splitted = str_date.split('-')
  const year = parseInt(splitted[0])
  const month = parseInt(splitted[1] - 1)   // for some weird reason month is being set to given+1, so setting it as -1
  const date = parseInt(splitted[2])
  let today = new Date();
  today.setYear(year);
  today.setMonth(month);
  today.setDate(date);
  return today;
}

// starting from the next day of given day, return the nth working day
function calc_work_date(from_date_str, no_of_days) {
  let to_date = create_date(from_date_str);
  while (no_of_days > 0) {
    to_date.setDate(to_date.getDate() + 1)

    if (to_date.getDay() != 0 && to_date.getDay() != 6) {
      no_of_days--;
    }
  }
  return to_date;
}
//! Color Coding the dates Feature ------ END



//! AG GRID ------ START
var columnDefs = [
]


//! Status Column
async function get_curr_usr() {
  const usr = await axios.get('/api/get-current-user');
  if (usr.data.editor) {
    columnDefs.push(
      {
        headerName: '✎', field: 'edit', sortable: false, filter: false, width: 50, pinned: 'left', cellClass: ['editor-only'], headerTooltip: 'Edit Lot',
        cellRenderer: params => {
          return `<a type="button" class="modify-lot" data-id="${params.data.id}" href="/lot/edit/${params.data.id}"><i class="bi bi-pencil-fill"></i></a>`;
        }
      },
      // {headerName : '✔️', field: 'finished', sortable:false, filter:false, width:50, pinned:'left', cellClass:['editor-only'], headerTooltip:'Finished Status', },
    )
  }

  columnDefs.push(
    //! Lot info
    {
      headerName: 'Lot Info',
      children:
        [
          { headerName: 'Community', field: 'community', sortable: true, filter: true, headerTooltip: 'Community', pinned: 'left', },
          { headerName: 'Section', field: 'section', sortable: true, filter: true, headerTooltip: 'Section', width: 80, pinned: 'left', },
          { headerName: 'Lot-Number', field: 'lot_number', sortable: true, filter: true, headerTooltip: 'Lot-Number', width: 80, pinned: 'left', },
          { headerName: 'Contract-Date', field: 'contract_date', sortable: true, filter: true, headerTooltip: 'Contract-Date', width: 120, pinned: 'left', },
          { headerName: 'Product', field: 'product', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Product', pinned: 'left', },
          { headerName: 'Elevation', field: 'elevation', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Elevation', pinned: 'left', },
        ],
    },

    //! Drafting
    {
      headerName: 'Drafting',
      children:
        [
          { headerName: 'Assigned To', field: 'assigned', sortable: true, filter: true, headerTooltip: 'Drafter Name', width: 100, },
          {
            headerName: 'Draft Deadline', field: 'draft_deadline', sortable: true, filter: true, headerTooltip: 'Drafting-Deadline Date', width: 120,
            cellStyle: params => {
              if (params.data.actual === "None" || params.data.actual === "") {
                return color_code(params.value)
              }
              else {
                return style_none
              }
            }
          },
          { headerName: 'Actual', field: 'actual', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Actual Finished Date', width: 120, },
          { headerName: 'Time', field: 'time', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Total Time in minutes', width: 120, },
        ],
    },

    //! Engineering
    {
      headerName: 'Engineering',
      children:
        [
          { headerName: 'Engineering', field: 'eng', sortable: true, filter: true, headerTooltip: 'Engineering Name', },
          { headerName: 'Eng. Sent', field: 'eng_sent', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Engineering Sent Date', width: 120, },
          {
            headerName: 'Eng. Planned Receipt', field: 'eng_planned_receipt', sortable: true, filter: true, headerTooltip: 'Engineering Planned Receipt Date', width: 120,
            cellStyle: params => {
              if (params.data.eng_actual_receipt === "None" || params.data.eng_actual_receipt === "") {
                return color_code(params.value)
              }
              else {
                return style_none
              }
            }
          },
          { headerName: 'Eng. Actual Receipt', field: 'eng_actual_receipt', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Engineering Actual Receipt Date', width: 120, },
        ]
    },

    //! Plat
    {
      headerName: 'Plat',
      children:
        [
          { headerName: 'Plat Engineering', field: 'plat_eng', sortable: true, filter: true, headerTooltip: 'Plat Engineering Name', },
          { headerName: 'Plat Sent', field: 'plat_sent', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Plat Sent Date', width: 120, },
          {
            headerName: 'Plat Planned Receipt', field: 'plat_planned_receipt', sortable: true, filter: true, headerTooltip: 'Plat Planned Receipt Date', width: 120,
            cellStyle: params => {
              if (params.data.plat_actual_receipt === "None" || params.data.plat_actual_receipt === "") {
                return color_code(params.value)
              }
              else {
                return style_none
              }
            }
          },
          { headerName: 'Plat Actual Receipt', field: 'plat_actual_receipt', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Plat Actual Receipt Date', width: 120, },
        ]
    },

    //! Permit
    {
      headerName: 'Permit',
      children:
        [
          { headerName: 'Permit Jurisdiction', field: 'permit_jurisdiction', sortable: true, filter: true, headerTooltip: 'Jurisdiction Name', },
          {
            headerName: 'Permit Planned Submit', field: 'permit_planned_submit', sortable: true, filter: true, headerTooltip: 'Permit Planned Submit Date', width: 120,
            cellStyle: params => {
              if (params.data.permit_actual_submit === "None" || params.data.permit_actual_submit === "") {
                return color_code(params.value)
              }
              else {
                return style_none
              }
            }
          },
          { headerName: 'Permit Actual Submit', field: 'permit_actual_submit', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Permit Actual Submit Date', width: 120, },
          { headerName: 'Permit Received', field: 'permit_received', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'Permit Received Date', width: 120, },
        ]
    },

    //! BBP
    {
      headerName: 'BBP',
      children:
        [
          {
            headerName: 'BBP Planned Posted', field: 'bbp_planned_posted', sortable: true, filter: true, headerTooltip: 'BBP Planned Posted Date', width: 120,
            cellStyle: params => {
              if (params.data.bbp_actual_posted === "None" || params.data.bbp_actual_posted === "") {
                return color_code(params.value)
              }
              else {
                return style_none
              }
            }
          },
          { headerName: 'BBP Actual Posted', field: 'bbp_actual_posted', sortable: true, filter: true, columnGroupShow: 'open', headerTooltip: 'BBP Actual Posted Date', width: 120, },
        ]
    },

    //! Notes
    {
      headerName: 'Notes',
      children:
        [
          { headerName: 'Notes', field: 'notes', sortable: true, filter: true, headerTooltip: 'Extra notes', width: 400, },
        ]
    },
  )
}
get_curr_usr();

// const rowDefs = [];

const gridOptions = {
  columnDefs: columnDefs,
  // rowData : rowDefs,
  rowSelection: 'multiple',
  domLayout: 'autoHeight',

  tooltipShowDelay: 0,
  tooltipHideDelay: 2000,

  defaultColDef: {
    width: 150,
    editable: false,
    // filter: 'agTextColumnFilter',
    floatingFilter: true,
    resizable: false,
    lockPosition: true, //ability to drag the columns
  },
  // pagination: true,
  // paginationPageSize: 20,

}

//! AJAX CALL TO GET THE LOTS
async function get_lots() {
  // console.info("xxxxxxxxxxx ASYNC FUNCTION STARTED xxxxxxxxx")

  const result = await axios.get('/api/get-lots')

  gridOptions.rowData = result.data;

  const lotGrid = document.querySelector('#lotGrid');
  new agGrid.Grid(lotGrid, gridOptions);

  // remove loading spinner
  const spinner = document.getElementById('home-spinner');
  spinner.parentNode.removeChild(spinner);

  // console.info("----------- ASYNC FUNCTION END -------------")
  //! Remove color for the not needed
  // remove_color_code(gridOptions.rowData);
}

get_lots()


//! Save as CSV
const $print_table = $('#print-table')
$print_table.on('click', function (e) {
  e.preventDefault();
  gridOptions.api.exportDataAsCsv();
});
