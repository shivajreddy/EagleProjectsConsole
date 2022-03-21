
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
  console.log(response);

  if (!response.data) {
    $editor_fields.addClass("invisible");
  }
  else{
    $editor_fields.removeClass("invisible");
  }
};
check_editor();


