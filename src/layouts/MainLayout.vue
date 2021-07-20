<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="tool">
        <q-toolbar-title class="q-pl-lg">
          Disease Predictor
        </q-toolbar-title>
        <div class="absolute-right">
          <q-btn class="btn-home" to="/" flat icon="home" size="15px" />
          <!-- <q-btn
            class="btn"
            to="/getstarted"
            flat
            label="Get Started"
            size="15px"
          /> -->
          <!-- <q-btn class="btn" flat label="Diseases" size="15px" />
          <q-btn class="btn" flat label="History" size="15px" /> -->
        </div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "MainLayout",
  data() {
    return {};
  }
};
</script>
<style>
.tool {
  background-color: rgb(39, 61, 37);
}

</style>
