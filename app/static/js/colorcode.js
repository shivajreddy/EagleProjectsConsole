
const  today = new Date();

const prevWeekDate = new Date()
prevWeekDate.setDate(new Date().getDate() - 7)

// console.log(today,prevWeekDate)

// var dd = String(today.getDate()).padStart(2, '0');
// var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
// var yyyy = today.getFullYear();
// today = mm + '/' + dd + '/' + yyyy;


const $mydate = $('#mydate')

const $draft_deadline = $('.draft_deadline');

$mydate.text(`${today}`)

$('.draft_deadline').each(function(){
  
  const date_str = $(this).text().trimRight().trimLeft()
  // console.log(date_str);
  let date = new Date(date_str);
    
  const ds = date.toUTCString()
  // console.log(date,today);

  if (date > today){
    $(this).addClass('late_1')
  }
  // console.log(ds);
});

