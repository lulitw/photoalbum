function copyToClipboard() {
    var txt = ""
    
    txt += this.location.href;

    ZeroClipboard.setMoviePath("http://www.track2web.com/wp-includes/js/zeroclipboard/ZeroClipboard.swf");

    clip = new ZeroClipboard.Client();

    clip.setHandCursor(true);

    clip.setText(txt);

    clip.addEventListener("complete", function (client, text) {
        alert("URL Copied! \n" + text);
    });

    clip.glue("copy_url_button");
}