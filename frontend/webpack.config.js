const HtmlWebPackPlugin = require("html-webpack-plugin");
const path = require('path');
const webpack = require('webpack')
const dotenv = require('dotenv-webpack')

module.exports = () => {
  return {
    entry: './src/index.tsx',
    output: {
      filename: 'main.js',
      path: path.resolve(__dirname, 'dist'),
    },
    plugins: [
      new webpack.ProvidePlugin({
        process: 'process/browser',
      }),
      new HtmlWebPackPlugin({
        template: "./public/index.html",
        filename: "index.html",
        minify: {
          removeComments: true,
          collapseWhitespace: true,
          removeAttributeQuotes: true,
        },
      }),
      new dotenv()
    ],
    resolve: {
      extensions: [".tsx", ".ts", ".jsx", ".js", ".json"],
    },
    module: {
      rules: [
        {
          use: ["ts-loader"],
          test: /\.ts$|tsx/,
          exclude: [/node_modules/],
        },
        {
            test: /\.css$/,
            use: [
              'style-loader',
              'css-loader'
            ]
          }
      ],
    },
    devServer: {
      historyApiFallback: true,
      port: 3000,
      allowedHosts: "all"
    },
  };
};
