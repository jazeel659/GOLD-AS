<template>

<div class="card-container"
>

<img :src="imageName" alt="">

<div class="details">
    <p>{{name}}</p>
    <p>{{category}}</p>
    <h2>{{price}}</h2>
</div>

</div>


</template>
<script>
export default{
props:{
 imageName: String,
 price: String,
 name:String,
 category:String,
 },

 
 };


</script>
<style scoped>
*{
    margin: 0;
    padding: 0;
}
.card-container{
    margin: 15px;
    width: 220px;
    background-color:rgb(255,255,255);
    border: 1px solid grey;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px;
    border-radius: 10px;

}
img{
    width:150px
}
.details{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: left;
    margin: 10px;
}
.details p,h2{
    margin: 10px;
}


</style>