const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
  target: ["web", "es6"],
  context: path.join(__dirname, "../"),
  entry: {
    project: path.resolve(__dirname, "../", "api", "src", "project"),
    carousel: path.resolve(__dirname, "../", "api", "src", "carousel"),
  },
  output: {
    path: path.resolve(__dirname, "../", "dist", "webpack_bundles"),
    publicPath: "/static/webpack_bundles/",
    filename: "js/[name]-[fullhash].js",
    chunkFilename: "js/[name]-[hash].js",
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: [
          {
            loader: "ts-loader",
            options: {
              transpileOnly: true,
            },
          },
        ],
      },
      // we pass the output from babel loader to react-hot loader
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        exclude: /node_modules/,
      },

      {
        test: /\.s?css$/i,

        use: [
          // fallback to style-loader in development
          process.env.NODE_ENV !== "production"
            ? "style-loader"
            : MiniCssExtractPlugin.loader,
          // Translates CSS into CommonJS
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
            },
          },

          {
            loader: "postcss-loader",
            options: {
              sourceMap: true,
              postcssOptions: {
                plugins: ["postcss-preset-env", "autoprefixer", "pixrem"],
              },
            },
          },
          // // Compiles Sass to CSS
          // "resolve-url-loader",
          {
            loader: "sass-loader",
            options: {
              api: "modern-compiler",
              sassOptions: {
                // Your sass options
              },
              implementation: require("sass"),
            },
          },
        ],
      },
      {
        test: /\.(ttf|eot|woff|woff2)$/,
        use: {
          loader: "url-loader",
        },
      },
      {
        test: /\.(jpe?g|png|gif|svg|webp)$/i,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "/assets/[name].[ext]",
              publicPath: "/assets",
            },
          },
        ],
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js", ".jsx", "..."],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].[contenthash].css",
      chunkFilename: "css/[id].css",
    }),
    new BundleTracker({
      path: path.resolve(
        path.join(__dirname, "../", "dist", "webpack_bundles"),
      ),
      filename: "webpack-stats.json",
    }),
  ],
  optimization: {
    minimizer: [new CssMinimizerPlugin()],
  },
};
