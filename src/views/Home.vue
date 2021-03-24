<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require(`@/assets/homepage/${random_welcome_image()}`)"
          class="mb-n12 my-md-3"
          contain
          height="500"
        />
      </v-col>
      <v-col
        class="mb-0 mb-md-4 d-flex flex-column justify-center align-center"
      >
        <h1 class="display-2 font-weight-bold mb-0 mb-md-3">
          {{ this.content.title }}
        </h1>
        <p class="subheading font-weight-regular">
          {{ this.content.subtitle }}
        </p>
        <v-col cols="12" md="6" class="d-flex justify-center">
          <router-link to="/deck-builder" style="text-decoration: none"
            ><v-btn elevation="2" x-large color="#C0B094" class="mr-2 mr-md-4"
              >Get started</v-btn
            ></router-link
          >
          <router-link to="/help" style="text-decoration: none"
            ><v-btn elevation="2" x-large color="#C0B094"
              >Instructions</v-btn
            ></router-link
          ></v-col
        >
      </v-col>
    </v-row>
    <v-row class="pb-10 d-flex justify-center">
      <v-col col="12" md="4">
        <v-card
          class="mx-auto pa-4 text-justify"
          width="100%"
          color="#171D29"
          tile
          style="line-height: 2rem !important"
        >
          <p class="mb-0 text-center text-button">Changelog</p>
          <p class="pl-4 mb-0 text-button">2021-03-24</p>
          <ul class="text-button">
            <li class="changelog-item">Initial release</li>
          </ul>
          <!-- <p class="mb-0">2021-03-24</p>
          <ul class="text-justify">
            <li>1</li>
            <li>1</li>
            <li>1</li>
            <li>1</li>
          </ul> -->
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    welcome_images: [
      "000000c6.png",
      "00000131.png",
      "00000143.png",
      "0000015c.png",
      "00000203.png",
      "000002d4.png",
      "0000033a.png",
      "000003c0.png",
      "00000403.png",
      "00000426.png",
      "00000431.png",
      "0000044a.png",
      "00000544.png",
      "000005ce.png",
      "0000066e.png",
      "0000069d.png",
      "0000073d.png",
    ],
    content: {
      title: "Onmyoji Deck Builder",
      subtitle: "Make and share decks."
    },
    changelog: {
      [{date:"", changes: [""]}]
    }
  }),
  methods: {
    random_welcome_image() {
      const random = Math.floor(Math.random() * this.welcome_images.length);
      console.log(this.welcome_images[random]);
      return this.welcome_images[random];
    },
  },
};
</script>

<style lang="scss" scoped>
.text-button {
  line-height: 1.8rem !important;
}

.changelog-item {
  font-size: 0.8rem !important;
}
</style>
