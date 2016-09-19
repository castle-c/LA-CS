angular.module("LACS")
  .config(($routeProvider) => {
    $routeProvider
      .when("/", {
        controller: "LandingCtrl",
        templateUrl: "/app/landing/landing.html"
      })
  })
