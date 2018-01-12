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
    
    console.log(data ," data");
    var spawn = require('child_process').spawn,
    py = spawn('python', ['./api/writeDna.py']),
             
    dataString = '';
    
    py.stdout.on('data', function(data){
       dataString += data.toString();
       console.log((dataString.replace("'",'"')), " dataString");
    });
            
       py.stdout.on('end', function(){
       console.log(dataString ," check");
     
       dna = JSON.parse(dataString.replace(/'/g,'"'));
       console.log(dna);
       //console.log(typeof(dna));
       console.log(dna, "1");
       res.redirect('/');   
    });
     
    py.stdin.write(JSON.stringify(data));
    py.stdin.end();
  
    console.log(dna , " json");
     
});

router.post('/aminoAcidPrecentage', function(req,res,next){
    console.log(req.body.data);   
    console.log(data ," data");
    var spawn = require('child_process').spawn,
    py = spawn('python', ['./api/aminoAcid.py']),
    data = [req.body.data],         
    dataString = '';
    
    py.stdout.on('data', function(data){
       dataString += data.toString();
       console.log((dataString.replace("'",'"')), " dataString");
    });
            
    py.stdout.on('end', function(){
    console.log(dataString);
     
    aa = JSON.parse(dataString.replace(/'/g,'"'));
    console.log(aa, "aa");
    //console.log(typeof(dna));
    
    res.redirect('/');   
    });
     
    py.stdin.write(JSON.stringify(data));
    py.stdin.end();
  
  
});

module.exports = router;
