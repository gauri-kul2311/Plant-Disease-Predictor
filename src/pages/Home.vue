<template>
  <q-page>
    <homehead />
    <homemid />
  </q-page>
</template>

<script>
export default {
  name: "PageIndex",

  components: {
    homehead: require("src/components/Home/HomeHead.vue").default,
    homemid: require("src/components/Home/HomeMid.vue").default
  }
};
</script>
<style></style>
