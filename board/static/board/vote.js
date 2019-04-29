var baseUrl = "/site/vote/";

$(".vote").click(function() {
  var ctx = $(this);

  var csrftoken = getCookie("csrftoken") || "";

  if (!csrftoken) {
    // TODO - handle this...
    var message = "There was a problem submitting your vote. Please try again.";
    return;
  }

  // TODO - functionality to 'remove' vote (set back to 0)
  var siteId = ctx.closest("article").data("site-id");
  var vote = ctx.hasClass("upvote") ? 1 : -1; // clicked upvote or downvote

  // like on reddit, if user clicks on button that is already active,
  // go back to default (delete vote), so set vote = 0
  if (ctx.hasClass("active")) {
    vote = 0;
  }

  var data = {
    siteId: siteId,
    vote: vote
  };

  $.ajax({
    type: "POST",
    url: baseUrl,
    data: data,
    headers: {
      "X-CSRFToken": csrftoken
    },
    success: function(data) {
      console.log(data);
      // change css class of buttons
      if (vote === 1) {
        ctx.addClass("active");
        ctx
          .closest(".vote-container")
          .find(".downvote")
          .removeClass("active");
      } else if (vote === -1) {
        ctx.addClass("active");
        ctx
          .closest(".vote-container")
          .find(".upvote")
          .removeClass("active");
      } else {
        // removed vote (0)
        ctx
          .closest(".vote-container")
          .find(".vote")
          .removeClass("active");
      }

      location.reload(); // FIXME - temporary hack
    },
    fail: function(err) {
      // TODO - handle this
      console.error("error :", err);
    }
  });
});
