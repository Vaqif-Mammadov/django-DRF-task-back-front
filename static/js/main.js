const main = document.querySelector('body')
let titles=[];
let names=[];
let years=[];
let images =[];

let yoxla = 0;

fetch("http://127.0.0.1:8000/books-api/list/")
  .then((res) => res.json())
  .then((items) => items.map((item) => (images.push(item.image),titles.push(item.title),years.push(item.year),names.push(item.name))));
const Books = document.createElement("div");
Books.classList.add("Books");
main.append(Books);


function yukle(){
  for (let i=0 ; i<= titles.length-1;i++){
    const Book = document.createElement("div");
    Book.classList.add("Book");
    Books.append(Book);
    const img = document.createElement("div");
    img.classList.add("imag");
    Book.append(img);
    const imgg=document.createElement('img')
    imgg.src=images[i]
    img.append(imgg);
    const option = document.createElement("div");
    option.classList.add("options");
    Book.append(option);
    const titl=document.createElement("h3")
    titl.innerHTML=titles[i]
    const yea=document.createElement("h3")
    yea.innerHTML=years[i]
    const nam=document.createElement("h3")
    nam.innerHTML=names[i]
    
}
}