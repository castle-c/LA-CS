'use strict'

angular.module("LACS")
  .controller('CompaniesCtrl', [
    '$scope',
    '$http',
    'RootFactory',
    '$timeout',
    function ($scope, $http, RootFactory, $timeout) {
      $scope.title = "companies"
      $scope.apiRoot = null;

      RootFactory.getApiRoot()
          .then(
            root => {
              $scope.apiRoot = root;
              $http.get(`${root.companies}`)
                .then(
                  res => {
                    $scope.companies = res.data
                    console.log("companies", $scope.companies);
                });
              $timeout();
            },
            err => console.log("error", err)
          )
        }])
