console.log("problem came here?");
//! Show user-role based content
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