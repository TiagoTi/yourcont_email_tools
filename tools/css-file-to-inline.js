var inlineCss = require('inline-css');
var fs = require('fs');

const testFolder  = '../templates/email/styled/';
const testFolder2 = '../templates/email/';

fs.readdir(testFolder, function (err, files) {
    files.forEach(file=>{
        console.log(file);
        fs.readFile(testFolder + file, 'utf8', function (err, html_contents) {
            inlineCss(html_contents, { url: 'http://youtcont.com' }).then(function (html_contents) {
             console.log("convertido com sucesso");
             fs.writeFile(testFolder2+file, html_contents, function(err, data) {
                if (err) console.log(err);
                 console.log("Successfully Written to File.");
                });
             });
       });
    });
});




