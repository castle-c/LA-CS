'use strict'

angular.module("LACS")
.controller('ParishDetailCtrl', [
    '$scope',
    '$http',
    '$timeout',
    '$routeParams',
      function ($scope, $http, $timeout, $routeParams) {
      $scope.title = "parishes";
      $scope.parish = "";
      $scope.parishKeyList = [];

      let logError = (err) => console.log("error", err);

          $http.get(`http://localhost:8000/parishes/${$routeParams.parishId}`)

            .then(res => $scope.parish = res.data)

            .then(() => {
              $http.get("http://localhost:8000/companies")
              .then((res) => {
                // console.log(res.data) --json
                for (let d in res.data) {
                  let data = res.data[d];
                  if (data.parish_key === $scope.parish.url) {
                    $scope.parishKeyList.push(data);
                // console.log(data)
                  }
                }

              });
            })

            logError

  }])
