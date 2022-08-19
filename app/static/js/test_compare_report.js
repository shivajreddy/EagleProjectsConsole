var $file1_input, $file2_input;

function validate_for_xlsm_type(filename) {
  const arr = filename.split(".");
  const file_ext = arr[arr.length - 1];
  if (file_ext === "xlsm" || file_ext === "XLSM") {
    return true;
  }
  return false;
}

$(document).ready(function () {
  $file1_input = $("#file-1");
  $file2_input = $("#file-2");

  const upload_button = $("#files-upload");
  upload_button.on("click", function (e) {
    e.preventDefault();

    var xhr;

    // const message = "Upload process started ";
    // console.log(`%c ${message}`, "color: orange");

    var file1_actual = $file1_input[0].files[0];
    var file2_actual = $file2_input[0].files[0];

    //* File validation here on client - both should be .xlsm files
    if (
      !validate_for_xlsm_type(file1_actual.name) ||
      !validate_for_xlsm_type(file2_actual.name)
    ) {
      console.error("One or both files are NOT VALID. Not .xlsm files");
      throw Error("One or both files are NOT VALID. Not .xlsm files");
      return;
    }

    // Create unique file names using the info from file objects
    var file1name, file2name;
    file1name =
      file1_actual.name.substring(0, file1_actual.name.length - 5) +
      file1_actual.lastModified +
      ".xlsm";
    file2name =
      file2_actual.name.substring(0, file2_actual.name.length - 5) +
      file2_actual.lastModified +
      ".xlsm";
    console.log("these are the generated names", file1name, file2name);

    // the names of these are used as keys for reference
    var formData = new FormData();
    formData.append("file1actual", file1_actual);
    formData.append("file1name", file1name);
    formData.append("file2actual", file2_actual);
    formData.append("file2name", file2name);

    $.ajax({
      xhr: function () {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/run-report");
        xhr.onreadystatechange = function (response) {};
        xhr.upload.addEventListener("progress", function (e) {
          // console.log("this is upload progress", xhr, e);
          if (e.lengthComputable) {
            var percent = Math.round((e.loaded / e.total) * 100);
            $("#files-upload-progressbar")
              .attr("aria-valuenow", percent)
              .css("width", percent + "%")
              .text(percent + "%");
          }
        });
        return xhr;
      },
      type: "POST",
      url: "/run-report",
      data: formData,
      processData: false,
      contentType: false,
      success: function (data) {
        // console.info("the post request is a success");
        $("#run-comparison").removeClass("invisible");
      },
    });
  });
});

const down_btn = $("#download-report-btn");
down_btn.on("click", function (e) {
  $.ajax({
    xhr: function () {
      var xhr = new XMLHttpRequest();
      xhr.open("GET", "/compare-sheets-algorithm");
      xhr.send();
      return xhr;
    },
    type: "GET",
    url: "/compare-sheets-algorithm",
    processData: false,
    contentType: false,
    success: function () {
      console.log("download here you go");
    },
  });
});

// TODO UI changes copy from old file.
// TODO Change the file name, remove the old js file.
