/*
  various js codes used in this project
  used separately
*/

// calculate total time, in yt playlist
const times = document.querySelectorAll('ytd-thumbnail-overlay-time-status-renderer');
let mins = 0, secs = 0;
for (let i = 0; i < times.length; i++) {
    // assumes <10 min video length
    mins += +times[i].innerText.substring(0, 1); // minutes
    secs += +times[i].innerText.substring(2, 5); // seconds
}
console.log(mins * 60 + secs);

// extract official hologra video links, in yt playlist
const videos = document.querySelectorAll('#video-title');
const regexPattern = /(?<=watch\?v=)(.*)(?=&list)/;
const unofficialVids = [0, 1, 3, 5, 6, 9, 12, 15, 18, 21, 23, 26, 28, 29, 32, 37, 38, 44, 45, 46, 47, 48, 49, 50, 52, 53];
var ids = '';
for (let i = 0; i < videos.length; i++) {
  if (i == 0) ids += '[';
  if (!(unofficialVids.includes(i))) {
    ids += `['${i + 1}', '${videos[i].href.match(regexPattern)[0]}']`;
    if (i != videos.length - 1) ids += ', ';
  }
  if (i == videos.length - 1) ids += ']';
}
console.log(ids);