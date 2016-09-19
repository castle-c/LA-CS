'use strict'

angular.module('LACS')
  .config($routeProvider => {
    $routeProvider
      .when('/parishes', {
        controller: 'ParishesCtrl',
        templateUrl: '/app/parishes/parishes.html'
      })
    });
