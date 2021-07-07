const path = require('path')
const argv = require('optimist').argv
let config = {}
let command = argv['_'][0]
switch(command) {
  case 'build':
    config = {
      publicPath: '/static',
      assetsDir: './',
      outputDir: '../api/static',
      pages: {
        app: {
          entry: 'src/main.js',
          template: 'public/index.html',
          filename: 
            path.resolve(
              '../api/templates', 'index.html'),
          title: 'Simple Blog Project'
        }
      }
    }
    break
  case 'serve':
    config = {
      devServer: {
        proxy: 'http://localhost:8080'
      }
    }
}
module.exports = config