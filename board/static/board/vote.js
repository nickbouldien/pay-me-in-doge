$(".upvote").click(function() {
  console.log("upvote");
  var siteId = $(this)
    .closest("article")
    .data("site-id");
  console.log("site id: ", siteId);
});

$(".downvote").click(function() {
  console.log("downvote");
  var siteId = $(this)
    .closest("article")
    .data("site-id");
  console.log("site id: ", siteId);
});
