function setBumperHeight() {
  const scrollHeight = document.documentElement.scrollHeight;
  const leftBumper = document.querySelector(".left-bumper");
  const rightBumper = document.querySelector(".right-bumper");

  leftBumper.style.height = `${scrollHeight}px`;
  rightBumper.style.height = `${scrollHeight}px`;
}

window.addEventListener("resize", setBumperHeight);
window.addEventListener("load", setBumperHeight);
