<template>
  <q-card
    class="q-pa-md cardBack text-black text-bold fontChange"
    style="border-radius:20px; width:150px;height:150px;"
  >
    <div class="text-center column">
      <span class="flex flex-center">
        <q-img :src="plant.image" width="35px" height="35px" />
      </span>
      <br />
      {{ plant.name }}
    </div>
  </q-card>
</template>

<script>
export default {
  props: ["plant"]
};
</script>

<style></style>
