<template>
  <nav>
      <h1>Buy Gold Coin</h1>
    </nav>
  <div class="container">
    
    <div class="gold-selector">


  <div v-for="filter in filterModes"
          :key="filter"
          :class="{ active: selectedFilter == filter }"
          @click="chooseFilter(filter)"

  >{{filter}}</div>



    </div>
    <div class="header">
          <h2>Buy Gold Coin</h2>
          <div class="div"> 
            <div> <Icon icon="gg:crown" />
    <Icon icon="akar-icons:circle" width="26" class="absolute"/>
    <p>99.99% Purity</p></div>
    <div> <Icon icon="carbon:delivery-truck" />
    <p>Door Step Delivery</p></div></div>
   
  
    </div>


    <div class="card-wrapper">
<GoldCardComponent
 v-for="item in actualData"
 :imageName="item.image_urls"
 :category="item.category"
 :price="item.price"
 :name="item.name"
></GoldCardComponent>
  </div>
  </div>


</template>
<script>
import GoldCardComponent from "../components/GoldCardComponent.vue";
import { Icon } from '@iconify/vue';
export default{
  components:{
    GoldCardComponent,
    Icon,
  },
   data() {
    return {
      filterModes:["SAFE GOLD","MMTC-PAMP"],
      selectedFilter: "SAFE GOLD",
      data:[],
    };
  },
  computed:{
    
     safeData() {
      return this.data.filter((item) => {
        return item.category == "SAFE GOLD";
      })
    },
     mmtcData() {
      return this.data.filter((item) => {
        return item.category == "MMTC-PAMP";
      })
    },
     actualData() {
      if (this.selectedFilter == "SAFE GOLD") {
        return this.safeData;
      } else if (this.selectedFilter == "MMTC-PAMP") {
        return this.mmtcData;
  }

},
  },
  methods: {
chooseFilter(filter) {
      this.selectedFilter = filter;
    },


  },
  mounted (){
    fetch("http://localhost:5000/gold/safe-gold").then((res)=>{
      return res.json()
    }).then((resp)=>{
      console.log(resp)
         this.data=resp
    })
    }
  };

</script>
<style scoped>
nav{
  background-color: rgb(0,41,112);
  display: flex;
  justify-content: center;
  color: white;
  margin-bottom: 20px;
}
.container{
  border-radius: 10px;
}
.gold-selector{
  border: 1px solid gray;

    border-radius: 5px;
    padding: 5px;
  

}
.gold-selector {
  display: flex;
  text-align: center;
  font-weight: 500;
  padding-bottom: 0;
}
.gold-selector div{
    width: 50%;
    font-weight: 500;

}
.gold-selector div.active {
  color: rgb(0,41,112);
  border-bottom: 4px solid rgb(0,41,112) ;
  font-weight: 600;
}
.gold-selector div:hover{
  cursor: pointer;
}
.header{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.header Icon{
  position: absolute;
}
.header .div{
  display: flex;
  align-items: center;
  justify-content: center;
  column-gap: 30px;
}
.header div div{
  display: flex;
  align-items: center;
}
.absolute{
  position: relative;
  right: 21px;
}
.card-wrapper{
  display: flex;
  column-gap: 30px;
 flex-wrap: wrap;
}




</style>