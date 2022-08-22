var $file1_input, $file2_input;

function validate_for_xlsm_type(filename) {
  const arr = filename.split(".");
  const file_ext = arr[arr.length - 1];
  if (file_ext === "xlsm" || file_ext === "XLSM") {
    return true;
  }
  return false;
}

const Generate_Comparison_Report_button = $("#files-upload");
function show_hide_upload_button() {
  let file1_val = $("#file-1").val();
  let file2_val = $("#file-2").val();

  if (file1_val !== "" && file2_val !== "") {
    // remove invisible if it exists already - for upload, run comparision buttons
    if (Generate_Comparison_Report_button.hasClass("invisible")) {
      Generate_Comparison_Report_button.removeClass("invisible");
    }
  } else {
    // add invisible if it doesn't exist
    if (!Generate_Comparison_Report_button.hasClass("invisible")) {
      Generate_Comparison_Report_button.addClass("invisible");
    }
  }
}

$(document).ready(function () {
  $file1_input = $("#file-1");
  $file2_input = $("#file-2");

  $("#file-1").change(show_hide_upload_button);
  $("#file-2").change(show_hide_upload_button);

  const upload_button = $("#files-upload");
  Generate_Comparison_Report_button.on("click", function (e) {
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

    function startDownload(signedRequest, url) {
      var link = document.createElement("a");
      link.href = signedRequest;
      link.setAttribute("download", "download");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    $.ajax({
      xhr: function () {
        var xhr = new XMLHttpRequest();
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
        xhr.addEventListener("readystatechange", function (e) {
          if (xhr.readyState === 2 && xhr.status === 200) {
            // download is being started
            console.log("Download is starting");
          } else if (xhr.readyState === 3) {
            console.log("download is under progress");
          } else if (xhr.readyState === 4) {
            console.log("The download has finished");
          }
        });
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
