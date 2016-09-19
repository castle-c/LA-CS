'use strict'

angular.module("LACS", ["ngRoute"])
  .factory("RootFactory", ($http, $timeout) => {
    let apiRoot = null;
    let httpGet = $http.get("http://localhost:8000");
    return {
      getApiRoot() {
        return httpGet.then(res => res.data)
      }
    }

  })
