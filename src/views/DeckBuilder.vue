<template>
  <!-- <v-container fluid px-16 pb-10> -->
  <v-container>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-row class="d-flex flex-column align-center pt-8">
        <v-col cols="11" xl="8">
          <v-row>
            <v-col cols="12">
              <div class="text-center">
                <h1>{{ this.content.title }}</h1>
                <br />
                <!-- {{ temp }} -->
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-textarea
              v-model="deck_title"
              label="Deck Title"
              hint="No more than 30 characters"
              class="user-deck-title"
              auto-grow
              counter
              :rules="[rules.length(30)]"
            >
            </v-textarea>
          </v-row>
          <v-row>
            <v-textarea
              v-model="deck_description"
              label="Deck Description"
              hint="No more than 900 characters"
              row-height="40"
              auto-grow
              counter
              :rules="[rules.length(900)]"
            >
            </v-textarea>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-autocomplete
                v-model="selected_shikigami_names"
                v-on:input="limit_shikigami"
                :items="shikigami"
                label="Select Shikigami"
                chips
                multiple
                hint="Choose 4 Shikgigami for your deck."
                persistent-hint
                item-text="name"
                item-value="name"
              >
                <template v-slot:selection="data">
                  <v-chip
                    v-bind="data.attrs"
                    :input-value="data.selected"
                    close
                    medium
                    :x-large="$vuetify.breakpoint.mdAndUp"
                    @click="data.select"
                    @click:close="remove_shikigami(data.item)"
                    color="#C0B094"
                  >
                    <v-avatar left>
                      <v-img
                        :src="require(`@/assets/cards/${data.item.avatar}`)"
                      ></v-img>
                    </v-avatar>
                    {{ data.item.name }}
                  </v-chip>
                </template>
                <template v-slot:item="data">
                  <template>
                    <v-list-item-avatar>
                      <img
                        :src="require(`@/assets/cards/${data.item.avatar}`)"
                      />
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title
                        v-html="data.item.name"
                      ></v-list-item-title>
                      <v-list-item-subtitle
                        v-html="data.item.group"
                      ></v-list-item-subtitle>
                    </v-list-item-content>
                  </template>
                </template>
              </v-autocomplete>
            </v-col>
            <!-- selected_shikigami_names: {{ selected_shikigami_names }} <br /> -->
            <!-- selected_shikigami_data: {{ selected_shikigami_data }} <br /> -->
            <!-- selected_shikigami_decks: {{ selected_shikigami_decks }} -->
            <!-- deck_title: {{ deck_title }} -->
            <!-- breakpoint: {{ this.$vuetify.breakpoint.name }} -->
            <!-- {{ this.$vuetify.breakpoint.width }} -->
          </v-row>
          <v-row v-for="(_, index) in selected_shikigami_names" :key="index">
            <v-card
              elevation="2"
              width="100%"
              class="pa-3"
              flat
              tile
              color="#171D29"
            >
              <v-row>
                <v-col
                  cols="2"
                  class="flex-column justify-end d-none d-md-flex"
                >
                  <div class="">
                    <v-img
                      :src="
                        require(`@/assets/cards/${selected_shikigami_data[index].character_card}`)
                      "
                      width="100%"
                    ></v-img>
                  </div>
                </v-col>
                <v-col cols="12" md="10" class="d-flex flex-column"
                  ><v-row cols="12">
                    <v-select
                      v-model="selected_shikigami_decks[index]"
                      v-on:input="limit_decks"
                      :items="selected_shikigami_data[index].cards"
                      item-text="name"
                      item-value="id"
                      chips
                      multiple
                      hint="Choose 8 cards for your deck."
                      persistent-hint
                      return-object
                      clearable
                      :dense="$vuetify.breakpoint.mdAndDown"
                    >
                      <template v-slot:selection="data">
                        <v-chip
                          v-bind="data.attrs"
                          :input-value="data.selected"
                          close
                          label
                          :small="$vuetify.breakpoint.mdAndDown"
                          @click="data.select"
                          @click:close="remove_decks(index, data.index)"
                          color="#C0B094"
                          >{{ data.item.name }}</v-chip
                        ></template
                      >
                    </v-select>
                  </v-row>
                  <v-row cols="12" class="d-flex align-end justify-center pb-3">
                    <v-card
                      width="33%"
                      color="#171D29"
                      class="d-flex d-md-none pt-2"
                    >
                      <v-img
                        :src="
                          require(`@/assets/cards/${selected_shikigami_data[index].character_card}`)
                        "
                      ></v-img
                    ></v-card>
                    <v-card
                      v-for="i in selected_shikigami_decks[index]"
                      :key="i.id"
                      :width="cardWidth"
                      color="#171D29"
                      class="pt-2"
                    >
                      <v-img
                        :src="require(`@/assets/cards/${i.url}`)"
                        class="deck-card"
                      ></v-img
                    ></v-card> </v-row
                ></v-col>
              </v-row>
            </v-card>
          </v-row>
          <!-- <v-row>
            {{ dev() }}
            {{ output_shikigami_decks }}
          </v-row> -->
          <!-- <v-row>
            <v-textarea :value="construct_url()" color="teal"> </v-textarea>
          </v-row> -->
          <v-row class="d-flex justify-center pt-6">
            <v-col cols="12" class="text-center"
              >Ready to share? Make sure your title and description are valid
              and press the generate sharing link button below.
            </v-col>
            <v-col cols="12" class="text-center"
              >Problems generating the sharing link? Try reducing the length of
              your description even further, or use the long URL instead.
            </v-col>
          </v-row>
          <v-row v-if="this.short_url" class="d-flex justify-center">
            <v-col cols="12" md="6">
              <v-text-field
                v-model="this.short_url"
                append-icon="mdi-content-copy"
                ref="generated_url"
                @click:append="copy_url"
                :readonly="true"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row v-if="this.long_url" class="d-flex justify-center">
            <v-col cols="12" md="6">
              <v-text-field
                v-model="this.long_url"
                append-icon="mdi-content-copy"
                ref="generated_url"
                @click:append="copy_url"
                :readonly="true"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="d-flex justify-center pb-12">
            <v-btn
              :disabled="!valid"
              color="#C0B094"
              class="mr-0 mr-md-4 mb-5 mb-md-0"
              @click="validate_short_url"
              :loading="submit_button_waiting"
            >
              Generate sharing link </v-btn
            ><v-btn
              :disabled="!valid"
              color="#C0B094"
              :loading="submit_button_waiting"
              @click="validate_long_url"
            >
              Show long URL
            </v-btn></v-row
          >
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
import shikigami from "../data/shikigami_cards.json";
import axios from "axios";

export default {
  data: () => ({
    content: {
      title: "Deck Builder",
    },
    selected_shikigami_names: [],
    selected_shikigami_data: [],
    selected_shikigami_decks: [[], [], [], []],
    shikigami: shikigami,
    deck_title: "",
    deck_description: "",
    rules: {
      length: (len) => (v) =>
        (v || "").length <= len || `Must be less than ${len} characters.`,
    },
    valid: true,
    submit_button_waiting: false,
    short_url: "",
    long_url: "",
  }),
  methods: {
    get_chosen_shikigami_data: function (shikigami_name) {
      for (let i = 0; i < this.shikigami.length; i++) {
        try {
          if (this.shikigami[i].name == shikigami_name) {
            return this.shikigami[i];
          }
        } catch (err) {
          console.error(err);
        }
      }
    },
    limit_shikigami: function (e) {
      if (e.length == 5) {
        e.pop();
      }
    },
    limit_decks: function (e) {
      if (e.length == 9) {
        e.pop();
      }
    },
    remove_shikigami(item) {
      const index = this.selected_shikigami_names.indexOf(item.name);
      if (index >= 0) {
        this.selected_shikigami_names.splice(index, 1);
        this.selected_shikigami_decks[index].splice(0);
        // shuffle shikigami down by 1
        if (index <= 3) {
          for (let j = index; j <= 2; j++) {
            for (
              let i = 0;
              i < this.selected_shikigami_decks[j + 1].length;
              i++
            ) {
              // this if is optional?
              if (index < 3) {
                this.selected_shikigami_decks[j].push(
                  this.selected_shikigami_decks[j + 1][i]
                );
              }
            }
            this.selected_shikigami_decks[j + 1] = [];
          }
        }
      }
    },
    remove_decks(shiki_index, card_index) {
      ``;
      this.selected_shikigami_decks[shiki_index].splice(card_index, 1);
    },
    construct_url: function () {
      const saved_selected_shikigami_names = btoa(
        JSON.stringify(this.selected_shikigami_names)
      );
      const saved_output_shikigami_decks = btoa(
        JSON.stringify(this.output_shikigami_decks)
      );
      const saved_deck_title = btoa(JSON.stringify(this.deck_title));
      const saved_deck_description = btoa(
        JSON.stringify(this.deck_description)
      );
      const url = `https://dev.onmyojideckbuilder.com/deck-builder?d0=${saved_deck_title}&d1=${saved_deck_description}&d2=${saved_selected_shikigami_names}&d3=${saved_output_shikigami_decks}`;
      return url;
    },
    validate_long_url() {
      this.$refs.form.validate();
      this.submit_button_waiting = true;
      this.long_url = this.construct_url();
      this.submit_button_waiting = false;
    },
    async validate_short_url() {
      this.$refs.form.validate();
      this.submit_button_waiting = true;
      let config = {
        headers: {
          accept: "application/json",
          "X-Api-Key": process.env.VUE_APP_SHLINK_API_KEY,
          "Content-Type": "application/json",
        },
      };
      let data = {
        longUrl: this.construct_url(),
        validateUrl: false,
      };
      try {
        const result = await axios.post(
          process.env.VUE_APP_SHLINK_API_ENDPOINT,
          data,
          config
        );
        console.log(result);
        this.short_url = result.data.shortUrl;
      } catch (error) {
        // TODO: show options for an error
        this.short_url =
          "There was an error generating the sharing link. Either try again, use a shorter description or use the long URL.";
      }

      this.submit_button_waiting = false;
    },
    copy_url() {
      let url_to_copy = this.$refs.generated_url.$el.querySelector("input");
      url_to_copy.select();
      document.execCommand("copy");
    },
  },
  computed: {
    cardWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return "33%";
        case "sm":
          return "33%";
        case "md":
          return "12.3%";
        case "lg":
          return "12.3%";
        case "xl":
          return "12.3%";
      }
      return "12.3%";
    },
    output_shikigami_decks() {
      const output = [[], [], [], []];
      for (let i = 0; i < this.selected_shikigami_decks.length; i++) {
        for (let j = 0; j < this.selected_shikigami_decks[i].length; j++) {
          output[i].push(this.selected_shikigami_decks[i][j].id);
        }
      }
      return output;
    },
  },
  mounted() {
    if (this.$route.query.d2) {
      const saved_selected_shikigami_names = JSON.parse(
        atob(this.$route.query.d2)
      );

      if (typeof saved_selected_shikigami_names != "object") {
        this.selected_shikigami_names = [];
      } else {
        this.selected_shikigami_names = [];
        for (let i = 0; i < saved_selected_shikigami_names.length; i++) {
          this.selected_shikigami_names.push(saved_selected_shikigami_names[i]);
        }
      }
    } else {
      this.selected_shikigami_names = [];
    }

    if (this.$route.query.d0) {
      const saved_deck_title = JSON.parse(atob(this.$route.query.d0));

      if (typeof saved_deck_title != "string") {
        this.deck_title = "";
      } else {
        this.deck_title = "";
        for (let i = 0; i < saved_deck_title.length; i++) {
          this.deck_title = saved_deck_title;
        }
      }
    } else {
      this.deck_title = "";
    }

    if (this.$route.query.d1) {
      const saved_deck_description = JSON.parse(atob(this.$route.query.d1));

      if (typeof saved_deck_description != "string") {
        this.deck_description = "";
      } else {
        this.deck_description = "";
        for (let i = 0; i < saved_deck_description.length; i++) {
          this.deck_description = saved_deck_description;
        }
      }
    } else {
      this.deck_description = "";
    }

    this.$nextTick(function () {
      if (this.$route.query.d3) {
        const saved_output_shikigami_decks = JSON.parse(
          atob(this.$route.query.d3)
        );
        console.log(saved_output_shikigami_decks);
        if (typeof saved_output_shikigami_decks != "object") {
          // do nothing: array will be empty
        } else {
          for (let i = 0; i < this.selected_shikigami_data.length; i++) {
            for (let k = 0; k < saved_output_shikigami_decks[i].length; k++) {
              for (
                let j = 0;
                j < this.selected_shikigami_data[i].cards.length;
                j++
              ) {
                if (
                  saved_output_shikigami_decks[i][k] ==
                  this.selected_shikigami_data[i].cards[j].id
                ) {
                  this.selected_shikigami_decks[i].push(
                    this.selected_shikigami_data[i].cards[j]
                  );
                }
              }
            }
          }
        }
      }
    });
  },
  watch: {
    selected_shikigami_names: function () {
      this.selected_shikigami_data = [];
      for (let i = 0; i < this.selected_shikigami_names.length; i++) {
        for (let j = 0; j < this.shikigami.length; j++) {
          try {
            if (this.shikigami[j].name == this.selected_shikigami_names[i]) {
              this.selected_shikigami_data.push(this.shikigami[j]);
            }
          } catch (err) {
            /* nothing */
          }
        }
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "~vuetify/src/styles/styles.sass";

.v-chip .v-avatar {
  width: 20px !important;
}

@media #{map-get(
    $display-breakpoints,
    "md-and-up"
  )} {
  .v-chip .v-avatar {
    height: 60px !important;
    width: 60px !important;
  }

  .deck-card:hover {
    position: relative;
    animation: card-zoom 500ms ease-in-out 0s forwards;
    z-index: 100;
  }
}

@keyframes card-zoom {
  100% {
    transform: scale(1.85);
  }
}

.v-textarea textarea {
  padding: 50px 0px 0px 0px !important;
}

.user-deck-title {
  font-size: 50px !important;
}
</style>

<style lang="scss">
.user-deck-title {
  & textarea {
    padding-top: 10px !important;
    padding-bottom: 15px !important;
    text-align: center;
    line-height: 3rem;
  }
}
</style>
