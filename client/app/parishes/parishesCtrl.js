app.controller('ParishesCtrl', [
    '$scope',
    '$http',
    '$timeout',

  function ($scope, $http, RootFactory, $timeout) {
    let logError = err => console.log("error", err)

  // $scope.getParish = function() {
    $http.get("http://localhost:8000/parishes")
     .then((res) => { $scope.parishes = res.data
          // console.log($scope.parishes)
          logError
     })
}])



