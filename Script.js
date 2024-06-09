// Array of chapter objects
const chapters = [
{ title: "Final Book", link: "Final Book.pdf" },
  { title: "Final brochure", link: "Final brochure.pdf" },
  { title: "Source Code", link: "Source.rar" },
  { title: "Project Book", link: "Book.pdf" },
  // Add more chapters as needed
];

// Loop through the array and create a link element for each chapter
const container = document.querySelector(".container");
chapters.forEach((chapter) => {
  const link = document.createElement("a");
  link.href = chapter.link;
  link.textContent = chapter.title;
  container.appendChild(link);
});
