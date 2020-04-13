<template>
    <div class="flex">
        <div class="image">
            <img src="../../../public/trees.jpeg">
        </div>
        <div class="content">
            <div class="loc"><em><h1>Location: Chios(Mesa Didima)</h1></em></div>
            
            <div class="trees"><h2>Trees: 50</h2></div>
            <div class="type"><h2>Type: Mastixa</h2></div>
        </div>
        <div class="price"><h2>Price: 200$/3m</h2></div>
    </div>
</template>

<script>
export default {
    name: "Field"
}
</script>

<style scoped>
    .flex{
        display: flex;
        background: linear-gradient(to bottom, rgba(125, 255, 143, 0.333), #33a170);
        align-items: center;
    }

    .image{
        display: flex;
    }

    img{
        border-radius: 5%;
    }

    .content{
        flex: 1;
        display: flex;
        flex-direction: column;
    }

    .loc{
        padding-left: 1%;
        align-self: center;
    }

    .price{
        padding-right: 1%;
        writing-mode: vertical-lr;
        display: flex;
        align-items: center;
        justify-content: center;
    }

</style>