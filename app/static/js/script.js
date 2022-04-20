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