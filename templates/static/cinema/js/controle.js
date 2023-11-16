
largura=window.screen.width;

window.addEventListener('load',Efeito);
function Efeito(){

hamburgue= document.getElementById("hamburgue");
siderbar= document.getElementById("side");
main =document.getElementById("main");


hamburgue.addEventListener("click", () => {
  siderbar.classList.toggle("transicao-sider");
  main.classList.toggle("transicao-main");
  if(largura<=600){
    siderbar.classList.toggle("transicao-sider-mini");
  }


  

  });

 
}





{
let ctx=document.getElementById("sexo")

var sexo= new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '#percentual por sexo ',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    },
    responsive:true 
  }
});}

{
let ctx=document.getElementById("idade")

var sexo= new Chart(ctx, {
  type: 'radar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '#Percentual idade  ',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {

    Animation:{
      duration:5000,
    },
    scales: {
      y: {
        beginAtZero: true
      }
    },

    layout:{
      padding:{
        left:40
      },

    },
    responsive:true 

  }
});}



{
let ctx=document.getElementById("total-dados")

var sexo= new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '#total dados  ',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    animations: {
      tension: {
        duration: 1000,
        easing: 'linear',
        from: 1,
        to: 0,
        loop: true
      }
    },
    scales: {
      y: { // defining min and max so hiding the dataset does not change scale range
        min: 0,
       
      }
    },
    
    layout:{
      padding:{
        left:40
      }

      
   
  },

  title: {
    display: true,
    text: 'Custom Chart Title',
    color:'white',
},
   responsive:true 
}
});}