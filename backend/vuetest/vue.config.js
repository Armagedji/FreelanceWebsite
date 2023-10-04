const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: 'https://localhost:8080',
  outputDir: '../static/dict',
  indexPath: '../../templates/base_vue.html',

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  },

  transpileDependencies: true
})
