// const { default: jsPDF } = require("jspdf");

//! Modify button for each lot on homepage
$modifyButton = $('.modify');
$modifyButton.on('click', (e)=>{
  e.preventDefault();
  const t = e.target.parentElement;
  const id = parseInt(t.nextElementSibling.innerText);
  window.location.href = `/lot/edit/${id}`;
});


$user_link = $('#user_link')
$user_link.on('click', (e) => {
  // e.preventDefault();
  console.log("This link is pressed");
});

//! Delete lot button
$deleteLotButton = $('.modify-delete')
$deleteLotButton.on('click', (e) =>{
  e.preventDefault();

  const path = window.location.pathname;
  var parts = path.split("/");
  var id = parseInt(parts[parts.length - 2]);

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE. Confirm delete?`);
  if (dialog) {
    window.location.href = `/lot/delete/${id}`;
  }
  else {
    console.log("crysis averted");
  }
});


//* Make an axios request to check if user is editor
const $editor_fields = $('.editor-only')
async function check_editor() {

  const response = await axios.get('/check-editor');

  if (response.data === true) {
    $editor_fields.removeClass("invisible");
  }
  else{
    $editor_fields.addClass("invisible");
  }

};
check_editor();


function generate() {
  var doc = new jsPDF('p', 'pt', 'letter');
  var htmlstring = '';
  var tempVarToCheckPageHeight = 0;
  var pageHeight = 0;
  pageHeight = doc.internal.pageSize.height;
  specialElementHandlers = {
      // element with id of "bypass" - jQuery style selector  
      '#bypassme': function (element, renderer) {
          // true = "handled elsewhere, bypass text extraction"  
          return true
      }
  };
  margins = {
      top: 150,
      bottom: 60,
      left: 40,
      right: 40,
      width: 600
  };
  var y = 20;
  doc.setLineWidth(2);
  doc.text(200, y = y + 30, "All Lots");
  doc.autoTable({
      html: '#main-lots-table',
      startY: 70,
      theme: 'grid',
      // columnStyles: {
      //     0: {
      //         cellWidth: 180,
      //     },
      //     1: {
      //         cellWidth: 180,
      //     },
      //     2: {
      //         cellWidth: 180,
      //     }
      // },
      // styles: {
      //     minCellHeight: 40
      // }
  })
  doc.save('All_lots.pdf');
}

//! Download table into PDF
const $print_table = $('#print-table')
$print_table.on('click', function (e){
  e.preventDefault();

  // download pdf
  console.log("STARTING FUNCTION");
  generate()



});

