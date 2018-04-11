var path = require('path');

PATHS = {
  app: path.join(__dirname, 'app'),
  build: path.join(__dirname, 'build')
};
module.exports = {
  module: {
   rules: [
     {
       test: /\.css$/,
       loaders: ['style-loader', 'css-loader'],
       include: PATHS.app
     },
     {
       test: /\.jsx?$/,
       loaders: ['babel-loader?cacheDirectory'],
       include: PATHS.app
     }
    ],
  },
  resolve: {
    extensions: ['.js','.jsx']
  },
  entry: {
      app: PATHS.app
  },
  output: {
    path: PATHS.build,
    filename: 'bundle.js',
  }
};
