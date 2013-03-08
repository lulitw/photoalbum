 function copyToClipBoard() {
        var clipBoardContent = "";
        clipBoardContent += this.location.href;
        window.clipboardData.setData("Text", clipBoardContent);
        alert("Sucess!");
    }