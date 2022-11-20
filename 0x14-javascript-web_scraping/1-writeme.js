#!/usr/bin/node
const file = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(file, data, 'utf', (err)=>{
    if(err) throw err;
    /*or
    if (err){
        return console.error(err);
    }*/
});