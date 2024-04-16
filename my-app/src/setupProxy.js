// src/setupProxy.js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  app.use(
    createProxyMiddleware('/upload', {
      target: 'http://localhost:3000',
      changeOrigin: true,
    }),
  );
  app.use(
    createProxyMiddleware('/upload', {
      target: 'http://localhost:5000',
      changeOrigin: true,
    }),
  );
};