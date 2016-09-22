
app.controller('CompaniesCtrl', [
    '$scope',
    '$http',
    '$timeout',

  function ($scope, $http, RootFactory, $timeout) {
    let logError = err => console.log("error", err)

    $http.get("http://45.55.254.212:8000/companies")
         .then((res) => { $scope.companies = res.data
          // console.log(res.data)
          logError
  })

  }])
