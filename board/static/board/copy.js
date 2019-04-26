$(document).ready(function() {
  var clipboard = new ClipboardJS(".clipboard");

  var reference = $(".clipboard");
  var popover = $(".popup");

  popover.hide();

  clipboard.on("success", function(e) {
    e.clearSelection();

    popover.show();

    var popper = new Popper(reference, popover, {
      placement: "bottom"
    });
  });

  clipboard.on("error", function(e) {
    // TODO - handle this
    console.error("error copying to clipboard: ", e);
  });

  $(".clipboard").on("blur", function() {
    popover.hide();
  });
});
