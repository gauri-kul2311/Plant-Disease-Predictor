<template>
  <q-page class="text-center">
    <span class="large-screen-only">
      <img src="Picture1.png" />
    </span>
    <img src="Picture1.png" class="fit small-screen-only" />
    <div class="constrain-more q-pa-md">
      <q-breadcrumbs class="text-grey" style="font-size:19px">
        <q-breadcrumbs-el label="Take Photo" icon="camera" to="/camera" />
        <q-breadcrumbs-el
          label="File Upload"
          icon="eva-attach-outline"
          to="/getstarted"
        />
      </q-breadcrumbs>

      <div class="camera-frame q-pa-md">
        <canvas ref="canvas" class="fit" />
      </div>
      <div class="text-center q-pa-md">
        <q-file
          @input="captureImageFallback"
          v-model="imageUpload"
          label="Choose an image"
          accept="image/*"
          outlined
        >
          <template v-slot:prepend>
            <q-icon name="eva-attach-outline" />
          </template>
        </q-file>
        <br />
        <q-btn
          style="background-color:rgb(71, 107, 50);color:white"
          @click="handleSubmit"
          label="Analyze"
        />
      </div>
    </div>
    <div v-if="sendResult" class="back text-center text-green-9 text-bold ">
      <span class="text-h4 large-screen-only">
        Predicted class of image is {{ this.result }}.
      </span>
      <span class="text-h6 small-screen-only">
        Predicted class of image is {{ this.result }}.
      </span>
      <q-btn
        type="a"
        class="q-mt-xl large-screen-only"
        flat
        no-caps
        size="xl"
        to="/solution"
        label="To know how to treat the disease , please visit out solution page"
        icon-right="eva-diagonal-arrow-right-up-outline"
      ></q-btn>
      <q-btn
        type="a"
        class="q-mt-xl small-screen-only"
        flat
        no-caps
        size="sm"
        to="/solution"
        icon-right="eva-diagonal-arrow-right-up-outline"
        >To know how to treat the disease , please visit out solution
        page</q-btn
      >
    </div>
  </q-page>
</template>

<script>
export default {
  name: "PageCamera",
  data() {
    return {
      imageUpload: [],
      image: null,
      result: null,
      sendResult: false,
      send: false,
      file: null
    };
  },
  methods: {
    captureImageFallback(file) {
      console.log("Hello");
      this.image = file;
      this.sendResult = false;
      let canvas = this.$refs.canvas;
      let context = canvas.getContext("2d");

      var reader = new FileReader();
      reader.onload = event => {
        var img = new Image();
        img.onload = () => {
          canvas.width = img.width;
          canvas.height = img.height;
          context.drawImage(img, 0, 0);
          this.imageCaptured = true;
        };
        img.src = event.target.result;
      };
      reader.readAsDataURL(file);

      console.log(this.image);
    },
    getImageResult(id) {
      this.$axios.get(`http://127.0.0.1:8000/api/plants/${id}/`).then(res => {
        this.result = res.data.result;
        this.timer = setTimeout(() => {
          this.$q.loading.hide();
          this.sendResult = true;
          this.timer = void 0;
        }, 2500);
      });
    },
    handleSubmit(e) {
      this.$q.loading.show();
      e.preventDefault();
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
<style lang="sass">
.camera-frame
    border: 2px solid $grey-10
    border-radius: 10px
.small-screen-only
    @media (max-width: $breakpoint-xs-max)
        display: block
    @media (min-width: $breakpoint-sm-min)
        display: none

.large-screen-only
    @media (max-width: $breakpoint-xs-max)
        display: none
    @media (min-width: $breakpoint-sm-min)
        display: block

.constrain
    max-width: 975px
    margin: 0 auto

.constrain-more
    max-width: 600px
    margin: 0 auto
</style>
