
//! Delete lot button
const $deleteLotButton = $('.modify-delete')

$deleteLotButton.on('click', delete_request);

// $deleteLotButton.on('click', (e) => {
//   e.preventDefault();

//   const path = window.location.pathname;
//   var parts = path.split("/");
//   var id = parseInt(parts[parts.length - 2]);

//   const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE. Confirm delete?`);
//   if (dialog) {
//     window.location.href = `/lot/delete/${id}`;
//   }
//   else {
//     console.log("crysis averted");
//   }
// });

async function delete_request(e) {

  e.preventDefault();

  const path = window.location.pathname;
  var parts = path.split('/');
  var id = parseInt(parts[parts.length-2]);

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE. Confirm delete?`);
  if (dialog) {
    const res = await axios.delete(`/api/delete-lot/${id}`)
    console.log(res)
    if (res){
      console.log(res);
      window.location.assign("/");
    }
  }
  else {
    console.log('crysis is avertled :)')
  }
};