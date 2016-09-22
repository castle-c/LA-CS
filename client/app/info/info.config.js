'use strict'

  app.config($routeProvider => {
    $routeProvider
      .when('/info', {
        controller: 'InfoCtrl',
        templateUrl: '/app/info/info.html'
      })
      .when('/info/form', {
        controller: 'InfoCtrl',
        templateUrl: '/app/info/infoForm.html'
      })

  })

