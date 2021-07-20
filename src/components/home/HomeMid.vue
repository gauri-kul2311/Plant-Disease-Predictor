<template>
  <q-page class="mid">
    <div class="fit row inline wrap justify-around items-center content-center">
      <div class="col-12 col-sm-3 p1">
        <div class="op">
          <img class="option" src="1.png" />
          <q-btn
            class="btn1 q-mb-lg"
            flat
            to="/symptoms"
            label="Know More about Plant Diseases"
            size="15px"
            icon-right="eva-diagonal-arrow-right-up-outline"
            dense
          />
        </div>
      </div>

      <div class="col-12 col-sm-3 p1">
        <div class="op">
          <img class="option" src="3.jpg" />
          <q-btn
            class="btn1 q-mb-lg"
            flat
            to="/planthealthy"
            label="How to keep your plants healthy"
            size="15px"
            icon-right="eva-diagonal-arrow-right-up-outline"
            dense
          />
        </div>
      </div>

      <div class="col-12 col-sm-3 p1">
        <div class="op">
          <img class="option" src="4.jpg" />
          <q-btn
            class="btn1 q-mb-lg"
            flat
            to="/solution"
            label="Get Solutions for plant diseases"
            size="15px"
            icon-right="eva-diagonal-arrow-right-up-outline"
            dense
          />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {};
</script>

<style>
.p1 {
  border-radius: 50px;
}
</style>
