<template>
    <iframe app fluid ref="iframe" id="iframe" :src="`http://127.0.0.1:5000/client?sso=${$store.getters.sso_token}`"
        scrolling="no" frameborder="0" allowtransparency="true"
        style="width: 0; min-width: 100% !important; min-height: 100%;" />
</template>
  
<script>

function initialState() {
    return {
        //
    };
}

export default {
    name: "NitroClient",

    data: function () {
        return initialState();
    },
};
</script>