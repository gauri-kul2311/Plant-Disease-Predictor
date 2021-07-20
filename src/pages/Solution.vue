<template>
  <q-page class="mid flex flex-center">
    <div>
      <h3 class="text-center">Solutions</h3>
      <div class="column ">
        <span class="small-screen-only">
          <q-input v-model="search" filled label="Search" />
        </span>

        <div class="q-pa-lg flex flex-center row">
          <div
            v-for="plant in filteredPlants"
            :key="plant.name"
            class="q-pa-md"
          >
            <q-btn flat @click="alert(plant.solution)"
              ><PlantCard :plant="plant" />
            </q-btn>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import plantdata from "../assets/data.json";
import PlantCard from "../components/PlantCard";
export default {
  data() {
    return {
      pal: plantdata,
      temp: [],
      search: ""
    };
  },
  components: {
    PlantCard
  },
  methods: {
    alert(data) {
      var i, len, text;
      for (
        i = 0, len = data.length, text = '<ul class="text-subtitle1">';
        i < len;
        i++
      ) {
        text += "<li>" + data[i] + "</li>";
      }
      text += "</ul>";
      console.log("Text : - ", text);
      this.$q
        .dialog({
          title: "Solution",
          message: text,
          html: true
        })
        .onOk(() => {});
    }
  },
  created() {
    Object.keys(this.pal).forEach(plant => {
      this.temp.push(this.pal[plant]);
    });
  },
  computed: {
    filteredPlants: function() {
      return this.temp.filter(data => {
        return data.name.toLowerCase().match(this.search.toLowerCase());
      });
    }
  }
};
</script>

<style lang="sass">
.constrain-more
  max-width: 700px
  margin: 0 auto
</style>
