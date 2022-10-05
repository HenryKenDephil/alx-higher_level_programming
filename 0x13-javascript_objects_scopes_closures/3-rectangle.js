#!/usr/bin/node

module.exports = class Rectangle {
    constructor(w, l) {
        if ((w <= 0) || (h <= 0)) {
            this.width = w;
            this.height = h;
        }
        
    }

    print() {
        for (let h = 0; h < this.height; h++) {
          let rec = '';
          for (let w = 0; w < this.width; w++) {
            rec +='x';
          } 
          console.log(rec); 
        }
    }
}
