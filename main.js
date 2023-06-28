class Timer {
    constructor () {
      this.isRunning = false;
      this.startTime = 0;
      this.overallTime = 0;
    }
  
    _getTimeElapsedSinceLastStart () {
      if (!this.startTime) {
        return 0;
      }
    
      return Date.now() - this.startTime;
    }
  
    start () {
      if (this.isRunning) {
        return console.error('Timer is already running');
      }
  
      this.isRunning = true;
  
      this.startTime = Date.now();
    }
  
    stop () {
      if (!this.isRunning) {
        return console.error('Timer is already stopped');
      }
  
      this.isRunning = false;
  
      this.overallTime = this.overallTime + this._getTimeElapsedSinceLastStart();
    }
  
    reset () {
      this.overallTime = 0;
  
      if (this.isRunning) {
        this.startTime = Date.now();
        return;
      }
  
      this.startTime = 0;
    }
  
    getTime () {
      if (!this.startTime) {
        return 0;
      }
  
      if (this.isRunning) {
        return this.overallTime + this._getTimeElapsedSinceLastStart();
      }
  
      return this.overallTime;
    }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
/*
<p>1 = 0-150<br>
2 = 150-240<br>
3 = 240-270<br>
4 = 270-300<br>
5 = 300-360</p>;
*/
function makeScore(score) {
    if (score > 300) {
        return 5;
    } else if (score > 270) {
        return 4;
    } else if (score > 240) {
        return 3;
    } else if (score > 150) {
        return 2;
    } else if (score > 0) {
        return 1;
    } else {
        return -1;
    }
}

function getDegrees(p0, c, p1) {
    //calculate the angel from 3 points, c = centre

    var p0c = Math.sqrt(Math.pow(c.x-p0.x,2)+
                        Math.pow(c.y-p0.y,2));  
    var p1c = Math.sqrt(Math.pow(c.x-p1.x,2)+
                        Math.pow(c.y-p1.y,2));
    var p0p1 = Math.sqrt(Math.pow(p1.x-p0.x,2)+
                        Math.pow(p1.y-p0.y,2));
    var angle = Math.acos((p1c*p1c+p0c*p0c-p0p1*p0p1)/(2*p1c*p0c));

    return Math.round(angle * (180 / Math.PI));
}
  
function startAgain(timer, shout, ending) {
  // shout.style.display = "none";
  // ending.style.display = "none";
  timer.reset();
  shout.innerHTML = "start";
  block = false;
}