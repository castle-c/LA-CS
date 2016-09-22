'use strict'

app.controller('ParishDetailCtrl', [
    '$scope',
    '$http',
    '$timeout',
    '$routeParams',
      function ($scope, $http, $timeout, $routeParams) {
      $scope.title = "parishes";
      $scope.parish = "";
      $scope.parishKeyList = [];

      let logError = (err) => console.log("error", err);

          $http.get(`http://45.55.254.212:8000/parishes/${$routeParams.parishId}`)

            .then(res => $scope.parish = res.data)

            .then(() => {
              $http.get("http://45.55.254.212:8000/companies")
              .then((res) => {
                for (let d in res.data) {
                  let data = res.data[d];
                  // console.log(data)
                  if (data.parish_key === $scope.parish.url) {
                    $scope.parishKeyList.push(data);
                // console.log(data)
                  }
                }

              });
            })

            logError

  }])
