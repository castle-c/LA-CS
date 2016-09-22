'use strict'


app.config($routeProvider => {
  $routeProvider
    .when('/login', {
      controller: 'LoginController',
      templateUrl: '/app/auth/login.html'
    })
    .when('/register', {
      controller: 'LoginController',
      templateUrl: '/app/auth/register.html'
    });
})
