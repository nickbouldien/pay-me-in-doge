var baseUrl = "/site/vote/";

$(".vote").click(function() {
  var ctx = $(this);

  var csrftoken = getCookie("csrftoken") || "";

  // TODO - functionality to 'remove' vote (set back to 0)
  var vote = ctx.hasClass("upvote") ? 1 : -1; // clicked upvote or downvote
  var siteId = ctx.closest("article").data("site-id");

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
      // change css class of buttons
      if (vote === 1) {
        ctx.addClass("active");
        window.ctx = ctx;
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
    },
    fail: function(err) {
      alert("Data Loaded: " + err);
    }
  });
});
