const { defineConfig } = require('@vue/cli-service')
const path = require("path")
module.exports = defineConfig({
  transpileDependencies: true,

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  },

  outputDir: path.resolve(
    __dirname,
    "../../backend/templates/frontend/CMS"
  ),

  assetsDir: "../../../../backend/static/frontend/CMS",
})
