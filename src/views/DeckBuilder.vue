<template>
  <!-- <v-container fluid px-16 pb-10> -->
  <v-container>
    <v-row class="d-flex flex-column align-center pt-8">
      <v-col cols="11">
        <v-row>
          <v-col cols="12">
            <div class="text-center">
              <h1>Deck Builder</h1>
              <br />
              <!-- {{ temp }} -->
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-textarea
            v-model="deck_title"
            label="Deck Title"
            class="user-deck-title"
            rows="1"
            row-height="80"
          ></v-textarea>
        </v-row>
        <v-row>
          <v-textarea v-model="deck_description" label="Deck Description">
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
                  x-large
                  @click="data.select"
                  @click:close="remove_shikigami(data.item)"
                  color="#C0B094"
                >
                  <v-avatar size="90" left>
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
                    <img :src="require(`@/assets/cards/${data.item.avatar}`)" />
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
          breakpoint: {{ this.$vuetify.breakpoint.name }}
          {{ this.$vuetify.breakpoint.width }}
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
              <v-col cols="2" class="d-flex flex-column justify-end">
                <div cols="12" class="">
                  <v-img
                    :src="
                      require(`@/assets/cards/${selected_shikigami_data[index].character_card}`)
                    "
                    width="100%"
                  ></v-img>
                </div>
              </v-col>
              <v-col cols="10" class="d-flex flex-column"
                ><v-row cols="12">
                  <!-- <v-row cols="12" class="d-none"> -->
                  <!-- {{ index }} -->
                  <!-- {{ selected_shikigami_decks[index][index].length }} -->
                  <v-select
                    v-model="selected_shikigami_decks[index][index]"
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
                  >
                    <template v-slot:selection="data">
                      <v-chip
                        v-bind="data.attrs"
                        :input-value="data.selected"
                        close
                        label
                        @click="data.select"
                        @click:close="remove_decks(index, data.index)"
                        color="#C0B094"
                        >{{ data.item.name }}</v-chip
                      ></template
                    >
                  </v-select>
                </v-row>
                <!-- <div cols="12">
                  {{ selected_shikigami_decks[index][index] }}
                </div> -->
                <v-row cols="12" class="d-flex align-end pb-3">
                  <v-card
                    v-for="i in selected_shikigami_decks[index][index]"
                    :key="i.id"
                    width="12.3%"
                    color="#171D29"
                  >
                    <!-- <div class="text-center">
                  {{ i.name }}
                </div> -->
                    <div class="">
                      <v-img
                        :src="require(`@/assets/cards/${i.url}`)"
                        class="deck-card"
                      ></v-img></div
                  ></v-card> </v-row
              ></v-col>
            </v-row>
          </v-card>
        </v-row>
        <v-row v-for="(_, index) in selected_shikigami_names" :key="index">
          <v-col class="pa-0" cols="9">
            <v-card
              elevation="2"
              width="100%"
              class=""
              flat
              tile
              color="#171D29"
              ><v-col cols="12" class="my-n1">
                <div class="d-flex">
                  <v-img
                    :src="
                      require(`@/assets/cards/${selected_shikigami_data[index].character_card}`)
                    "
                    width="11.1%"
                    class="px-1"
                  ></v-img
                  ><v-img
                    :src="require(`@/assets/cards/${i.url}`)"
                    class="px-1"
                    v-for="i in selected_shikigami_decks[index][index]"
                    :key="i.id"
                    width="12%"
                  ></v-img></div></v-col
            ></v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-textarea :value="construct_url()" color="teal"> </v-textarea>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import shikigami from "../data/shikigami_cards.json";
export default {
  data: () => ({
    selected_shikigami_names: [],
    selected_shikigami_data: [],
    selected_shikigami_decks: [{ 0: [] }, { 1: [] }, { 2: [] }, { 3: [] }],
    shikigami: shikigami,
    deck_title: "",
    deck_description: "",
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
        this.selected_shikigami_decks[index][index].splice(0);
        // shuffle shikigami down by 1
        if (index <= 3) {
          for (let j = index; j <= 2; j++) {
            for (
              let i = 0;
              i < this.selected_shikigami_decks[j + 1][j + 1].length;
              i++
            ) {
              // this if is optional?
              if (index < 3) {
                this.selected_shikigami_decks[j][j].push(
                  this.selected_shikigami_decks[j + 1][j + 1][i]
                );
              }
            }
            this.selected_shikigami_decks[j + 1][j + 1] = [];
          }
        }
      }
    },
    remove_decks(shiki_index, card_index) {
      ``;
      this.selected_shikigami_decks[shiki_index][shiki_index].splice(
        card_index,
        1
      );
      console.log(this.selected_shikigami_decks[shiki_index].shiki_index);
      console.log(shiki_index, card_index);
    },
    construct_url: function () {
      const saved_selected_shikigami_names = btoa(
        JSON.stringify(this.selected_shikigami_names)
      );
      const saved_selected_shikigami_decks = btoa(
        JSON.stringify(this.selected_shikigami_decks)
      );
      const saved_deck_title = btoa(JSON.stringify(this.deck_title));
      const saved_deck_description = btoa(
        JSON.stringify(this.deck_description)
      );
      const url = `?deck_title=${saved_deck_title}&deck_description=${saved_deck_description}&selected_shikigami_names=${saved_selected_shikigami_names}&selected_shikigami_decks=${saved_selected_shikigami_decks}`;
      return url;
    },
  },
  computed: {},
  mounted() {
    if (this.$route.query.selected_shikigami_names) {
      const saved_selected_shikigami_names = JSON.parse(
        atob(this.$route.query.selected_shikigami_names)
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

    if (this.$route.query.selected_shikigami_decks) {
      const saved_selected_shikigami_decks = JSON.parse(
        atob(this.$route.query.selected_shikigami_decks)
      );

      if (typeof saved_selected_shikigami_decks != "object") {
        this.selected_shikigami_decks = [
          { 0: [] },
          { 1: [] },
          { 2: [] },
          { 3: [] },
        ];
      } else {
        this.selected_shikigami_decks = [];
        for (let i = 0; i < saved_selected_shikigami_decks.length; i++) {
          this.selected_shikigami_decks.push(saved_selected_shikigami_decks[i]);
        }
      }
    } else {
      this.selected_shikigami_decks = [
        { 0: [] },
        { 1: [] },
        { 2: [] },
        { 3: [] },
      ];
    }

    if (this.$route.query.deck_title) {
      const saved_deck_title = JSON.parse(atob(this.$route.query.deck_title));

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

    if (this.$route.query.deck_description) {
      const saved_deck_description = JSON.parse(
        atob(this.$route.query.deck_description)
      );

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
.v-chip .v-avatar {
  height: 60px !important;
  width: 60px !important;
}

.deck-card:hover {
  position: relative;
  animation: card-zoom 500ms ease-in-out 0s forwards;
  z-index: 100;
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
.user-deck-title textarea {
  padding-top: 10px !important;
  padding-bottom: 15px !important;
  text-align: center;
}
</style>
