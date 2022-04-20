// console.log("scripts file starts");
//! Modify button for each lot on homepage
$modifyButton = $('.modify');
$modifyButton.on('click', (e)=>{
  e.preventDefault();

  let id = parseInt($(e.currentTarget).attr("data-id"));

  window.location.href = `/lot/edit/${id}`;
});
  
//? for some reason, JS events are not coming until here, they are going to what ever href says for the anchor button
// const $modifyLotButton = $('.modify-lot');
// $modifyLotButton.on('click', (e)=>{
//   e.preventDefault();
//   console.log("fired");

//   let id = parseInt($(e.currentTarget).attr("data-id"));

//   window.location.href = `/lot/edit/${id}`;
// });


