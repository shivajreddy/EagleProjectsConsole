// Run this after the document has loaded completely
$(document).ready(function () {
  // console.log("its ready");
  $("#file-1").change(function () {
    if ($("#file-1").val() !== "") {
      return $("#file-1-upload").removeClass("invisible");
    } else {
      return;
    }
    // console.log(fil1);
  });

  // separate upload buttons for each
  file1_upload = $("#file-1-upload");
  file2_upload = $("#file-2-upload");

  file1_upload.on("click", function (e) {
    e.preventDefault();
    console.log("Upload file 1 started");
  });

  // get the name of the submit

  $("#compare-report-form").on("submit", function (event) {
    event.preventDefault();
    const thisform = $("#compare-report-form");

    // Dont submit form, if one of the file is not uploaded
    const file1_val = $("#file-1").val();
    const file2_val = $("#file-2").val();
    // console.log(`%cValues: ${file1_val}, ${file2_val}`, "color: orange");
    if (!file1_val || !file2_val) {
      console.log(`%cFailed: ${file1_val}, ${file2_val}`, "color: orange");
      return;
    }

    // trying looping over two files
    var all_files = $("#");
    var completedCount = 0;
    var totalFiles = 2;
    for (var i = 0; i < totalFiles; i++) {
      var formData = new FormData();
      var file = all_files.files;
      console.log("FILE = ", file);
    }

    var report_form_data = new FormData($("#compare-report-form")[0]);
    // console.log(thisform[0], report_form_data);

    // console.log(formData.getAll);

    // Handle form submissions to be proper here on front-end
    // console.log("report form = ", report_form_data);

    $.ajax({
      xhr: function () {
        var xhr = new window.XMLHttpRequest();
        xhr.upload.addEventListener("progress", function (e) {
          console.log("this is the shit", xhr, e);
          if (e.lengthComputable) {
            // console.log("100% bytes Loaded" + e.loaded);
            // console.log("Total Size:" + e.total);
            // console.log("Percentage Uploaded" + e.loaded / e.total);
            var percent = Math.round((e.loaded / e.total) * 100);
            $("#file1-upload-progressbar")
              .attr("aria-valuenow", percent)
              .css("width", percent + "%")
              .text(percent + "%");
            $("#file2-upload-progressbar")
              .attr("aria-valuenow", percent)
              .css("width", percent + "%")
              .text(percent + "%");
          }
        });
        return xhr;
      },
      type: "POST",
      url: "/run-report",
      data: report_form_data,
      processData: false,
      contentType: false,
      success: function () {
        const message = "Form submitted";
        console.log(`%c ${message}`, "color: orange");
      },
    });
  });
});
