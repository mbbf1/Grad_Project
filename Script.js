// Array of chapter objects
const chapters = [
{ title: "Final Book", link: "final book.pdf" },
  { title: "Final brochure", link: "Final brochure .pdf" },
  { title: "Source Code", link: "https://github.com/mbbf1/Grad_Project/tree/main/Source" },
  { title: "Project Book", link: "booklet.pdf" },
  { title: "Design & Implementation Of Stand Alone High Gain Jammer system Against UAVS Using Helical Antennas", link: "Design & Implementation Of Stand Alone High Gain Jammer system Against UAVS Using Helical Antennas.pdf" },
  { title: "Images", link: "https://github.com/mbbf1/Grad_Project/tree/main/Images" },
  { title: "Presentation", link: "  presentation.zip" },
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
