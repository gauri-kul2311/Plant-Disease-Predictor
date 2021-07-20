<template>
  <q-page class="getstartedbase">
    <div class="getstartedbase">
      <div class="text-center q-pa-md q-mr-lg">
        <div class="text-center">
          <h5>
            Share a picture of plant and get immediate result!
          </h5>
          <q-btn icon="camera" label="Take Photo" 
          to="/camera"
          stack glossy color="green" />
          <h5>OR</h5>

        </div>
        <div class="analyze">
          <br />
          <div class="kk">
            <input
              type="file"
              class="image"
              accept="image/png, image/jpeg"
              defaultValue=""
              @change="handleImageChange"
              required
            />
            <br />
            <br />
            <img class="inputImage" :src="file" alt="" />
            <br />
            <br />
            <q-btn @click="handleSubmit" label="Analyze" />
            <br />
            <br />
          </div>
        </div>
        <br />
        <div v-if="sendResult">
          <b>Result : {{ this.result }}</b>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      image: null,
      result: null,
      sendResult: false,
      send: false,
      file: null
    };
  },
  methods: {
    handleImageChange(e) {
      (this.image = e.target.files[0]),
        (this.sendResult = false),
        (this.send = false),
        (this.file = URL.createObjectURL(e.target.files[0]));
      console.log(this.file);
    },
    getImageResult(id) {
      this.$axios.get(`http://127.0.0.1:8000/api/plants/${id}/`).then(res => {
        this.result = res.data.result;
        this.sendResult = true;
      });
    },
    handleSubmit(e) {
      e.preventDefault();
      console.log("Hello!");
      let form_data = new FormData();
      form_data.append("image", this.image, this.image.name);
      let url = "http://localhost:8000/api/plants/";
      this.$axios
        .post(url, form_data, {
          headers: {
            "content-type": "application/json"
          }
        })
        .then(res => {
          console.log(res.data);
          this.getImageResult(res.data.id);
          this.send = true;
        })
        .catch(err => console.log(err));
    }
  }
};
</script>

<style></style>
