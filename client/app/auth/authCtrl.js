
  app.controller('LoginController', [
    '$scope',
    '$http',
    '$location',
    'RootFactory',
    'AuthFactory',
    'apiUrl',

    function($scope, $http, $location, RootFactory, AuthFactory, apiUrl) {

      // Default values for scope variables
      $scope.user = {
        username: "",
        password: ""
      };
      $scope.root = null;


      $scope.register = function() {
        $http({
          url: `${apiUrl}/register`,
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          data: {
            "username": $scope.user.username,
            "password": $scope.user.password,
          }
        }).success(res => {
          if (res.data !== null) {
            /*
            Registration was successful. The register_user method in the Django
            application also handles login, so the client can store credentials
            for use in requests to API that require permissions
             */
            AuthFactory.credentials({
              username: $scope.user.username,
              password: $scope.user.password
            });

            $location.path('/');
          }
        }).error(console.error);
      };

      /*
        Post the user-provided credentials to API
       */
      $scope.login = function() {
        $http({
          url: `${apiUrl}/login`,
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          data: {
            "username": $scope.user.username,
            "password": $scope.user.password
          }
        }).then(
          res => {
            if (res.data !== null) {
              /*
              Login was successful, store credentials for use in requests
              to API that require permissions
               */
              AuthFactory.credentials({
                username: $scope.user.username,
                password: $scope.user.password
              });

              // Redirect to ticket list on successful login
              $location.path('/');
            } else {
              console.error("Invalid username or password");
            }
          },
          err => console.error
        );
      };
    }])
