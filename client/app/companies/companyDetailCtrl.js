'use strict'

angular.module("LACS")
  .controller('CompanyDetailCtrl', [
    '$scope',
    '$http',
    'RootFactory',
    '$timeout',
    '$routeParams',
    function ($scope, $http, RootFactory, $timeout, $routeParams) {
      $scope.title = "companies"

      let logError = (err) => console.log("error", err);

      RootFactory.getApiRoot()
      .then(
        root => {
          console.log(root)
          $http.get(`${root.companies}${$routeParams.companyId}`)
            .then(res => $scope.company = res.data)
        },
        logError
      )
  }])
