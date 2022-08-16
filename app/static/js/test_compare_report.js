var $file1, $file2;

$(document).ready(function () {
  $file1 = $("#file-1");
  $file2 = $("#file-2");

  const upload_button = $("#files-upload");
  upload_button.on("click", async function (e) {
    e.preventDefault();

    var xhr;

    const message = "Upload process started ";
    console.log(`%c ${message}`, "color: orange");

    console.log($file1[0].files[0]);
    console.log($file2[0].files[0]);

    // the names of these are used as keys for reference
    var formData = new FormData();
    formData.append("file1actual", $file1[0].files[0]);
    formData.append("file1name", "AQT_01_01_2022");
    formData.append("file2actual", $file2[0].files[0]);
    formData.append("file2name", "AQT_01_02_2022");
    // console.log("this form data", formData, formData.values());
    for (const k of formData.keys()) {
      console.log(k);
    }

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
        // alert(data);
        console.log("the post request is a success");
        $("#run-comparison").removeClass("invisible");
      },
    });
  });
});

const down_btn = $("#download-report-btn");
console.log(down_btn);
