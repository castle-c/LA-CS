'use strict'

angular.module("LACS")
  .controller('ParishesCtrl', [
    '$scope',
    '$http',
    'RootFactory',
    '$timeout',
    function ($scope, $http, RootFactory, $timeout) {
      $scope.title = "parishes"
      $scope.apiRoot = null;

      RootFactory.getApiRoot()
          .then(
            root => {
              $scope.apiRoot = root;
              $http.get(`${root.parishes}`)
                .then(
                  res => {
                    $scope.parishes = res.data
                    console.log("parishes", $scope.parishes);
                });
              $timeout();
            },
            err => console.log("error", err)
          )
        }])
