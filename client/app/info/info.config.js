'use strict'

angular.module('LACS')
  .config($routeProvider => {
    $routeProvider
      .when('/info', {
        controller: 'InfoCtrl',
        templateUrl: '/app/info/info.html'
      })

  })

