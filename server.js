var express = require('express');
var request = require('request');
var http = require('http');
var engines = require('consolidate');

var app = express();

app.set('port', 8080);
app.use(express.static(__dirname + '/public'));
app.engine('html', engines.mustache);
app.set('view engine', 'html');


app.get('/', function(req, res) {res.render('index.html')});

http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});