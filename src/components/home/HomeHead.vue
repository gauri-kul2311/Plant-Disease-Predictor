<template>
  <div class="head">
    <div class="float-left">
      <table class="above-base">
        <tr>
          <td class="pc">
            <p class="op">
              <img width="50px" height="50px" class="plant-cartoon" src="hang.jpg" />
            </p>
          </td>
          <td class="sp">
            <div class="op">
              <h5 class="text-center text-bold">PLANT DISEASE PREDICTOR</h5>
              <h6 class="large-screen-only">
                Upload the picture of diseased plant and get the disease predicted! 
              </h6>
              <q-btn class="get-started"
                to="/getstarted"
                size="1em">
                <q-icon left size="2em" name="eco" />
                <div>Get Started</div>
              </q-btn>
            </div>
          </td>
          <td class="pc">
            <p class="op large-screen-only">
              <img class="plant-cartoon "  src="hang.jpg" />
            </p>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.btn{
  height: 40px;
  background-color: rgb(71, 107, 50);
  margin-left: 10px;
  margin-right: 10px;
  padding-bottom: 10px;
  text-align: center;
}
.btn-home{
    height: 30px;
  margin-top: 10px;
  margin-left: 10px;
  margin-right: 10px;
  text-align: center;
}
.get-started{
    background-color: rgb(71, 107, 50);
    color: white;
}
</style>
