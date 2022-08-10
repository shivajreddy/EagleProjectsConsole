// Run this after the document has loaded completely
$(document).ready(function () {
  console.log("its ready");

  // get the name of the submit

  $("#compare-report-form").on("submit", function (event) {
    event.preventDefault();
    const thisform = $("#compare-report-form");

    var report_form_data = new FormData($("#compare-report-form")[0]);
    console.log(thisform[0], report_form_data);
    // console.log(formData.getAll);

    // Handle form submissions to be proper here on front-end
    console.log("report form = ", report_form_data);

    $.ajax({
      type: "POST",
      url: "/run-report",
      data: report_form_data,
      processData: false,
      contentType: false,
      success: function () {
        const message = "hi" + "hello";
        console.log(`%c ${message}`, "color: orange");
      },
    });
  });
});
