var lines = $('#tab_0').find('.container > h1');

function putTimeOnLine(prefix, line) {
    $.get("/now", function (data) {
        line.text(prefix + data);
    });
}

putTimeOnLine('onload: ', lines.first());

setInterval(function () {
    putTimeOnLine('reload: ', lines.last());
}, 500);
