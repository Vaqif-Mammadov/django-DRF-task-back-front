

fetch("http://127.0.0.1:8000/books-api/list/")
.then ((res)=> res.json())
.then ((data)=> data.map(blog => kitab(blog)));

function kitab(blog){
  const bisey =`<div class="card">
                    <div class="card-img-top"></div>
                      <img src="${blog.image}" alt="Card image cap">
                      <div class="card-body">
                          <h2 class="card-title" >${blog.title}</h2>
                          <h2 class="card-title" >${blog.name}</h2>
                          <h2 class="card-title" >${blog.year}</h2>
                      </div>
                </div>;`
                console.log(document.querySelector(".ketebe").innerHTML)
  document.querySelector(".ketebe").innerHTML+=bisey;
}
