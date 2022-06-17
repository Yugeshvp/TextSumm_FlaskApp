let textfield = document.getElementById("text-field");
let wordCount = document.getElementById("word-count");

 textfield.addEventListener("input", () => {
//value-length command specifies the maximum value length in bytes
//textContent sets or returns the text content of the specified node
   characCount.textContent = textfield.value.length;
//trim() method removes whitespace from both ends of a string
   let txt = inputTextArea.value.trim();
//txt.split(/\s+/) code will split the full classname of an element into an array containing every class
   wordCount.textContent = txt.split(/\s+/).filter((item) => item).length;
 });