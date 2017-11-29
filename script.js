function ButtonClick() {
    readTextFile("///C:/Users/emacise/Desktop/Moni/raspberry/test.txt");
    displayValue("temperature", 20);
    // window.alert(readTextFile("file:///C:/Users/emacise/Desktop/Moni/raspberry"););
}

function displayValue(uchwyt, temp){
    var tempVal = temp;
    document.getElementById(uchwyt).innerHTML = tempVal.toString();
}

function readTextFile(file) {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, true);
    // window.alert("TEST");

    rawFile.onreadystatechange = function () {

        if(rawFile.readyState === 4) {
            if(rawFile.status === 200 || rawFile.status == 0) {
                var allText = rawFile.responseText;
                window.alert(allText);
                // document.getElementById(uchwyt).innerHTML = allText;
            }
        }
    }
    rawFile.send(null);
}
