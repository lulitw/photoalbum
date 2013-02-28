
function creat_album() {
    var txt = "<li class='span4'><div class='thumbnail'><img src='http://carryoncitizens.com/files/600px-WiimoteButton1_svg.png' alt='Thumbnail'><div class='caption'><h3>New Album</h3><p>album's description</p><p><a href='#' class='btn btn-primary'>View</a><a href='#' class='btn btn-success'>Edit</a> <a href='#' class='btn btn-danger'>Delete</a></p></div></div></li>";
    $("#new_album").before(txt);
}
