
var timer;
var startTime;

function start() {
  startTime = parseInt(localStorage.getItem('startTime') || Date.now());
  localStorage.setItem('startTime', startTime);
  timer = setInterval(clockTick, 100);
}

function stop() {
  clearInterval(timer);
}

function reset() {
  clearInterval(timer);
  localStorage.removeItem('startTime');
  document.getElementById('display-area').innerHTML = "00:00:00.000";
}

function clockTick() {
  var currentTime = Date.now(),
    timeElapsed = new Date(currentTime - startTime),
    hours = timeElapsed.getUTCHours(),
    mins = timeElapsed.getUTCMinutes(),
    secs = timeElapsed.getUTCSeconds(),
    ms = timeElapsed.getUTCMilliseconds(),
    display = document.getElementById("display-area");

  display.innerHTML =
    (hours > 9 ? hours : "0" + hours) + ":" +
    (mins > 9 ? mins : "0" + mins) + ":" +
    (secs > 9 ? secs : "0" + secs) + "." +
    (ms > 99 ? ms : ms > 9 ? "0" + ms : "00" + ms);
};

var stopBtn = document.getElementById('stop_btn');

stopBtn.addEventListener('click', function() {
  stop();
})
start();