<template>
  <q-page class="constrain-more q-pa-md">
    <q-breadcrumbs class="text-grey" style="font-size: 19px">
      <q-breadcrumbs-el
        icon="eva-attach-outline"
        label="File Upload"
        to="/getstarted"
      />
      <q-breadcrumbs-el icon="camera" label="Take Photo" to="/camera" />
    </q-breadcrumbs>
    <div class="camera-frame q-pa-md">
      <video v-show="!imageCaptured" ref="video" class="full-width" autoplay />
      <canvas
        v-show="imageCaptured"
        ref="canvas"
        class="full-width"
        height="240"
      />
    </div>
    <div class="text-center q-pa-md">
      <q-btn
        v-if="hasCameraSupport"
        @click="captureImage"
        color="grey-10"
        icon="eva-camera"
        size="lg"
        round
      />
      <br />
      <br />
      <q-btn
        v-if="imageCaptured"
        @click="handleSubmit"
        label="Analyze"
        style="background-color:rgb(71, 107, 50);color:white"
      />
      <br />
      <br />
    </div>
    <div v-if="sendResult" class="text-center">
      <h6>Predicted class of image is {{ this.result }}.</h6>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "PageCamera",
  data() {
    return {
      image: null,
      result: null,
      sendResult: false,
      send: false,
      imageCaptured: false,
      hasCameraSupport: true
    };
  },

  methods: {
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
    },
    initCamera() {
      navigator.mediaDevices
        .getUserMedia({
          video: true
        })
        .then(stream => {
          this.$refs.video.srcObject = stream;
        })
        .catch(error => {
          this.hasCameraSupport = false;
        });
    },
    captureImage() {
      let video = this.$refs.video;
      let canvas = this.$refs.canvas;
      canvas.width = video.getBoundingClientRect().width;
      canvas.height = video.getBoundingClientRect().height;
      let context = canvas.getContext("2d");
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      this.imageCaptured = true;
      this.image = this.dataURItoBlob(canvas.toDataURL());
      this.disableCamera();
    },

    disableCamera() {
      this.$refs.video.srcObject.getVideoTracks().forEach(track => {
        track.stop();
      });
    },
    dataURItoBlob(dataURI) {
      // convert base64 to raw binary data held in a string
      // doesn't handle URLEncoded DataURIs - see SO answer #6850276 for code that does this
      var byteString = atob(dataURI.split(",")[1]);

      // separate out the mime component
      var mimeString = dataURI
        .split(",")[0]
        .split(":")[1]
        .split(";")[0];

      // write the bytes of the string to an ArrayBuffer
      var ab = new ArrayBuffer(byteString.length);

      // create a view into the buffer
      var ia = new Uint8Array(ab);

      // set the bytes of the buffer to the correct values
      for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }

      // write the ArrayBuffer to a blob, and you're done
      var blob = new Blob([ab], { type: mimeString });
      return blob;
    }
  },
  mounted() {
    this.initCamera();
  },
  beforeDestroy() {
    if (this.hasCameraSupport) {
      this.disableCamera();
    }
  }
};
</script>

<style lang="sass">
.camera-frame
    border: 2px solid $grey-10
    border-radius: 10px

.constrain
    max-width: 975px
    margin: 0 auto

.constrain-more
    max-width: 600px
    margin: 0 auto
</style>
