const btn = document.getElementById("summarise");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    document.getElementById("lebron").innerHTML = "foo";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        document.getElementById("lebron").innerHTML = url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "Summarise";
        }
        document.getElementById("lebron").innerHTML = "kobe";
        xhr.send();
        document.getElementById("lebron").innerHTML = text;
    });
});