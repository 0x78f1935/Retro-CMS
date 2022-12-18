<template>
    <v-app-bar app>
        <v-img :src="$store.getters.app_name_logo" max-height="50" max-width="150"></v-img>
        <v-spacer></v-spacer>
        <v-btn>HOME</v-btn>
        <v-btn>COMMUNITY</v-btn>
        <v-btn>SHOP</v-btn>
        <v-btn>ABOUT HABBO</v-btn>
    </v-app-bar>
</template>
    
<script>
import axios from "axios";
import { InfoMutations } from "@/store/info/mutations";

function initialState() {
    return {

    };
}

export default {
    name: "AppBar",

    data: function () {
        return initialState();
    },

    components: {
        //
    },

    created() {
        this.info();
    },

    methods: {
        info() {
            axios
                .get("/api/v1/info/app")
                .then((response) => {
                    if (response.status == 200) {
                        this.$store.commit(InfoMutations.SET_APP_LONG_NAME, response.data.name_long);
                        this.$store.commit(InfoMutations.SET_APP_SHORT_NAME, response.data.name_short);
                        this.$store.commit(InfoMutations.SET_APP_NAME_LOGO, response.data.logo);
                        return;
                    }
                    console.error(response.data);
                })
                .catch((e) => {
                    if (e.response.data["message"]) {
                        console.error(e.response.data.message);
                    }
                });
        },
    },
};
</script>
  