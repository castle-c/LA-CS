app.controller('InfoCtrl', [
    '$scope',
    '$http',
    '$timeout',
    function($scope, $http, $timeout) {
        let logError = err => console.log("error", err)
        let info = null
        $scope.companyKey = ''
        $scope.formData = {}
        $scope.parishFormData = {}



        $scope.processForm = function() {

            $http.post("http://localhost:8000/info/", $scope.formData)
              .then(res =>  $scope.companyKey = res.data)
                   .then(() => {
                    $scope.parishFormData.company_key = $scope.companyKey.url;
                    $http.post("http://localhost:8000/companies/", $scope.parishFormData)
                    .success((res) => console.log(res))
                    .error(logError)

                  })
              }


        $scope.getParish = function() {
            $http.get("http://localhost:8000/parishes")
            .then((res) => { $scope.parishes = res.data
              // console.log($scope.parishes)
              logError
     })
   }

        $http.get("http://localhost:8000/info")
            .then((res) => {
                $scope.info = res.data
                    // console.log('info', $scope.info)
                logError
            }).then(() => {
                // console.log($scope.info)



            })
    }
])
