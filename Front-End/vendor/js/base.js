$(function(){
    $("#includedNavbar").load("../../layouts/navbar.html");
});

// https://www.freecodecamp.org/news/how-to-read-json-file-in-javascript/
var config_base = null;
console.log('load json', new Date())
fetch('../../config.json')
    .then(function(res){
        return res.json();
    })
    .then(function(js){
        console.log('finished to load json', new Date())
        config_base = js;
    })