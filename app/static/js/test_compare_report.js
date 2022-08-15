var $file1, $file2;

$(document).ready(function () {
  // $("#compare-report-form").on("submit", processForm);
  $file1 = $("#file-1");
  $file2 = $("#file-2");

  const something = $file1[0].files[0];
  console.log("this is that something", something);

  const upload_button = $("#files-upload");
  upload_button.on("click", function (e) {
    e.preventDefault();

    const message = "Upload process started ";
    console.log(`%c ${message}`, "color: orange");

    console.log($file1[0].files[0]);
    console.log($file2[0].files[0]);

    var formData = new FormData();
    formData.append("file1actual", $file1[0].files[0]);
    formData.append("file2actual", $file2[0].files[0]);
    console.log("this form data", formData);

    $.ajax({
      url: "/run-report",
      data: formData,
      type: "POST",
      success: function () {
        console.log("the form is submitted along with ajax");
      },
    });
  });
});

//   $.ajax({
//     xhr: function () {
//       myXhr = $.ajaxSettings.xhr();
//       myXhr.addEventListener("progress", function (e) {}, false);
//       if (myXhr.upload) {
//         myXhr.upload.onprogress = function (e) {
//           var completed = 0;
//           if (e.lengthComputable) {
//             var done = e.position || e.loaded,
//               total = e.totalSize || e.total;
//             completed = Math.round(((done / total) * 1000) / 10);
//           }
//           console.log(completed); // Displays the completed percentage
//         };
//       }
//       return myXhr;
//     },
//   });
// });

function processForm(e) {
  e.preventDefault();
  console.log("processForm");

  var formData = new FormData();
  if ($file1.val()) formData.append("file1", $file1.get(0).files[0]);
  if ($file2.val()) formData.append("file2", $file2.get(0).files[0]);

  var request = new XMLHttpRequest();
  request.open("POST", "/run-report");
  console.log("request is now open");

  // request.upload.addEventListener("progress", (pe) => {
  //   if (pe.lengthComputable) {
  //     var percent = Math.round((pe.loaded / pe.total) * 100);
  //     console.log(percent, pe);
  //     $("#files-upload-progressbar")
  //       .attr("aria-valuenow", percent)
  //       .css("width", percent + "%")
  //       .text(percent + "%");
  //   }
  // });

  request.onprogress = function (e) {
    console.log("this is inside progress");
    if (e.lengthComputable) {
      console.log(e.loaded + " / " + e.total);
    }
  };

  request.send(formData);

  request.onload = function (e) {
    console.log("Request Status", request.status);
  };
  request.upload.addEventListener("progress", function (e) {
    console.log("this is the request upload event", e);
  });
}
