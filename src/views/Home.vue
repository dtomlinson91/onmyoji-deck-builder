<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12" class="d-flex justify-center">
        <v-img
          :src="require(`@/assets/homepage/${random_welcome_image()}`)"
          class=""
          contain
          max-width="390px"
        />
      </v-col> </v-row
    ><v-row class="pt-16 pt-md-4">
      <v-col class="d-flex flex-column justify-center align-center text-center">
        <h1 class="display-2 font-weight-bold">
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
        >
          <p class="mb-0 text-center text-button">Changelog</p>
          <div v-for="i in this.changelog" :key="i.date">
            <p class="pl-4 mb-0 text-button">{{ i.date }}</p>
            <ul class="text-button">
              <li v-for="j in i.changes" :key="j" class="changelog-item">
                {{ j }}
              </li>
            </ul>
          </div>
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
      subtitle: "Make and share decks online for Onmyoji TCG.",
    },
    changelog: [
      {
        date: "2021-03-24",
        changes: ["Initial release"],
      },
      // { date: "2021-03-23", changes: ["Initial release 3"] },
    ],
  }),
  methods: {
    random_welcome_image() {
      const random = Math.floor(Math.random() * this.welcome_images.length);
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
  line-height: 1.8rem !important;
}
</style>
