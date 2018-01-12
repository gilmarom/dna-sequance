var express = require('express');
var router = express.Router();
var dna={};
var Prism = require('prismjs');
var aa={};

router.get('/', function(req, res, next){
    
    res.render('index', { dna : dna, aa : aa })
            
});

router.post('/send', function (req, res, next) {
    
    var data = req.body.data;
    var spawn = require('child_process').spawn,
    py = spawn('python', ['./api/writeDna.py']),
    dataString = '';
    py.stdout.on('data', function(data){
       dataString += data.toString();
       console.log((dataString.replace("'",'"')), " dataString");
    });
            
       py.stdout.on('end', function(){
       dna = JSON.parse(dataString.replace(/'/g,'"'));
       res.redirect('/');   
    });
     
    py.stdin.write(JSON.stringify(data));
    py.stdin.end();
  
    
     
});

router.post('/aminoAcidPrecentage', function(req,res,next){
   
    var spawn = require('child_process').spawn,
    py = spawn('python', ['./api/aminoAcid.py']),
    data = [req.body.data],         
    dataString = '';
    
    py.stdout.on('data', function(data){
       dataString += data.toString();
      
    });
            
    py.stdout.on('end', function(){
   
     
    aa = JSON.parse(dataString.replace(/'/g,'"'));

    //console.log(typeof(dna));
    
    res.redirect('/');   
    });
     
    py.stdin.write(JSON.stringify(data));
    py.stdin.end();
  
  
});

module.exports = router;
