
//! Delete lot button
const $deleteLotButton = $('.modify-delete')
$deleteLotButton.on('click', delete_request);

async function delete_request(e) {

  e.preventDefault();

  const path = window.location.pathname;
  var parts = path.split('/');
  var id = parseInt(parts[parts.length-2]);

  const dialog = confirm(`‼️ THIS ACTION IS NOT REVERSIBLE. Confirm delete?`);
  if (dialog) {
    await axios.delete(`/api/delete-lot/${id}`)
    window.location.assign('/')
  }
  else {
    console.log('crysis is avertled :)')
  }
};