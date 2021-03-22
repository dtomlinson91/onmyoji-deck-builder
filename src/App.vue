<template>
  <v-app>
    <v-navigation-drawer
      v-model="primaryDrawer.model"
      :clipped="false"
      :floating="false"
      :mini-variant="false"
      app
      :expand-on-hover="true"
      overflow
      color="#272935"
    >
      <v-list>
        <v-list-item
          v-for="item in primaryDrawer.items"
          :key="item.title"
          link
          :to="item.link"
        >
          <v-list-item-icon>
            <!-- <v-icon>{{ item.icon }}</v-icon> -->
            <v-img :src="item.icon" width="50"></v-img>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title class="text-button">{{
              item.title
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar :clipped-left="false" app color="#272935" hide-on-scroll>
      <v-app-bar-nav-icon
        @click.stop="primaryDrawer.model = !primaryDrawer.model"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>Onmyoji Deck Builder</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

    <!-- <v-footer :inset="false" color="#272935" app>
      <span class="px-2">
        <v-icon>{{ icons.mdiGithub }}</v-icon> View on GitHub
      </span>
    </v-footer> -->
  </v-app>
</template>

<script>
import {
  mdiGithub,
} from "@mdi/js";

const home_icon = require(`@/assets/navbar/0000034a.png`);
const deck_icon = require(`@/assets/navbar/00000047.png`);
const help_icon = require(`@/assets/navbar/00000121.png`);

export default {
  name: "App",

  data: () => ({
    primaryDrawer: {
      model: true,
      items: [
        { title: "Home", icon: home_icon, link: "/" },
        { title: "Deck Builder", icon: deck_icon, link: "deck-builder" },
        { title: "Help", icon: help_icon, link: "help" },
      ],
    },
    icons: {
      mdiGithub: mdiGithub,
    },
  }),
};
</script>
