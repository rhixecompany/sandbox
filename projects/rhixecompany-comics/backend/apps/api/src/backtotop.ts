// Get the Top button
const myCustomTopButton = document.getElementById(
  "btn-to-top",
) as HTMLBodyElement;

// Get the Down button
const myCustomDownButton = document.getElementById(
  "btn-to-down",
) as HTMLBodyElement;

// When the user scrolls down 20px from the top of the document, show the button
const myScrollTopFunction = (): void => {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    myCustomTopButton.classList.add("style_visible");
  } else {
    myCustomTopButton.classList.remove("style_visible");
  }
};

// When the user scrolls down 20px from the down of the document, show the button
const myScrollDownFunction = (): void => {
  if (
    document.body.scrollTop > 100 ||
    document.documentElement.scrollTop > 100
  ) {
    myCustomDownButton.classList.remove("style_visible");
  } else {
    myCustomDownButton.classList.add("style_visible");
  }
};

const mybackToTop = (): void => {
  window.scrollTo({ top: 0, behavior: "smooth" });
};

const mybackToDown = (): void => {
  window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
};

// When the user clicks on the button, scroll to the top of the document
myCustomTopButton.addEventListener("click", mybackToTop);

// When the user clicks on the button, scroll to the top of the document
myCustomDownButton.addEventListener("click", mybackToDown);

window.addEventListener("scroll", myScrollTopFunction);

window.addEventListener("scroll", myScrollDownFunction);
