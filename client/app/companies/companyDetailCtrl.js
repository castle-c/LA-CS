'use strict'

app.controller('CompanyDetailCtrl', [
    '$scope',
    '$http',
    '$timeout',
    '$routeParams',
      function ($scope, $http, $timeout, $routeParams) {
      $scope.title = "";
      $scope.companyKeyList = [];

      let logError = (err) => console.log("error", err);

          $http.get(`http://45.55.254.212:8000/companies/${$routeParams.companyId}`)

            .then(res => $scope.company = res.data)

            .then(() => {
              $http.get("http://45.55.254.212:8000/info")
              .then((res) => {
                // console.log(res.data)
                for (let d in res.data) {
                  let data = res.data[d];
                  // console.log(data.url)
                  // console.log($scope.company)
                  if (data.url === $scope.company.company_key) {
                    $scope.companyKeyList.push(data);
                    // console.log(data)
                  }
                  $timeout()
                }
                   logError
              });
            })


  }])
