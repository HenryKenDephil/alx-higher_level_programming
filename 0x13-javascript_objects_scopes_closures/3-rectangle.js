#!/usr/bin/node

module.exports = class Rectangle {
    constructor(w, l) {
        if ((w > 0) && (h > 0)) {
            this.width = w;
            this.height = h;
        }
        
    }

    print() {
        for (let height = 0; height < this.height; height++) {
          let rec = '';
          for (width = 0; this.width < this.width; j++) {
            rec +='x';
          } 
          console.log(rec); 
        }
    }
}
