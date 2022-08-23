var $file1_input, $file2_input;

function transform_button_to_spinner() {
  const $generate_report_button = $("#generate-report-btn");
  $generate_report_button.removeClass("btn-danger");
  $generate_report_button.addClass("btn-primary");
  $generate_report_button.text("Generating Comparison Report");
  $generate_report_button.prop("disabled", true);
  $generate_report_button.prepend(
    '<span id="button-spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span><span> </span>'
  );
}

function transform_button_to_finished() {
  const $generate_report_button = $("#generate-report-btn");
  $generate_report_button.empty();
  $generate_report_button.text("Report Successfully Downloaded");
  $generate_report_button.removeClass("btn-primary");
  $generate_report_button.addClass("btn-success");
}

$(document).ready(function () {
  // DOM nodes
  // const generate_report_button = $("#files-upload");
  const generate_report_button = $("#generate-report-btn");
  $file1_input = $("#file-1");
  $file2_input = $("#file-2");

  // Helper Function -> Show Button after both files selected
  function show_hide_upload_button() {
    let file1_val = $("#file-1").val();
    let file2_val = $("#file-2").val();

    if (file1_val !== "" && file2_val !== "") {
      // remove invisible if it exists already - for upload, run comparision buttons
      if (generate_report_button.hasClass("invisible")) {
        generate_report_button.removeClass("invisible");
      }
    } else {
      // add invisible if it doesn't exist
      if (!generate_report_button.hasClass("invisible")) {
        generate_report_button.addClass("invisible");
      }
    }
  }

  // Helper function -> File extension validation
  function validate_for_xlsm_type(filename) {
    const arr = filename.split(".");
    const file_ext = arr[arr.length - 1];
    if (file_ext === "xlsm" || file_ext === "XLSM") {
      return true;
    }
    return false;
  }

  $file1_input.change(show_hide_upload_button);
  $file2_input.change(show_hide_upload_button);

  // Generate_Comparison_Report_button.on("click", function (e) {
  generate_report_button.on("click", function (e) {
    e.preventDefault();

    //? Disable button, Show generating spinner, Change Text
    transform_button_to_spinner();
    // return;

    var file_1_fileObject = $file1_input[0].files[0];
    var file_2_fileObject = $file2_input[0].files[0];

    //* File validation here on client - both should be .xlsm files
    if (
      !validate_for_xlsm_type(file_1_fileObject.name) ||
      !validate_for_xlsm_type(file_2_fileObject.name)
    ) {
      console.error("One or both files are NOT VALID. Not .xlsm files");
      throw Error("One or both files are NOT VALID. Not .xlsm files");
      return;
    }

    //? Create unique file names using the info from file objects
    var file_1_name_ext, file_2_name_ext;
    file_1_name_ext =
      file_1_fileObject.name.substring(0, file_1_fileObject.name.length - 5) +
      file_1_fileObject.lastModified +
      ".xlsm";
    file_2_name_ext =
      file_2_fileObject.name.substring(0, file_2_fileObject.name.length - 5) +
      file_2_fileObject.lastModified +
      ".xlsm";

    //? Create form data, with files and and their names
    //? the names of the files given here are used as keys for reference on server
    var formData = new FormData();
    formData.append("file1actual", file_1_fileObject);
    formData.append("file1name", file_1_name_ext);
    formData.append("file2actual", file_2_fileObject);
    formData.append("file2name", file_2_name_ext);

    function startDownload(signedRequest, url) {
      var link = document.createElement("a");
      link.href = signedRequest;
      link.setAttribute("download", "download");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    var xhr;
    $.ajax({
      xhr: function () {
        var xhr = new XMLHttpRequest();
        // xhr.upload.addEventListener("progress", function (e) {
        //   if (e.lengthComputable) {
        //     var percent = Math.round((e.loaded / e.total) * 100);
        //     $("#files-upload-progressbar")
        //       .attr("aria-valuenow", percent)
        //       .css("width", percent + "%")
        //       .text(percent + "%");
        //   }
        // });
        // xhr.addEventListener("readystatechange", function (e) {
        //   if (xhr.readyState === 2 && xhr.status === 200) {
        //     // download is being started
        //     console.log("Download is starting");
        //   } else if (xhr.readyState === 3) {
        //     console.log("download is under progress");
        //   } else if (xhr.readyState === 4) {
        //     console.log("The download has finished");
        //   }
        // });
        return xhr;
      },
      type: "POST",
      url: "/upload-run-download",
      data: formData,
      processData: false,
      contentType: false,
      // flask creates the file and sends the filename
      success: function (fileName) {
        console.info("the post request is a success");
        $("#run-comparison").removeClass("invisible");

        var blob = new Blob([fileName], { type: "application/octetstream" });

        //Check the Browser type and download the File.
        var isIE = false || !!document.documentMode;
        if (isIE) {
          window.navigator.msSaveBlob(blob, fileName);
        } else {
          var url = window.URL || window.webkitURL;
          link = url.createObjectURL(blob);
          var a = $("<a />");
          a.attr("download", fileName);
          a.attr("href", link);
          $("body").append(a);
          a[0].click();
          $("body").remove(a);
        }

        //? Change the button state to finished
        transform_button_to_finished();
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
      // console.log("download here you go");
    },
  });
});

// TODO UI changes copy from old file.
// TODO Change the file name, remove the old js file.
