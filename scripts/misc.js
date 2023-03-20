/*
  YT playlist: https://www.youtube.com/playlist?list=PLPZferZXSpjgE_mg6mKqQRJLlRbk0Sxjp
  Miscellaneous scripts for getting stuff in DOM of the YT playlist.
  Used separately.
*/

// calculate total time //
const times = document.querySelectorAll('ytd-thumbnail-overlay-time-status-renderer');
let mins = 0, secs = 0;
for (let i = 0; i < times.length; i++) {
    // assumes <10 min video length
    mins += +times[i].innerText.substring(0, 1); // minutes
    secs += +times[i].innerText.substring(2, 5); // seconds
}
// convert seconds to HH:MM:SS
console.log(new Date((mins * 60 + secs) * 1000).toISOString().slice(11, 19));
// ======================================== //

// extract official hologra video links by parts of 50 links, for extract_comments.py
const videos = document.querySelectorAll('a#video-title');
const regexPattern = /(?<=watch\?v=)(.*)(?=&list)/;
const unofficialVids = [0, 1, 3, 5, 6, 9, 12, 15, 18, 21, 23, 26, 28, 29, 32, 37, 38, 44, 45, 46, 47, 48, 49, 50, 52, 53];
const episodeNo = 150;
const endIndex = episodeNo + 50;
let ids = '';
for (let i = episodeNo; i < endIndex; i++) {
  let epNo = i + 1;
  // outer opening bracket
  if (i === episodeNo) ids += '[';
  // ignore unofficial links
  if (!(unofficialVids.includes(i))) {
    // indentation
    if (i % 5 === 0 && i !== episodeNo) ids += '             ';
    // main content
    ids += `['${epNo}', '${videos[i].href.match(regexPattern)[0]}']`;
    // comma
    if (epNo !== endIndex) ids += ', ';
    // new line every 5 items
    if ((epNo) % 5 === 0 && epNo !== endIndex) ids += '\n';
  }
  // outer closing bracket
  if (epNo === endIndex) ids += ']';
}
console.log(ids);
// ======================================== //