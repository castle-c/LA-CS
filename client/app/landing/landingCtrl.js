
app.controller('LandingCtrl', [
    '$scope',
    '$http',
    '$timeout',
    '$routeParams',

  function ($scope, $http, $timeout) {
    let logError = err => console.log("error", err)


    $http.get("http://localhost:8000/parishes")
         .then((res) => { $scope.parishes = res.data
          // console.log('freferfrefe', $scope.parishes)
          logError
       })
       }])


