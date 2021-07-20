<template>
  <q-page style="border:solid black">
    <template>
      <div class="cont ">
        <div class="fill">
          <img class="img" src="../assets/bg.jpg" alt="Store Images" />
        </div>
        <div class="centered bgg">
          <div class="q-gutter-x-md q-pa-lg">
            <div class="text-h4 q-mt-xl text-center">
              Ways to keep your plant healthy
            </div>
            <ul class="text-h6">
              <li class="q-pt-lg">
                Find a site with the right light by observing the amounts of
                morning or afternoon sun they get before putting plants
              </li>
              <li class="q-pt-lg">
                Make pots hold water longer by tucking a damp sponge at the
                bottom of the pot.
              </li>
              <li class="q-pt-lg">
                Use ice cubes to water Place them around the soil, but not
                touching the stem. The ice will melt slowly, releasing water
                gradually and evenly into the soil.
              </li>
              <li class="q-pt-lg">
                Use fully composted yard waste when mixing it with soil.
              </li>
              <li class="q-pt-lg">
                Use infesticides to protect plants against the insects by
                applying a correct fertilizer.
              </li>
              <li class="q-pt-lg">
                Prune damaged limbs at the right time to prevent from further
                diseases.
              </li>
              <li class="q-pt-lg">Don’t Repot Your Plants by Pulling Them!</li>
              <li class="q-pt-lg">
                Dust Your Plants!Plants that collect too much dust on their
                leaves can’t get the sunlight they may need to survive. few
                times per year, use a wet cloth and lightly wipe down the leaves
                of your plants on both sides.
              </li>
            </ul>
          </div>
        </div>
      </div>
    </template>
  </q-page>
</template>

<script>
export default {};
</script>

<style>
@media (max-width: 480px) {
  .centered {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

@media (min-width: 480px) {
  .centered {
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

.bgg {
  width: fit-content;
  background: rgba(225, 225, 225, 0.5);
  color: rgb(15, 12, 12);
  border-radius: 5%;
}

.fill {
  display: flex;
  justify-content: center;
  align-items: center;
}
.fill img {
  flex-shrink: 0;
  min-width: 100%;
}
</style>
