const app = angular.module('LACS', ['ngRoute', 'ngCookies'])
app.constant('apiUrl', "http://localhost:8000")

  app.factory('RootFactory', [
    "$http", "apiUrl",
    ($http, apiUrl) => {
      let apiRoot = null;
      let httpGet = $http.get(apiUrl);
      let userCredentials = {};

      return {
        getApiRoot () {
          return httpGet.then(res => res.data)
        }
      }
    }
  ])

  app.run((AuthFactory) => {
  AuthFactory.read();
});

