// Run this after the document has loaded completely
$(document).ready(function () {
  // console.log("its ready");
  const Generate_Comparison_Report_button = $("#files-upload");
  const run_comparison_button = $("#run-comparison");

  //  Show Upload-Files button only after both files are selcted
  function show_hide_upload_button() {
    let file1_val = $("#file-1").val();
    let file2_val = $("#file-2").val();

    if (file1_val !== "" && file2_val !== "") {
      // remove invisible if it exists already - for upload, run comparision buttons
      if (Generate_Comparison_Report_button.hasClass("invisible")) {
        Generate_Comparison_Report_button.removeClass("invisible");
      }
      if (run_comparison_button.hasClass("invisible")) {
        run_comparison_button.removeClass("invisible");
      }
    } else {
      // add invisible if it doesn't exist
      if (!Generate_Comparison_Report_button.hasClass("invisible")) {
        Generate_Comparison_Report_button.addClass("invisible");
      }
      if (!run_comparison_button.hasClass("invisible")) {
        run_comparison_button.addClass("invisible");
      }
    }
  }

  $("#file-1").change(show_hide_upload_button);
  $("#file-2").change(show_hide_upload_button);

  // start upload
  Generate_Comparison_Report_button.on("click", function (e) {
    e.preventDefault();

    // show the progress bar div
    const progress_bar_div = $("#files-upload-progressbar-div");
    progress_bar_div.removeClass("invisible");

    const message = "Upload process started ";
    console.log(`%c ${message}`, "color: orange");

    var report_form_data = new FormData($("#compare-report-form")[0]);

    // start the upload process
    $.ajax({
      xhr: function () {
        var xhr = new window.XMLHttpRequest();
        console.log("this is xhr", xhr, xhr.upload);
        xhr.upload.addEventListener("progress", function (e) {
          console.log("this is the upload progress", xhr, e);
          if (e.lengthComputable) {
            // console.log("100% bytes Loaded" + e.loaded);
            // console.log("Total Size:" + e.total);
            // console.log("Percentage Uploaded" + e.loaded / e.total);
            var percent = Math.round((e.loaded / e.total) * 100);
            $("#files-upload-progressbar")
              .attr("aria-valuenow", percent)
              .css("width", percent + "%")
              .text(percent + "%");
            // $("#file2-upload-progressbar")
            //   .attr("aria-valuenow", percent)
            //   .css("width", percent + "%")
            //   .text(percent + "%");
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
        const message =
          "File upload finished and the form is going to be subbmitted with POSt request";
        console.log(`%c ${message}`, "color: orange");
      },
    });
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
  });
});
